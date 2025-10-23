# 📝 Flask TODO List Starter

Proyek ini adalah template sederhana untuk workshop **Flask Web Framework** dengan studi kasus **aplikasi TODO List**.

Tujuannya adalah membantu peserta memahami dasar framework Flask, seperti:
- Membuat route (`@app.route`)
- Menggunakan template HTML
- Mengelola data dengan form
- Menyimpan data ke file JSON

---

## ⚙️ Persiapan Awal

### 1. Pastikan Python sudah terinstall
Cek dengan perintah:
```bash
python --version
```
Jika belum ada, silakan install Python dari python.org/downloads

### 2. Buat Virtual Environment
Gunakan perintah berikut di command prompt atau terminal:
### windows
```
python -m venv venv
venv\Scripts\activate
```
### mac/linux
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Depedency yang dibutuhkan
setelah virtual environtment aktif, jalankan
```
pip install -r requirements.txt
```


## 🚀 Menjalankan Aplikasi
1. Pastikan kamu berada di dalam folder proyek:
```
cd workshop_web_smk
```
2. Jalankan aplikasi
```
python3 app.py
```
atau 
```
flask run --host 0.0.0.0 --port 5000
```
3. Buka browser dan akses
```
http://localhost:5000
```
## 📁 Struktur Folder
```
flask_todo_starter/
│
├── app.py                # File utama Flask
├── todos.json            # File penyimpanan data tugas
└── templates/
    └── index.html        # Halaman utama TODO List
```
