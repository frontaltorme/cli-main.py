# Crypto Utils CLI

Bu proje, basit bir komut satırı aracı (CLI) ile Ethereum adreslerinin işlemlerini dışa aktarmak için tasarlanmıştır.  
Veriler **Etherscan API** kullanılarak çekilir.

---

## Kurulum

1. Repo’yu klonla:
   ```bash
   git clone https://github.com/kullaniciadiniz/crypto-utils.git
   cd crypto-utils
2. Sanal ortam oluştur ve bağımlılıkları yükle:
python -m venv venv
source venv/bin/activate   # Windows için: venv\Scripts\activate
pip install -r requirements.txt

3. .env dosyası oluştur ve Etherscan API anahtarını ekle:
ETHERSCAN_API_KEY=senin_keyin


## Kullanım

Ethereum adresinin son işlemlerini CSV’ye export etmek için:
  python -m cli 0xADRESIN --chain eth --limit 50 --out txs.csv
  
--0xADRESIN → İşlemleri almak istediğin adres

--chain eth → Ethereum ağı (ileride başka ağlar da eklenebilir)

--limit 50 → Kaç işlem alınacak

--out txs.csv → Sonuçların kaydedileceği dosya

Sonuç: txs.csv dosyasında işlemleri görebilirsin.

Katkı

Pull request açabilirsiniz.

API key’inizi .env dosyasına koymayı unutmayın, asla repoya yüklemeyin!

---

### Yapman Gereken
1. README.md içeriğini sil → yukarıdaki metni yapıştır.  
2. Commit butonuna basmadan önce:  
   - **Yeni branch aç → `docs/usage-readme`** seç.  
   - Commit mesajı:  
     ```
     docs: add usage instructions for Etherscan exporter
     ```  
3. Sonra **PR aç → Merge et**.  

---

👉 Bunu yaptıktan sonra senin repoda **3 farklı katkı türü** olmuş olacak:  
- `feat` (özellik ekleme)  
- `chore` (altyapı dosyaları)  
- `docs` (dokümantasyon)  

Böylece GitHub profilinde profesyonel bir proje gibi görünecek ✨  

İstiyor musun ben sana `.gitignore` dosyasını da hazır vereyim, tek seferde ekleyelim?
