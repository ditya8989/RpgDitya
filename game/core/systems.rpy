## systems.rpy — Fungsi inti: perubahan stat, status relasi, penentu ending

init python:

    STAT_MIN, STAT_MAX = 0, 100

    # Ambang True Route. Maks teoretis saat ini: Affection ~54, Trust ~53.
    TRUE_AFFECTION_MIN = 35
    TRUE_TRUST_MIN = 35

    def _clamp(v):
        return max(STAT_MIN, min(STAT_MAX, v))

    def change_stat(name, amount, notify_player=True):
        """Ubah meter relasi dan tampilkan notifikasi kecil."""
        old = getattr(store, name)
        setattr(store, name, _clamp(old + amount))
        if notify_player and amount != 0:
            sign = "+" if amount > 0 else ""
            renpy.notify("{} {}{}".format(name.replace("_", " ").title(), sign, amount))

    def impulsive_choice(trust_penalty=5):
        """PRD 4.A: opsi terlalu impulsif menurunkan rasa nyaman heroine."""
        store.impulsive_count += 1
        change_stat("trust", -trust_penalty)

    def set_status(new_status):
        store.relation_status = new_status
        renpy.notify("Status relasi: " + new_status)

    def resolve_ending():
        """Tentukan rute akhir berdasarkan state (PRD bagian 5)."""
        if final_choice == "confess" and affection >= TRUE_AFFECTION_MIN and trust >= TRUE_TRUST_MIN:
            return "ending_true"
        if final_choice == "confess":
            # Berani tapi fondasi belum cukup -> tetap hangat, belum jadi komitmen
            return "ending_bittersweet"
        if final_choice == "hold":
            return "ending_bittersweet"
        # "delay" atau keraguan menumpuk
        return "ending_regret"
