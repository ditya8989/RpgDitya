## screens_custom.rpy — UI tambahan (HUD relasi, kartu judul semester)

# HUD meter relasi di pojok kanan atas. Aktifkan: show screen relation_hud
screen relation_hud():
    zorder 50
    frame:
        xalign 0.98 yalign 0.02
        padding (12, 8)
        vbox:
            spacing 4
            text "[relation_status]" size 18 bold True
            hbox:
                text "Affection " size 14 min_width 90
                bar value affection range 100 xsize 140 ysize 12
            hbox:
                text "Trust " size 14 min_width 90
                bar value trust range 100 xsize 140 ysize 12
            hbox:
                text "Curiosity " size 14 min_width 90
                bar value curiosity range 100 xsize 140 ysize 12

# Kartu judul pembuka setiap babak
screen act_title(act, subtitle):
    zorder 100
    add Solid("#000000cc")
    vbox:
        align (0.5, 0.5)
        spacing 10
        text act size 48 xalign 0.5
        text subtitle size 24 xalign 0.5 italic True
    timer 2.5 action Return()
