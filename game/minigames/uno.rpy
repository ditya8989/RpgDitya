## uno.rpy — Mini-game Tabletop Uno Event (PRD 4.B)
## Versi kerangka: pemain memilih kartu dari tangan tiap ronde; tipe kartu memicu dialog.
##   Wild / Draw 4  -> banter usil / tantangan tatap mata
##   Skip / Reverse -> topik beralih ke arah personal
##   Angka          -> obrolan ringan
## TODO: aturan Uno penuh (warna/angka harus cocok) & UI kartu visual di images/ui/cards/

init python:
    import random

    UNO_COLORS = ["Merah", "Kuning", "Hijau", "Biru"]
    UNO_ACTIONS = ["Skip", "Reverse"]
    UNO_WILDS = ["Wild", "Draw 4"]

    def uno_build_deck():
        deck = []
        for c in UNO_COLORS:
            deck += ["{} {}".format(c, n) for n in range(10)]
            deck += ["{} {}".format(c, a) for a in UNO_ACTIONS]
        deck += UNO_WILDS * 4
        random.shuffle(deck)
        return deck

    def uno_card_type(card):
        if card in UNO_WILDS:
            return "wild"
        if card.split(" ", 1)[1] in UNO_ACTIONS:
            return "action"
        return "number"

default uno_rounds = 3

label uno_minigame:
    $ uno_deck = uno_build_deck()
    $ uno_hand = [uno_deck.pop() for _ in range(5)]
    narator "Kartu dibagikan. [heroine_name] duduk tepat di seberangmu."

    $ r = 0
    while r < uno_rounds:
        $ card = renpy.display_menu([(c, c) for c in uno_hand])
        $ uno_hand.remove(card)
        $ uno_hand.append(uno_deck.pop())
        $ ctype = uno_card_type(card)

        if ctype == "wild":
            call uno_event_wild(card)
        elif ctype == "action":
            call uno_event_action(card)
        else:
            call uno_event_number(card)
        $ r += 1

    narator "Permainan selesai. Tawa masih tersisa di meja."
    return

label uno_event_wild(card):
    p "[card]! Rasain."
    show heroine kaget at right
    h "Ih! Kamu sengaja ya?"
    menu:
        "Tatap matanya sambil nyengir.":
            $ change_stat("affection", 5)
            show heroine apaloh
            h "...Apa?"
            batin "Dia buang muka duluan. Aku menang dua kali."
        "Pura-pura polos.":
            $ change_stat("trust", 3)
            h "Dasar."
    return

label uno_event_action(card):
    p "[card]."
    h "Hmm. Eh, kamu dari dulu emang di kelas ini?"
    menu:
        "Cerita sedikit tentang diri sendiri.":
            $ change_stat("trust", 5)
            h "Oh gitu. Aku kira kamu tipe pendiam."
        "Balik tanya tentang kelas lamanya.":
            $ change_stat("trust", 3)
            $ change_stat("affection", 2)
            h "Bubar. Ya udah, sekarang di sini aja."
    return

label uno_event_number(card):
    p "[card]."
    c1 "Main aman mulu, [player_name]."
    $ change_stat("curiosity", 2, notify_player=False)
    return
