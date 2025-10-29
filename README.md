# 🎓 EduLaptop Advisor

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
  "jurusan": "informatika",
  "aktivitas": "coding",
  "budget": 12000000,
  "rules_terpakai": [
    "Jurusan Informatika → butuh laptop dengan CPU minimal i5 dan RAM >= 8GB",
    "Aktivitas coding → butuh CPU kuat dan RAM besar",
    "Budget 10–15 juta → high performance student laptop"
  ],
  "spesifikasi_dianjurkan": [
    "CPU minimal i5",
    "RAM >= 8GB",
    "CPU i5/i7 dan RAM >= 16GB"
  ],
  "rekomendasi": "ASUS ZenBook 14 / Acer Swift X / Lenovo Yoga Slim 7"
}
```