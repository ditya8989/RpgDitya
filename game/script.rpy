## script.rpy — Entry point. Alur utama mengikuti Semester Arc (PRD bagian 3).

label start:
    scene black
    $ player_name = renpy.input("Siapa namamu?", default=player_name, length=16).strip() or "Raka"

    show screen relation_hud

    call act1_semester3
    call act2_semester4_5
    call act3_semester6
    call act4_semester7

    # Penentuan ending
    $ ending_label = resolve_ending()
    hide screen relation_hud
    call expression ending_label

    return
