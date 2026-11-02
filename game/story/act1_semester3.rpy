## Act I: Semester 3 — Pertemuan & Papan Kartu Uno

label act1_semester3:
    call screen act_title("Act I — Semester 3", "Pertemuan & Papan Kartu Uno")

    scene bg kelas with fade
    narator "Semester 3. Kelas kami bertambah wajah baru — sisa dari kelas yang dibubarkan."
    batin "Satu nama yang entah kenapa langsung nempel di kepala..."

    show heroine netral at right with dissolve
    h "Ini kelas B kan? Oke, sip."
    hide heroine with dissolve

    # --- Ajakan nongkrong ---
    scene bg tongkrongan with fade
    c1 "[player_name]! Sini, kurang satu orang buat Uno."
    c2 "Yang anak pindahan juga ikut, nih."

    batin "Ikut duduk berarti duduk dekat dia. Menolak berarti aman... tapi kosong lagi."

    menu:
        "Ikut gabung main Uno.":
            $ change_stat("curiosity", 5)
            p "Gas. Siapin kartunya."
        "Ragu, bilang mau ngerjain tugas dulu.":
            $ hesitation += 1
            p "Eh... aku nyusul deh."
            c1 "Halah, tugas mulu. Duduk!"
            narator "Dimas menarik kursi. Tidak ada pilihan lain."

    show heroine netral at right with dissolve
    h "Kamu jago Uno? Aku nggak suka kalah, loh."

    # --- Mini-game Uno (PRD 4.B) ---
    call uno_minigame
    $ flag_uno_played = True

    show heroine senyum at right
    h "Lumayan juga kamu. Lain kali aku balas."
    batin "Tatapannya barusan... dia juga memperhatikanku?"

    $ set_status("Casual Acquaintance")
    return
