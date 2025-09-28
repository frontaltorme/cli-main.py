#!/usr/bin/env python3
"""
Address TX Exporter (Etherscan)
Fetches normal transactions for an address and exports to CSV.

Usage:
  python -m cli 0xADDRESS --chain eth --limit 50 --out txs.csv
Chains: eth (mainnet), sepolia, polygon, bsc, arbitrum, optimism
"""
import os, sys, csv, argparse, requests
from dotenv import load_dotenv

load_dotenv()
ETHERSCAN_KEY = os.getenv("ETHERSCAN_API_KEY")
if not ETHERSCAN_KEY:
    print("Error: ETHERSCAN_API_KEY missing in .env"); sys.exit(1)

ETHERSCAN_BASE = {
    "eth": "https://api.etherscan.io/api",
    "sepolia": "https://api-sepolia.etherscan.io/api",
    "polygon": "https://api.polygonscan.com/api",
    "bsc": "https://api.bscscan.com/api",
    "arbitrum": "https://api.arbiscan.io/api",
    "optimism": "https://api-optimistic.etherscan.io/api",
}

def fetch_txs(address, chain="eth", limit=50):
    base = ETHERSCAN_BASE.get(chain)
    if not base:
        raise ValueError(f"Unsupported chain: {chain}")
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": limit,
        "sort": "desc",
        "apikey": ETHERSCAN_KEY
    }
    r = requests.get(base, params=params, timeout=20)
    r.raise_for_status()
    j = r.json()
    if j.get("status") != "1":
        return j.get("result", [])
    return j["result"]

def txs_to_csv(items, out_file="transactions.csv"):
    if not items:
        print("No transactions found."); return
    fields = ["hash","timeStamp","from","to","value","gas","gasPrice","isError","txreceipt_status"]
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for it in items:
            w.writerow({k: it.get(k, "") for k in fields})
    print(f"Saved {len(items)} tx rows to {out_file}")

def main():
    p = argparse.ArgumentParser(description="Export address transactions to CSV via Etherscan-like APIs.")
    p.add_argument("address", help="Wallet address (0x...)")
    p.add_argument("--chain", default="eth", help="eth|sepolia|polygon|bsc|arbitrum|optimism")
    p.add_argument("--limit", type=int, default=50, help="number of txs to fetch")
    p.add_argument("--out", default="transactions.csv", help="output CSV file")
    a = p.parse_args()

    print(f"Fetching {a.limit} txs for {a.address} on {a.chain}…")
    try:
        items = fetch_txs(a.address, chain=a.chain, limit=a.limit)
    except Exception as e:
        print("Fetch error:", e); sys.exit(1)
    txs_to_csv(items, a.out)

if __name__ == "__main__":
    main()
