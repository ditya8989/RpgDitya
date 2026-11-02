## endings.rpy — Tiga cabang akhir (PRD bagian 5)

label ending_true:
    scene bg kafe_malam with fade
    show heroine kaget at center
    p "Aku suka kamu. Dari meja Uno itu. Dari \"apa loh\" itu."
    show heroine senyum
    h "...Lama banget sih kamu, Pisces."
    $ set_status("Lover")
    narator "TRUE ENDING — \"Bagaikan Lagu Gemini & Pisces\""
    return

label ending_bittersweet:
    scene bg kafe_malam with fade
    show heroine senyum at center
    batin "Mungkin begini saja sudah cukup. Hangat, tanpa risiko kehilangan."
    h "Makasih ya, udah jadi teman yang paling ngerti aku."
    narator "BITTERSWEET ENDING — \"Comfort Zone / Forever Warmth\""
    return

label ending_regret:
    scene bg wisuda with fade
    narator "Skripsi, sidang, wisuda. Chat kami makin jarang, lalu berhenti."
    batin "Ada satu bab yang tak pernah kutulis."
    narator "REGRET ENDING — \"The Unspoken Chapter\""
    return
