
# **Bot Telegram Anti Mute dan Peringatan Username**

Bot ini dirancang untuk memantau anggota grup Telegram yang tidak memiliki username, memberikan peringatan hingga tiga kali, dan mengeluarkan mereka jika tidak memenuhi aturan. Selain itu, bot memiliki fitur untuk membisukan dan membuka mute semua anggota grup.

---

## **Fitur**
- **Peringatan Username:**
  - Bot memantau anggota tanpa username.
  - Memberikan hingga tiga peringatan sebelum mengeluarkan anggota dari grup.
- **Mute/Unmute Semua Anggota:**
  - Admin grup dapat membisukan semua anggota grup.
  - Admin grup juga dapat membuka mute untuk semua anggota grup.
- **Informasi dan Bantuan:**
  - Perintah `/start` dan `/help` memberikan informasi dan daftar perintah bot.

---

## **Persyaratan**
### **Instalasi Lokal**
- Python 3.9 atau lebih baru.
- Modul Python berikut:
  - `python-telegram-bot`
  - `python-dotenv`

### **Instalasi Docker**
- Docker dan Docker Compose telah diinstal.

---

## **Instalasi**

### **1. Clone Repository**
Clone atau salin script ini ke direktori lokal:
```bash
git clone https://github.com/edikurexe/satpam-bot-telegram.git \satpam-bot
cd satpam-bot
```

---

### **2. Instalasi Lokal**

#### **a. Instalasi Dependencies**
Instal semua dependencies yang diperlukan:
```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum dibuat, tambahkan dependencies berikut ke file tersebut:
```
python-telegram-bot==20.3
python-dotenv
```

#### **b. Konfigurasi Token**
1. Buat file `token.env` di direktori utama proyek:
   ```bash
   touch token.env
   ```
2. Tambahkan token bot Anda ke file `token.env`:
   ```
   TOKEN=YOUR_BOT_TOKEN
   ```
   Ganti `YOUR_BOT_TOKEN` dengan token yang didapatkan dari BotFather.

#### **c. Menjalankan Bot**
Jalankan bot dengan perintah berikut:
```bash
python bot.py
```

#### **d. Hentikan Bot**
Gunakan kombinasi `CTRL + C` untuk menghentikan bot.

---

### **3. Instalasi Menggunakan Docker**

#### **a. Persiapan File**
Pastikan file `Dockerfile` dan `docker-compose.yml` ada di direktori proyek. Berikut adalah contohnya:

**Dockerfile**
```Dockerfile
# Gunakan Python sebagai base image
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Instal semua dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin file script bot
COPY bot.py .

# Salin file environment token.env
COPY token.env .

# Jalankan bot
CMD ["sh", "-c", "TOKEN=$(grep TOKEN token.env | cut -d '=' -f 2) python3 bot.py"]
```

**docker-compose.yml**
```yaml
version: "3.8"
services:
  bot:
    build: .
    container_name: telegram_bot
    env_file:
      - token.env
    restart: unless-stopped
```

#### **b. Konfigurasi Token**
Tambahkan token bot ke file `token.env` seperti berikut:
```
TOKEN=YOUR_BOT_TOKEN
```

#### **c. Build dan Jalankan Bot**
Jalankan perintah berikut:
```bash
docker-compose up --build -d
```

#### **d. Hentikan Bot**
Gunakan perintah berikut untuk menghentikan bot:
```bash
docker-compose down
```

---

## **Daftar Perintah**
| Perintah         | Deskripsi                                           |
|-------------------|----------------------------------------------------|
| `/start`          | Menampilkan informasi tentang bot.                 |
| `/help`           | Menampilkan daftar perintah bot.                   |
| `/check_members`  | Memberikan informasi tentang fitur monitoring bot. |

---

## **Catatan**
- **Lokal:** Pastikan Python diinstal dan lingkungan virtual (optional) digunakan untuk menghindari konflik dependencies.
- **Docker:** Pastikan Docker berjalan di mesin Anda, dan gunakan `docker-compose` untuk pengelolaan yang lebih mudah.
- Pastikan bot memiliki izin admin di grup agar dapat memantau anggota atau mengatur izin mereka.

---

Jika ada pertanyaan atau masalah, jangan ragu untuk menghubungi pengembang bot melalui [Telegram](https://t.me/edikurbot).
