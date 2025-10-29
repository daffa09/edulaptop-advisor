import { useState } from "react";
import "./App.css";

export default function App() {
  const [form, setForm] = useState({ jurusan: "", aktivitas: "", budget: "" });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const res = await fetch("http://localhost:5000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...form, budget: Number(form.budget) }),
    });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  // === Sesuai rule di app.py ===
  const jurusanOptions = [
    "Informatika",
    "Teknik Informatika",
    "Ilmu Komputer",
    "Desain",
    "DKV",
    "Arsitektur",
    "Bisnis",
    "Ekonomi",
    "Manajemen",
    "Hukum",
    "Sastra",
    "Psikologi",
  ];

  const aktivitasOptions = [
    "Coding",
    "Desain",
    "Gaming",
    "Office / Mengetik",
  ];

  const budgetOptions = [
    { label: "≤ 7 juta", value: 7000000 },
    { label: "7–10 juta", value: 10000000 },
    { label: "10–15 juta", value: 15000000 },
    { label: "≥ 15 juta", value: 20000000 },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-950 to-black flex items-center justify-center p-6 text-gray-200">
      <div className="bg-gradient-to-b from-gray-800/90 to-gray-900/90 shadow-2xl rounded-2xl p-8 w-full max-w-xl border border-gray-700 backdrop-blur-sm">
        <h1 className="text-3xl font-bold text-center text-blue-400 mb-6 tracking-wide">
          🎓 EduLaptop Advisor
        </h1>

        <form onSubmit={handleSubmit} className="space-y-5">
          {/* Jurusan */}
          <div>
            <label className="block text-sm font-semibold text-gray-300 mb-1">
              Jurusan
            </label>
            <select
              name="jurusan"
              onChange={handleChange}
              value={form.jurusan}
              className="bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring focus:ring-blue-800 rounded-lg w-full p-2.5 text-gray-100 transition-all outline-none"
              required
            >
              <option value="">Pilih Jurusan</option>
              {jurusanOptions.map((j) => (
                <option key={j} value={j}>
                  {j}
                </option>
              ))}
            </select>
          </div>

          {/* Aktivitas */}
          <div>
            <label className="block text-sm font-semibold text-gray-300 mb-1">
              Aktivitas Utama
            </label>
            <select
              name="aktivitas"
              onChange={handleChange}
              value={form.aktivitas}
              className="bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring focus:ring-blue-800 rounded-lg w-full p-2.5 text-gray-100 transition-all outline-none"
              required
            >
              <option value="">Pilih Aktivitas</option>
              {aktivitasOptions.map((a) => (
                <option key={a} value={a}>
                  {a}
                </option>
              ))}
            </select>
          </div>

          {/* Budget */}
          <div>
            <label className="block text-sm font-semibold text-gray-300 mb-1">
              Budget (Rp)
            </label>
            <select
              name="budget"
              onChange={handleChange}
              value={form.budget}
              className="bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring focus:ring-blue-800 rounded-lg w-full p-2.5 text-gray-100 transition-all outline-none"
              required
            >
              <option value="">Pilih Range Budget</option>
              {budgetOptions.map((b) => (
                <option key={b.value} value={b.value}>
                  {b.label}
                </option>
              ))}
            </select>
          </div>

          <button
            disabled={loading}
            className={`w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-lg font-semibold tracking-wide transition-all transform hover:scale-[1.02] ${
              loading ? "opacity-70 cursor-not-allowed" : ""
            }`}
          >
            {loading ? "Memproses..." : "💡 Dapatkan Rekomendasi"}
          </button>
        </form>

        {result && (
          <div className="mt-6 bg-gradient-to-b from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-5 shadow-lg shadow-blue-900/30 animate-fadeIn">
            <h2 className="text-xl font-bold text-blue-400 mb-2">
              💻 Rekomendasi Laptop
            </h2>
            <p className="text-gray-200 mb-4 italic">{result.rekomendasi}</p>

            <h3 className="font-semibold text-blue-400 mb-2">
              🔍 Aturan yang Digunakan:
            </h3>
            <ul className="list-disc list-inside text-gray-300 space-y-1">
              {result.rules_terpakai.map((r, i) => (
                <li key={i}>{r}</li>
              ))}
            </ul>

            {result.spesifikasi_dianjurkan?.length > 0 && (
              <>
                <h3 className="font-semibold text-blue-400 mt-3 mb-1">
                  ⚙️ Spesifikasi yang Dianjurkan:
                </h3>
                <ul className="list-disc list-inside text-gray-300 space-y-1">
                  {result.spesifikasi_dianjurkan.map((s, i) => (
                    <li key={i}>{s}</li>
                  ))}
                </ul>
              </>
            )}
          </div>
        )}

        <p className="text-center text-xs text-gray-500 mt-6">
          © 2025 EduLaptop Advisor • Daffa Fathan
        </p>
      </div>
    </div>
  );
}
