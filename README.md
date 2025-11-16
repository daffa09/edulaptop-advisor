<!-- portfolio -->
<!-- slug: edulaptop-advisor -->
<!-- title: EduLaptop Advisor -->
<!-- description: Aplikasi expert system sederhana berbasis forward chaining untuk rekomendasi laptop mahasiswa. -->
<!-- image: https://github.com/user-attachments/assets/03091a47-7189-41e9-b543-7c3f9e1a5ab3 -->
<!-- tags: python, flask, react, expert-system, forward-chaining, ai, campus-project -->

# 🎓 EduLaptop Advisor

<img width="865" height="708" alt="image" src="https://github.com/user-attachments/assets/03091a47-7189-41e9-b543-7c3f9e1a5ab3" />

Aplikasi sederhana berbasis **Forward Chaining** yang merekomendasikan laptop terbaik untuk mahasiswa berdasarkan **jurusan**, **aktivitas utama**, dan **budget**.  
Dibuat menggunakan **React (Frontend)** dan **Flask (Backend)**.

---

## 👨‍💻 Identitas Pembuat

| Nama | NPM | Mata Kuliah |
|------|------|--------------|
| Daffa Fathan | 4522210082 | Intelligent System |

---

## 🧠 Deskripsi Singkat

**EduLaptop Advisor** merupakan sistem pakar sederhana yang menggunakan metode *forward chaining* untuk menentukan rekomendasi laptop yang sesuai kebutuhan pengguna.  
Pengguna hanya perlu memilih:
1. **Jurusan** (misal: Informatika, DKV, Bisnis, dsb)
2. **Aktivitas utama** (misal: Coding, Desain, Office)
3. **Budget (Rp)**  

Lalu sistem akan menampilkan rekomendasi laptop beserta **aturan-aturan (rules)** yang digunakan dalam proses inferensi.

---

## ⚙️ Teknologi yang Digunakan

### Backend
- Python 3.x  
- Flask  
- Flask-CORS  

### Frontend
- React + Vite  
- Tailwind CSS  

---

## 🚀 Cara Menjalankan Project

### 1. Jalankan Backend (Flask)
```php
cd backend
pip install flask flask-cors
python app.py
```
Secara default, backend akan berjalan di:
```php
http://localhost:5000
```

### 2. Jalankan Frontend (React)
```php
cd frontend
npm install
npm run dev
```
Frontend akan berjalan di:
```php
http://localhost:5173
```
## 🧩 Struktur Project
```php
EduLaptop-Advisor/
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── ...
│   └── package.json
│
└── README.md
```

## 🧠 Contoh Aturan (Forward Chaining Rules)
| Kondisi                                              | Aturan yang Digunakan            | Rekomendasi                       |
| ---------------------------------------------------- | -------------------------------- | --------------------------------- |
| Jurusan Informatika + Aktivitas Coding + Budget 12jt | Butuh CPU kuat & RAM besar       | ASUS ZenBook 14 / Acer Swift X    |
| Jurusan DKV + Aktivitas Desain + Budget 9jt          | Butuh GPU Dedicated & Layar IPS  | ASUS Vivobook 15 / IdeaPad Slim 3 |
| Jurusan Bisnis + Aktivitas Office + Budget 6jt       | Butuh laptop ringan & hemat daya | Acer Swift 1 / Lenovo IdeaPad 1   |

## 🧾 API Endpoint

## POST /recommend

### Request Body:
```php
{
  "jurusan": "informatika",
  "aktivitas": "coding",
  "budget": 12000000
}
```

### Response:
```php
{
  "input_fakta_awal": ["jurusan_informatika", "aktivitas_coding", "budget_mid"],
  "fakta_akhir": [
    "jurusan_informatika",
    "aktivitas_coding",
    "butuh_cpu_i5",
    "butuh_ram_8gb",
    "butuh_ram_16gb",
    "kategori_mid_range",
    "rekomendasi_vivobook_lenovo_ideapad"
  ],
  "log_inferensi": [
    "Rule diterapkan: {'jurusan_informatika'} → butuh_cpu_i5",
    "Rule diterapkan: {'jurusan_informatika'} → butuh_ram_8gb",
    "Rule diterapkan: {'aktivitas_coding'} → butuh_cpu_i5",
    "Rule diterapkan: {'aktivitas_coding'} → butuh_ram_16gb",
    "Rule diterapkan: {'budget_mid'} → kategori_mid_range",
    "Rule diterapkan: {'kategori_mid_range'} → rekomendasi_vivobook_lenovo_ideapad"
  ],
  "rekomendasi": "ASUS Vivobook 15 / Lenovo IdeaPad Slim 3 / HP 14"
}
```

## POST /feedback

### Request Body
```php
{
  "jurusan": "informatika",
  "aktivitas": "coding",
  "budget": 9000000,
  "rekomendasi": "ASUS Vivobook 15 / Lenovo IdeaPad Slim 3 / HP 14",
  "feedback": "sesuai"
}
```

## Response
```php
{
  "status": "success",
  "message": "Feedback diterima dan disimpan ke learning_data.json"
}
```


### Catatan:
1. Nilai feedback dapat berupa "sesuai" atau "tidak_sesuai".
2. Sistem akan memantau kombinasi yang sering mendapat feedback positif.
3. Jika pola tertentu muncul berulang kali, sistem otomatis menambah aturan baru agar inferensi berikutnya lebih relevan.


### 🧬 Mekanisme Learning Agent
1. Sistem menyimpan setiap kombinasi fakta + hasil rekomendasi + feedback pengguna.
2. Jika pola tertentu (misal: “jurusan desain + aktivitas editing + budget tinggi”) sering mendapat feedback positif, maka:
```php
IF jurusan_desain AND aktivitas_editing AND budget_high → rekomendasi_macbook_air_m2
```
akan otomatis ditambahkan ke basis pengetahuan.

3. Dengan ini, sistem belajar secara adaptif, sehingga rekomendasi berikutnya semakin sesuai dengan preferensi pengguna.
