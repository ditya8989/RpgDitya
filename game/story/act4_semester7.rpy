## Act IV: Semester 7 — Dinamika Zodiak & Fase "Warm Friends"
## Mekanik: Chemistry & Tone Matching -> penentuan Climax Route

init python:
    # Setiap topik: (kalimat heroine, nada yang cocok)
    # Nada: "playful" | "deep" | "supportive"
    TONE_TOPICS = [
        ("Kata orang Gemini itu punya dua kepribadian. Menurutmu aku yang mana?", "playful"),
        ("Kadang aku ngerasa rame di luar, tapi sepi di dalam. Kamu pernah gitu?", "deep"),
        ("Aku takut abis lulus semua orang jalan sendiri-sendiri.", "supportive"),
    ]
    TONE_OPTIONS = [
        ("Bercanda balik dengan santai", "playful"),
        ("Jujur menceritakan isi hati", "deep"),
        ("Menenangkan dan meyakinkan", "supportive"),
    ]

label act4_semester7:
    call screen act_title("Act IV — Semester 7", "Dinamika Zodiak & Fase \"Warm Friends\"")

    scene bg kafe_malam with fade
    $ set_status("Warm Friend")
    narator "Tingkat akhir. Obrolan kami pindah dari koridor ke chat larut malam, lalu ke kafe ini."
    show heroine senyum at center with dissolve
    h "Eh, kamu Pisces kan? Katanya Gemini sama Pisces itu... ribet."
    p "Ribet gimana?"
    h "Ya kayak kita. Hehe."

    # --- Chemistry & Tone Matching ---
    $ t = 0
    while t < len(TONE_TOPICS):
        $ line, expected = TONE_TOPICS[t]
        h "[line]"
        $ picked = renpy.display_menu([(label, tone) for label, tone in TONE_OPTIONS])
        if picked == expected:
            $ tone_match_score += 1
            $ change_stat("affection", 8)
            $ change_stat("trust", 5)
            show heroine senyum
            h "...Iya. Kamu ngerti banget."
        else:
            $ change_stat("affection", 2)
            show heroine netral
            h "Hmm, gitu ya."
        $ t += 1

    # --- Persimpangan: Climax Route ---
    narator "Lagu di kafe berganti. Lagu yang pernah dia kirim jam dua pagi."
    batin "Sekarang, atau tidak sama sekali? Atau... nanti saja?"

    menu:
        batin "Apa yang akan kulakukan?"
        "Nyatakan perasaan dengan jujur.":
            $ final_choice = "confess"
        "Simpan perasaan, jaga persahabatan ini.":
            $ final_choice = "hold"
        "Nanti saja... setelah skripsi.":
            $ final_choice = "delay"
            $ hesitation += 2

    # Keraguan yang menumpuk sepanjang game bisa mengunci momen
    if final_choice != "confess" and hesitation >= 5:
        $ final_choice = "delay"

    hide heroine with dissolve
    return
