## characters.rpy — Definisi karakter & gambar placeholder
## Ganti Placeholder/Solid dengan aset asli di folder images/ saat sudah tersedia.

# Nama default (bisa diubah pemain di awal game)
default player_name = "Raka"
default heroine_name = "Nayla"   # TODO: nama final heroine

# --- Karakter ---
define p = Character("[player_name]", color="#7fb3ff")            # Protagonis (Pisces)
define h = Character("[heroine_name]", color="#ffb37f")           # Heroine (Gemini)
define batin = Character(None, what_italic=True, what_color="#a8d8d0",
                         what_prefix="(", what_suffix=")")        # Inner Monologue
define c1 = Character("Dimas", color="#c0e08a")                   # Circle tongkrongan
define c2 = Character("Sari", color="#e0a0d0")                    # Circle tongkrongan
define dosen = Character("Pak Hendra", color="#cccccc")           # Dosen pengampu KP
define narator = Character(None, what_color="#dddddd")

# --- Background (placeholder warna) ---
image bg kelas = Solid("#3d4a5c")
image bg koridor = Solid("#4f4a5c")
image bg tongkrongan = Solid("#5c4a3d")
image bg kafe_malam = Solid("#2a2f45")
image bg wisuda = Solid("#6a6a4a")

# --- Sprite heroine (ekspresi sesuai PRD) ---
image heroine netral   = Placeholder("girl", text="heroine netral")
image heroine apaloh   = Placeholder("girl", text="heroine cuek 'apa loh'")
image heroine kaget    = Placeholder("girl", text="heroine kaget")
image heroine senyum   = Placeholder("girl", text="heroine senyum hangat")
image heroine sedih    = Placeholder("girl", text="heroine sedih")
