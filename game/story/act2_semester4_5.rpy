## Act II: Semester 4 & 5 — Jeda, Tatapan, dan "Apa Loh"
## Mekanik: observasi tatapan + inner monologue. Affection tertahan, Curiosity naik.

label act2_semester4_5:
    call screen act_title("Act II — Semester 4 & 5", "Jeda, Tatapan, dan \"Apa Loh\"")

    scene bg kelas with fade
    narator "Entah sejak kapan, kami jarang bicara lagi. Tidak ada pertengkaran. Hanya... jeda."
    $ set_status("Distant Glances")

    # --- Sistem observasi tatapan: beberapa momen kecil ---
    $ glance_moments = [
        "Dia tertawa dengan teman di barisan depan.",
        "Dia menopang dagu, menatap jendela saat dosen menjelaskan.",
        "Dia mengetuk-ngetuk pulpen, kelihatan bosan.",
    ]
    $ i = 0
    while i < len(glance_moments):
        narator "[glance_moments[i]]"
        menu:
            "Perhatikan diam-diam.":
                $ change_stat("curiosity", 5)
                batin "Kenapa aku nggak bisa berhenti lihat?"
            "Alihkan pandangan.":
                $ hesitation += 1
                batin "Sudahlah. Bukan urusanku."
        $ i += 1

    # --- Event inti: tertangkap basah ---
    scene bg koridor with fade
    narator "Koridor lantai dua. Aku menatap terlalu lama."
    show heroine apaloh at center with vpunch
    h "Apa loh?"
    $ flag_apa_loh_seen = True

    batin "Dua kata. Ketus. Tapi kenapa malah bikin jantung nggak karuan?"

    menu:
        batin "Jawab apa?"
        "\"Nggak, cuma kepikiran sesuatu.\" (aman)":
            $ change_stat("trust", 3)
            h "Hmm. Aneh."
        "\"Kamu beda aja hari ini.\" (impulsif)":
            $ impulsive_choice()
            $ change_stat("curiosity", 5)
            show heroine kaget
            h "...Hah? Apaan sih."
        "Senyum kecil, lalu pergi.":
            $ change_stat("curiosity", 8)
            $ hesitation += 1

    hide heroine with dissolve
    batin "\"Apa loh?\" — terngiang terus sampai semester 5 berakhir."
    $ change_stat("curiosity", 10)
    return
