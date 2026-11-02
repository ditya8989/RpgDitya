# Product Requirement Document (PRD) & Game Design Document (GDD)
**Judul Proyek (Tentatif):** Echoes of Semester (Kisah Gemini & Pisces)  
**Genre:** Narrative Life-Sim RPG / Romantic Slice-of-Life  
**Platform Target:** PC / Web (atau Ren'Py / Godot Engine)  
**Tipe Kontrol:** Mouse & Keyboard (Choice-Driven, Interactive Dialogue, Mini-games)

---

## 1. Visi & Overview Game

Sebuah game RPG naratif realistis berbasis kehidupan kampus yang mengeksplorasi batas tipis antara kenyamanan pertemanan, keraguan emosional, dan pencarian cinta sejati. Pemain mengarungi kehidupan mahasiswa dari semester 3 hingga semester 7, menghadapi dinamika relasi yang pasang surut bersama seorang mahasiswi pindahan.

### Nilai Inti Narasi:
* **Realitas Perkuliahan:** Mengangkat dinamika mahasiswa nyata (pembagian kelas, nongkrong santai, kepengurusan kelas, mata kuliah Kerja Praktik/KP).
* **Fluktuasi Emosi Realistis:** Hubungan tidak selalu bergerak maju; ada fase dekat, fase asing tanpa alasan jelas, hingga kembali merapat karena keadaan.
* **Resonansi Karakter:** Ikatan batin yang terbangun lewat celetukan santai, lagu, dan kecocokan zodiak (Gemini x Pisces).

---

## 2. Profil Karakter

### 1. Protagonis (Player Character)
* **Status:** Mahasiswa (21 Tahun), merangkap Ketua Kelas di semester 6.
* **Zodiak:** Pisces.
* **Karakteristik:** Observatif, menyimpan kekosongan batin di balik sikap ramahnya, canggung jika menyangkut perasaan pribadi, memiliki insting keadilan sekaligus dorongan melindungi orang yang disukai.
* **Motivasi:** Mencari sosok yang benar-benar bisa memahami dan mengisi kekosongan hatinya, bukan sekadar pelarian kenyamanan sesaat.

### 2. The Heroine (Teman Sekelas)
* **Status:** Mahasiswi pindahan sejak Semester 3 (akibat pembubaran kelas di semester 1–2).
* **Zodiak:** Gemini.
* **Karakteristik:** Santai, ceplas-ceplos, memiliki aura misterius antara cuek dan perhatian, kompetitif dalam hal kasual (game kartu).
* **Ciri Khas:** Spontan melontarkan celetukan seperti *"Apa loh?"* saat ditatap, namun bisa sangat mengandalkan protagonis di momen krusial perkuliahan.

### 3. Circle Tongkrongan
* Kumpulan teman sekelas yang menjadi katalis pertemuan, penyedia papan permainan (Uno), dan penengah dinamika kelas.

---

## 3. Struktur Babak Narasi (Semester Arc)

### Act I: Semester 3 – Pertemuan & Papan Kartu Uno
* **Fokus:** Peleburan kelas baru. Protagonis diajak nongkrong bareng circle.
* **Event Inti:** Sesi bermain kartu Uno bersama. Interaksi tatap muka pertama yang membuka memori bahwa mereka saling memperhatikan.
* **Output Gameplay:** Pengenalan kontrol dialog dan mini-game kartu Uno. Terbentuknya status relasi: *Casual Acquaintance*.

### Act II: Semester 4 & 5 – Jeda, Tatapan, dan "Apa Loh"
* **Fokus:** Kerenggangan tanpa alasan pasti. Interaksi langsung minim, komunikasi hanya lewat kontak mata dari kejauhan ruang kelas.
* **Event Inti:** Momen protagonis tertangkap basah sedang menatapnya di koridor/kelas. Respon spontan sang wanita: *"Apa loh?"* yang alih-alih menjauhkan, justru membuat protagonis terpikat dan terus terngiang.
* **Output Gameplay:** Sistem observasi tatapan dan dialog batin (*Inner Monologue*). Parameter *Affection* tertahan, namun *Obsession/Curiosity* meningkat.

### Act III: Semester 6 – Mandat Ketua Kelas & Konflik KP
* **Fokus:** Protagonis menjabat sebagai Ketua Kelas. Tekanan akademis penentuan mata kuliah Kerja Praktik (KP).
* **Event Inti:** Karakter wanita mendatangi protagonis secara langsung: *"Gimana nih ketua, tolong dong apapun penilaian kamu aku anggap sebagai adil!"*. Terjadi sengketa pemilihan judul/topik antar dua kelompok kelas.
* **Output Gameplay:** Cabang keputusan berbobot (*Decision Point*). Memenangkan kelompoknya meningkatkan *Trust* dan *Intimacy* drastis, sekaligus memecahkan dinding pemisah semester sebelumnya.

### Act IV: Semester 7 – Dinamika Zodiak & Fase "Warm Friends"
* **Fokus:** Tingkat akhir. Hubungan bertransformasi menjadi *warm friend*—saling bertukar cerita mendalam di luar jam kampus.
* **Event Inti:** Obrolan larut tentang zodiak (Gemini vs Pisces), selera musik, dan refleksi hidup. Protagonis berada di persimpangan jalan antara mempertahankan kenyamanan saat ini atau mengambil risiko menyatakan perasaan.
* **Output Gameplay:** Manajemen dialog *Chemistry & Tone Matching*. Penentuan rute akhir (*Climax Route*).

---

## 4. Mekanik & Sistem Game

### A. Sistem Relasi & Status
* **Affection Meter:** Mengukur kedekatan emosional romantis.
* **Comfort / Trust Meter:** Mengukur rasa aman dan keterbukaan heroine kepada protagonis.
* **Inner Monologue (Batin Pisces):** Sebelum memilih respons verbal, pemain dapat melihat pertimbangan batin protagonis. Memilih opsi yang terlalu impulsif dapat menurunkan rasa nyaman heroine.

### B. Mini-Game: Tabletop Uno Event
* Kartu yang dimainkan membawa dampak dialog:
  * *Wild / Draw 4:* Memicu lelucon, banter usil, atau tantangan tatap mata.
  * *Skip / Reverse:* Mengalihkan topik pembicaraan ke arah personal.

### C. Sistem Keputusan Arbitrase (Semester 6)
* Pemain menghadapi sengketa kelas. Menyeimbangkan antara etika netralitas ketua kelas vs keberpihakan emosional kepada heroine. Keputusan memengaruhi relasi sosial di kelas dan tingkat kepercayaan heroine.

---

## 5. Cabang Akhir (Endings)

1. **True Route: "Bagaikan Lagu Gemini & Pisces"**
   Protagonis berani melangkah keluar dari zona pertemanan di momen yang tepat, menyatakan perasaan secara jujur. Hubungan bertransisi menjadi komitmen yang mengisi kekosongan batin keduanya.
2. **Bittersweet Route: "Comfort Zone / Forever Warmth"**
   Protagonis memilih menyimpan perasaannya demi menjaga persahabatan tetap utuh tanpa risiko kehilangan interaksi hangat.
3. **Regret Route: "The Unspoken Chapter"**
   Rasa ragu yang berlarut-larut membuat momentum hilang seiring kesibukan tugas akhir dan perpisahan kelulusan.

---

## 6. Spesifikasi Teknis Awal
* **Format Penulisan Skrip:** Linear-Branching State Machine.
* **Rekomendasi Engine:** Ren'Py (Visual Novel Engine) atau Web Canvas / React Native RPG framework.
* **Aset Utama yang Diperlukan:** Background ruang kelas, meja cafe/tongkrongan, sprite ekspresi karakter (kaget, cuek "apa loh", tersenyum hangat), serta UI dialog kartu.