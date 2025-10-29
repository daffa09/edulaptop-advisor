from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Aturan Forward Chaining ---
rules = [
    # Jurusan ke kebutuhan dasar
    ({"jurusan_informatika"}, "butuh_cpu_i5"),
    ({"jurusan_informatika"}, "butuh_ram_8gb"),
    ({"jurusan_desain"}, "butuh_gpu_dedicated"),
    ({"jurusan_desain"}, "butuh_layar_ips"),
    ({"jurusan_bisnis"}, "butuh_baterai_awet"),
    ({"jurusan_bisnis"}, "butuh_laptop_ringan"),
    ({"jurusan_non_teknik"}, "butuh_laptop_entry"),

    # Aktivitas ke kebutuhan tambahan
    ({"aktivitas_coding"}, "butuh_cpu_i5"),
    ({"aktivitas_coding"}, "butuh_ram_16gb"),
    ({"aktivitas_desain"}, "butuh_gpu_dedicated"),
    ({"aktivitas_gaming"}, "butuh_gpu_gaming"),
    ({"aktivitas_office"}, "butuh_ssd"),

    # Budget ke kategori laptop
    ({"budget_low"}, "kategori_low_end"),
    ({"budget_mid"}, "kategori_mid_range"),
    ({"budget_high"}, "kategori_high_perf"),
    ({"budget_premium"}, "kategori_premium"),

    # Kombinasi fakta ke rekomendasi
    ({"kategori_low_end"}, "rekomendasi_acer_swift_asus_a416"),
    ({"kategori_mid_range"}, "rekomendasi_vivobook_lenovo_ideapad"),
    ({"kategori_high_perf"}, "rekomendasi_zenbook_swiftx_yoga"),
    ({"kategori_premium"}, "rekomendasi_macbook_rog_xps"),
]

# --- Mesin inferensi forward chaining ---
def forward_chaining(facts, rules):
    facts = set(facts)
    applied = True
    log = []
    while applied:
        applied = False
        for premis, conclusion in rules:
            if premis.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                log.append(f"Rule diterapkan: {premis} → {conclusion}")
                applied = True
    return facts, log

# --- Endpoint utama ---
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    jurusan = data.get("jurusan", "").lower()
    aktivitas = data.get("aktivitas", "").lower()
    budget = data.get("budget", 0)

    # --- Konversi input user ke fakta awal ---
    facts = set()

    # Jurusan
    if jurusan in ["informatika", "teknik informatika", "ilmu komputer"]:
        facts.add("jurusan_informatika")
    elif jurusan in ["desain", "dkv", "arsitektur"]:
        facts.add("jurusan_desain")
    elif jurusan in ["bisnis", "ekonomi", "manajemen"]:
        facts.add("jurusan_bisnis")
    else:
        facts.add("jurusan_non_teknik")

    # Aktivitas
    if "coding" in aktivitas:
        facts.add("aktivitas_coding")
    elif "desain" in aktivitas:
        facts.add("aktivitas_desain")
    elif "gaming" in aktivitas:
        facts.add("aktivitas_gaming")
    elif "office" in aktivitas:
        facts.add("aktivitas_office")

    # Budget
    if budget <= 7000000:
        facts.add("budget_low")
    elif 7000000 < budget <= 10000000:
        facts.add("budget_mid")
    elif 10000000 < budget <= 15000000:
        facts.add("budget_high")
    else:
        facts.add("budget_premium")

    # --- Jalankan inferensi ---
    final_facts, log = forward_chaining(facts, rules)

    # --- Tentukan rekomendasi berdasarkan fakta akhir ---
    rekomendasi = "Belum ditemukan"
    if "rekomendasi_acer_swift_asus_a416" in final_facts:
        rekomendasi = "Acer Swift 1 / ASUS A416 / Lenovo IdeaPad 1"
    elif "rekomendasi_vivobook_lenovo_ideapad" in final_facts:
        rekomendasi = "ASUS Vivobook 15 / Lenovo IdeaPad Slim 3 / HP 14"
    elif "rekomendasi_zenbook_swiftx_yoga" in final_facts:
        rekomendasi = "ASUS ZenBook 14 / Acer Swift X / Lenovo Yoga Slim 7"
    elif "rekomendasi_macbook_rog_xps" in final_facts:
        rekomendasi = "MacBook Air M2 / ASUS ROG Flow / Dell XPS 13"

    return jsonify({
        "input_fakta_awal": list(facts),
        "fakta_akhir": list(final_facts),
        "log_inferensi": log,
        "rekomendasi": rekomendasi
    })


if __name__ == "__main__":
    app.run(debug=True)
