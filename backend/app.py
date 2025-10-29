from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    jurusan = data.get('jurusan', '').strip().lower()
    aktivitas = data.get('aktivitas', '').strip().lower()
    budget = data.get('budget', 0)

    rules = []
    spesifikasi = []
    rekomendasi = "Belum ditemukan"

    # === Forward chaining rules ===
    # Jurusan rules
    if jurusan in ["informatika", "teknik informatika", "ilmu komputer"]:
        rules.append("Jurusan Informatika → butuh laptop dengan CPU minimal i5 dan RAM >= 8GB")
        spesifikasi.extend(["CPU minimal i5", "RAM >= 8GB"])
    elif jurusan in ["desain", "dkv", "arsitektur"]:
        rules.append("Jurusan Desain/Arsitektur → butuh GPU dedicated dan layar IPS")
        spesifikasi.extend(["GPU dedicated", "Layar IPS"])
    elif jurusan in ["bisnis", "ekonomi", "manajemen"]:
        rules.append("Jurusan Bisnis → butuh laptop ringan dengan baterai awet")
        spesifikasi.extend(["Ringan", "Baterai awet"])
    elif jurusan in ["hukum", "sastra", "psikologi"]:
        rules.append("Jurusan non-teknik → laptop entry-level sudah cukup")
        spesifikasi.extend(["CPU i3/Ryzen 3", "RAM 8GB"])

    # Aktivitas rules
    if "desain" in aktivitas:
        rules.append("Aktivitas desain → butuh GPU dedicated")
        spesifikasi.append("GPU dedicated")
    if "coding" in aktivitas:
        rules.append("Aktivitas coding → butuh CPU kuat dan RAM besar")
        spesifikasi.append("CPU i5/i7 dan RAM >= 16GB")
    if "gaming" in aktivitas:
        rules.append("Aktivitas gaming → butuh GPU gaming (GTX/RTX series)")
        spesifikasi.append("GPU gaming")
    if "office" in aktivitas or "mengetik" in aktivitas:
        rules.append("Aktivitas office → cukup CPU i3 dan SSD")
        spesifikasi.append("SSD wajib")

    # Budget rules
    if budget <= 7000000:
        rules.append("Budget di bawah 7 juta → laptop low-end cocok")
        rekomendasi = "Acer Swift 1 / ASUS A416 / Lenovo IdeaPad 1"
    elif 7000000 < budget <= 10000000:
        rules.append("Budget 7–10 juta → mid-range laptop")
        rekomendasi = "ASUS Vivobook 15 / Lenovo IdeaPad Slim 3 / HP 14"
    elif 10000000 < budget <= 15000000:
        rules.append("Budget 10–15 juta → high performance student laptop")
        rekomendasi = "ASUS ZenBook 14 / Acer Swift X / Lenovo Yoga Slim 7"
    else:
        rules.append("Budget di atas 15 juta → premium laptop")
        rekomendasi = "MacBook Air M2 / ASUS ROG Flow / Dell XPS 13"

    return jsonify({
        "jurusan": jurusan,
        "aktivitas": aktivitas,
        "budget": budget,
        "rules_terpakai": rules,
        "spesifikasi_dianjurkan": spesifikasi,
        "rekomendasi": rekomendasi
    })

if __name__ == '__main__':
    app.run(debug=True)
