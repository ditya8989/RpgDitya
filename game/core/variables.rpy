## variables.rpy — State game (Linear-Branching State Machine)
## Semua nilai disimpan dengan `default` agar ikut tersimpan di save file.

# --- Meter relasi (PRD 4.A) ---
default affection = 0        # kedekatan emosional romantis
default trust = 0            # comfort / trust: rasa aman & keterbukaan heroine
default curiosity = 0        # obsession/curiosity protagonis (Act II)
default class_rep = 50       # reputasi protagonis di mata kelas (Act III)

# --- Penghitung perilaku ---
default hesitation = 0       # akumulasi keraguan -> memicu Regret Route
default impulsive_count = 0  # pilihan impulsif -> menurunkan comfort

# --- Status relasi ---
default relation_status = "Stranger"
# Stranger -> Casual Acquaintance -> Distant Glances -> Trusted Ally -> Warm Friend -> Lover

# --- Flag event per babak ---
default flag_uno_played = False
default flag_apa_loh_seen = False
default kp_decision = None          # "her_side" | "neutral" | "other_side"
default tone_match_score = 0        # Act IV: Chemistry & Tone Matching
default final_choice = None         # "confess" | "hold" | "delay"
