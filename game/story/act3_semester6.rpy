## Act III: Semester 6 — Mandat Ketua Kelas & Konflik KP
## Mekanik: Sistem Keputusan Arbitrase (PRD 4.C)

label act3_semester6:
    call screen act_title("Act III — Semester 6", "Mandat Ketua Kelas & Konflik KP")

    scene bg kelas with fade
    dosen "Mulai semester ini, ketua kelas kalian [player_name]. Urusan pembagian topik KP, koordinasikan lewat dia."
    batin "Ketua kelas. Tanggung jawab yang nggak pernah kuminta."

    narator "Dua kelompok berebut topik KP yang sama. Salah satunya kelompok [heroine_name]."
    c1 "Kelompok kami duluan daftar, [player_name]. Jangan pilih kasih, ya."

    # --- Heroine datang langsung (dialog kunci PRD) ---
    show heroine netral at right with dissolve
    h "Gimana nih ketua, tolong dong apapun penilaian kamu aku anggap sebagai adil!"
    batin "Setelah dua semester asing, dia datang padaku. Dan dia bilang... akan menerima apapun keputusanku."

    # --- Decision Point ---
    menu:
        batin "Netralitas ketua kelas, atau keberpihakan hati?"

        "Menangkan kelompok [heroine_name].":
            $ kp_decision = "her_side"
            $ change_stat("trust", 20)
            $ change_stat("affection", 15)
            $ change_stat("class_rep", -15)
            show heroine senyum
            h "Serius? Makasih, ketua!"
            c1 "...Oke. Aku catat, ya."

        "Putuskan dengan undian terbuka di depan kelas.":
            $ kp_decision = "neutral"
            $ change_stat("trust", 12)
            $ change_stat("affection", 5)
            $ change_stat("class_rep", 15)
            narator "Undian jatuh ke kelompok Dimas."
            show heroine netral
            h "Yah. Tapi adil sih. Aku kan udah janji terima."
            h "Kamu ternyata bisa diandalkan, ya."

        "Menangkan kelompok lain (yang mendaftar duluan).":
            $ kp_decision = "other_side"
            $ change_stat("trust", 5)
            $ change_stat("class_rep", 10)
            $ hesitation += 1
            show heroine sedih
            h "...Oke. Aku bilang aku terima, kan."

    hide heroine with dissolve

    if trust >= 15:
        batin "Dinding yang berdiri sejak semester 4 — rasanya mulai retak."
        $ set_status("Trusted Ally")

    return
