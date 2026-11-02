# Echoes of Semester

RPG pixel naratif tentang ekspektasi dan realita, dari semester 3 sampai 7.
Tokoh utama: **Adgan**. Tokoh perempuan: **Maryjune**.
Naskah cerita (sumber utama): `docs/CERITA.md`.

Main langsung: **https://echoes-of-semester.vercel.app** (browser, laptop, atau HP)

© 2026 Muhammad Aditya

## Main (paling mudah)

Klik dua kali `web-prototype/index.html`. Tidak perlu instalasi, cukup browser (Chrome/Edge).
Game langsung memenuhi seluruh jendela browser; tekan **F** (atau tombol ⛶ di pojok kanan atas) untuk layar penuh sungguhan.

Kontrol: Panah/WASD jalan · Z/Spasi/Enter bicara, periksa & lanjut · M musik on/off · F layar penuh.
Di layar judul ada **PILIH BABAK** (kiri/kanan) untuk langsung lompat ke babak mana pun.
Satu kali main kira-kira 20–30 menit.

Di HP/tablet (posisi mendatar), kontrol sentuh muncul otomatis: **tombol arah** (kiri bawah) untuk jalan,
tombol **Z** (kanan bawah) untuk bicara & periksa, **ketuk layar** untuk lanjut dialog dan memilih,
**tahan layar** saat diminta tarik napas. Di layar judul, ketuk `<` `>` pada PILIH BABAK lalu ketuk tombolnya lagi untuk mulai.

## Lagu tema (opsional)

Simpan lagu milikmu sebagai `web-prototype/musik/tema.mp3`, lalu refresh.
Lagu itu diputar di layar judul dan sepanjang Epilog; tanpa file, game memakai chiptune bawaan.
Pengaturannya ada di `LAGU_TEMA` (bagian paling atas `<script>` di `index.html`), petunjuk lengkap di `web-prototype/musik/BACA-SAYA.txt`.

## Online di Vercel (bisa dimainkan siapa saja, termasuk di HP)

Isi `web-prototype/` adalah situs statis (tanpa proses build), jadi Vercel bisa langsung menyajikannya.

**Lewat terminal** (login cukup sekali; untuk memperbarui game, ulangi saja perintah terakhir):

```
cd web-prototype
npx vercel login
npx vercel deploy --prod --yes --project echoes-of-semester --create-if-missing
```

**Tanpa terminal:** seret folder `web-prototype` ke [vercel.com/drop](https://vercel.com/drop). Tiap kali drop membuat proyek baru,
jadi untuk pembaruan berikutnya pakai perintah di atas atau hubungkan proyeknya ke GitHub
(Root Directory: `web-prototype`, Framework Preset: Other).

Di HP, buka link `https://….vercel.app` lalu putar HP mendatar.
Android: tombol ⛶ membuat layar penuh. iPhone: ketuk **Bagikan → Tambahkan ke Layar Utama** lalu buka dari ikonnya,
supaya game tampil penuh tanpa bilah browser (ikon & `manifest.webmanifest` sudah disiapkan).

Catatan: semua isi `web-prototype/` ikut terbit. Kalau `musik/tema.mp3` diisi lagu milik orang lain, lagu itu ikut tersebar
ke publik; pakai lagu yang memang boleh kamu sebarkan, atau biarkan kosong (chiptune bawaan).

## Isi game

| Babak | Tempat | Yang dimainkan |
|---|---|---|
| I · Meja UNO dan Frekuensi yang Pas (Sem 3) | Kantin | Mini-game Frekuensi: balas celetukan Maryjune sebelum jeda habis. Bar ♥ mulai terisi diam-diam |
| II · Mengamati dari Garis Batas (Sem 4–5) | Kelas, lab, selasar, peta musim | Garis batas di lantai, curi pandang, draf pesan yang tak pernah terkirim, jadwal praktikum |
| III · Sengketa di Lorong Semester Enam (Sem 6) | Selasar lantai 3, ruang koordinator | Kumpulkan bukti, sidang lawan BENANG KUSUT, montase chat larut malam |
| IV · Buket Rajut Ungu dan Layar yang Terbelah (Sem 7) | Depan ruang seminar | Layar terbelah EKSPEKTASI vs REALITA |
| V · Kotak Dialog di Kamar yang Hening | Kamar malam | Pesan jujur, bar terungkap sebagai EKSPEKTASI, matikan layar, tarik napas |
| Epilog · Menutup Terminal, Membuka Musim Baru | Gerbang kampus, meja belajar | Angguk tanpa menoleh, ketik skripsi sampai kebun mekar |

Lapisan animasi: lampu hias & berkas sinar jendela, debu melayang, hujan, angin, kunang-kunang berpendar, burung,
kupu-kupu (terbang, hinggap, berbayang), ikan koi yang sesekali melompat & riak air, bayangan awan, kucing kampus,
pohon yang melentur tertiup hembusan angin, jejak kaki & debu langkah, NPC berkedip/bicara/tertawa/menoleh,
balon celetukan, bantalan cahaya & panah penanda yang naik-turun, gelembung tombol **Z** di depan benda/orang,
papan nama ruangan yang mengambang, senter Adgan di layar judul malam, sorot cahaya, efek gelombang,
dan peta kecil berbingkai kayu di lorong panjang.

Gaya animasinya mengikuti situs portofolio piksel rahmateka.my.id: kanvas memenuhi layar dengan zoom piksel bulat,
transisi **iris** (lingkaran menutup/membuka di sekitar Adgan), **tirai piksel** diagonal saat membuka/memulai,
judul yang jatuh memantul, UI kertas-tinta dengan tombol piksel yang bisa "ditekan", kabar yang meluncur dari atas,
dan bilah atas (babak, misi, bar ♥) yang melayang di atas game.

## Struktur

```
EchoesOfSemester/
├── web-prototype/
│   ├── index.html          # game lengkap dalam satu file (HTML + CSS + JS)
│   ├── manifest.webmanifest # data aplikasi untuk "Tambahkan ke Layar Utama" di HP
│   ├── ikon/               # ikon aplikasi (dibuat dari pixel art game)
│   └── musik/              # taruh tema.mp3 di sini (opsional)
├── docs/
│   ├── CERITA.md           # naskah cerita + pemetaan ke gameplay
│   └── PRDrpg.md           # PRD awal (versi romansa, sudah digantikan CERITA.md)
├── game/                   # kerangka Ren'Py lama, masih mengikuti PRD awal
└── _arsip/
    ├── web-prototype-v1.html   # prototipe pertama
    └── web-prototype-v2.html   # versi kotak kecil (sebelum layar penuh, nama lama Jumay)
```

Bagian kode di `index.html` diberi judul per bagian: DASAR, LAGU TEMA, AUDIO, PIXEL ART, TILE & PETA,
STATE & HUD, ENTITAS & KAMERA, INPUT, DIALOG/PONSEL, EFEK, RENDER, ADEGAN KHUSUS, BABAK, ALUR.
Dialog tiap babak ada di bagian BABAK, jadi mudah diubah tanpa menyentuh mesin game.

