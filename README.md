# Liar's Gambit: The Underground Game
**Terinspirasi dari Manga: USOGUI**

Sebuah visual novel interaktif yang menampilkan mekanik pilihan berganda dengan multiple endings dan branching storylines.

## 📖 Deskripsi Game

Anda adalah seorang pemain yang diundang ke turnamen underground yang misterius. Sepanjang perjalanan, Anda akan menghadapi pilihan yang sulit, musuh yang cerdas, dan momen yang menentukan nasib. Keputusan Anda akan membentuk jalan cerita dan menentukan akhir yang Anda dapatkan.

Terinspirasi dari manga *Usogui* - sebuah cerita tentang perjudian, penipuan, strategi, dan kemampuan membaca manusia.

## 🎮 Fitur Utama

### Input (Interaksi)
- Bot bertanya kepada pemain melalui pilihan berganda
- Contoh: "Dengarkan proposalnya?" / "Tolak dan pergi?" / "Coba membaca ekspresinya?"

### Logic (Logika)
- Kode Python menggunakan perintah `if` dan `else` untuk mengecek pilihan pemain
- Setiap pilihan mengarahkan ke cabang cerita yang berbeda
- Logika permainan mempertimbangkan keputusan sebelumnya

### Output (Hasil)
- Bot memberikan respons cerita yang unik berdasarkan pilihan
- Narasi berubah sesuai dengan path yang dipilih pemain
- Ending berbeda-beda tergantung keputusan kumulatif

## 🎭 Jenis-Jenis Ending

### ⭐ TRUE ENDING (Ending Sejati)
- **The Prepared Strategist** - Persiapan matang adalah kunci
- **The Respectful Opponent** - Bermain dengan hormat dan integritas
- **The Honest Victor** - Kejujuran membawa kesuksesan sejati
- **The Enlightened Champion** - Pencerahan spiritual dan mental
- **The Loyal Champion** - Loyalitas lebih bernilai dari uang
- **The Rising Apprentice** - Belajar dari kegagalan dengan rendah hati
- **The Perfect Partnership** - Kemitraan yang sempurna dibangun atas kepercayaan
- **The Ultimate Gambler** - Pemain tertinggi yang membuat organisasi sendiri

### ❌ BAD ENDING (Ending Buruk)
- **The Coward's Regret** - Menolak kesempatan emas
- **The Predictable Player** - Terlalu mudah dibaca
- **The Exposed Liar** - Tipuan selalu ketahuan pada akhirnya
- **The Caught Thief** - Mencuri informasi membawa bencana
- **The Fatal Trap** - Mengabaikan nasihat bijak membawa kehancuran
- **The Overconfident Gambler** - Kepercayaan diri yang berlebihan
- **The Violent Failure** - Kekerasan tidak pernah menjadi solusi
- **The Sore Loser** - Tidak bisa menerima kekalahan dengan hormat
- **The Betrayer's Doom** - Pengkhianatan membawa kematian karir

### 🟡 NEUTRAL ENDING (Ending Netral)
- **The Opportunity Missed** - Indikasi dalam pengambilan keputusan
- **The Puppet Master's Tool** - Kaya tetapi kehilangan kebebasan
- **The Cautious Survivor** - Bermain aman membuat Anda selamat tapi biasa
- **The Fearful Gambler** - Takut risiko = tetap tertinggal
- **The Enigma** - Misterius membawa kesuksesan modest
- **Alone Once More** - Uang tanpa teman bukan kemenangan
- **The Informed Choice** - Kemenangan yang dicuri tidak memuaskan

## 🎯 Cara Bermain

### Menjalankan Game
```bash
python main.py
```

### Gameplay
1. **Input Nama** - Mulai dengan memasukkan nama karakter Anda
2. **Baca Cerita** - Ikuti narasi yang diketik dengan efek typing
3. **Buat Pilihan** - Pilih dari opsi yang diberikan (1, 2, atau 3)
4. **Lihat Hasil** - Cerita berkembang berdasarkan pilihan Anda
5. **Capai Ending** - Permainan akan berakhir dengan salah satu dari 19+ endings

## 📚 Struktur Cerita

```
CHAPTER 1: Pengenalan
├─ Dengarkan (Jalur Antusias)
│  └─ Chapter 2: The Mysterious Game
│     ├─ Main dengan Strategi Defensif → Neutral Ending
│     ├─ Main Agresif → Chapter 4: Overwhelming Power
│     └─ Bentuk Aliansi → Chapter 4: United Front
├─ Tolak (Jalur Penolakan) → Bad Ending: The Coward's Regret
└─ Baca Ekspresi (Jalur Detektif)
   └─ Chapter 2: The Perceptive Path
      ├─ Ikuti Instruksi → Neutral Ending: The Puppet
      ├─ Tantang Kiji → Chapter 3: One-on-One Duel
      └─ Minta Bukti → TRUE ENDING: The Prepared Strategist
```

## 🎨 Fitur Visual

- **Warna Terminal** - Output berwarna untuk better readability
  - 🟦 BLUE - Chapter titles
  - 🟩 GREEN - True endings
  - 🟥 RED - Bad endings
  - 🟨 YELLOW - Neutral endings
  
- **Efek Typing** - Teks tercetak secara dinamis untuk pengalaman immersive

- **Clear Screen** - Layar dibersihkan untuk setiap chapter baru

## 💾 Teknologi

- **Python 3.x**
- **Standard Library Only** (time, os, sys)
- **Terminal Colors** - ANSI color codes
- **Cross-Platform** - Bekerja di Linux, macOS, dan Windows

## 🎲 Mekanik Permainan

### Decision-Based Branching
Setiap keputusan membawa Anda ke branch cerita yang berbeda:
```python
if pilihan == "1":
    return true_ending_prepare(nama)
elif pilihan == "2":
    return bad_ending_scaredy(nama)
elif pilihan == "3":
    return chapter_2_detective(nama)
```

### Multiple Paths to Endings
- Simple choices → Simple endings
- Complex sequences → Unique endings
- Strategic thinking → True endings
- Reckless decisions → Bad endings

## 📖 Inspirasi dari Usogui

Seperti manga Usogui yang berfokus pada:
- **Psychological Warfare** - Perang pikiran dalam pertandingan
- **Reading People** - Membaca ekspresi dan emosi lawan
- **Strategic Thinking** - Strategi kompleks melawan kecerdasan murni
- **Integrity vs Deception** - Dilema antara kejujuran dan penipuan
- **High Stakes** - Risiko tinggi dan konsekuensi besar

Game ini menghadirkan tema-tema serupa dalam format interaktif!

## 🚀 Tips Bermain

1. **Baca dengan Seksama** - Setiap kalimat mungkin memberi hint
2. **Pertimbangkan Karakter** - Kiji adalah master pembaca manusia
3. **Pelajari dari Endings** - Setiap ending memberi pelajaran moral
4. **Mainkan Berkali-kali** - Jelajahi semua path dan endings
5. **Pikirkan Strategis** - True endings reward perencanaan matang

## 📊 Statistik Game

- **Total Chapters**: 4+
- **Total Endings**: 19
  - True Endings: 8
  - Bad Endings: 9
  - Neutral Endings: 7
- **Total Branching Points**: 20+
- **Unique Story Paths**: 100+

## 🎓 Pelajaran dari Setiap Ending

Setiap ending memberikan pelajaran moral:
- **True Endings**: Kejujuran, strategi, kolab, loyalitas
- **Bad Endings**: Konsekuensi pilihan egois/impulsif
- **Neutral Endings**: Gray area antara sukses dan kegagalan

## 📝 Lisensi

Game ini dibuat untuk tujuan edukasi dan hiburan.
Terinspirasi oleh manga *Usogui* oleh Toshio Sako.

---

**Selamat bermain dan semoga Anda menemukan TRUE ENDING! 🎮✨**
