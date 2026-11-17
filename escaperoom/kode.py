import os
import random

# --- INDSTILLINGER ---
KODEORD = "SYSTEM"
BREDDE = 40  # Antal søjler (skal være større end længden på kodeordet)
HOJDE = 22  # Antal rækker

# Farvekoder til terminalen (Grøn tekst på sort baggrund)
GRON = "\033[32m"
LYS_GRON = "\033[92m"
NULSTIL = "\033[0m"


def generer_matrix():
  # Ryd terminalen (virker på både Windows, Mac og Linux)
  os.system("cls" if os.name == "nt" else "clear")

  # 1. Vælg tilfældige, unikke søjler til hvert bogstav, og sorter dem fra venstre mod højre
  valgte_sojler = sorted(random.sample(range(BREDDE), len(KODEORD)))

  # 2. Vælg en tilfældig række (højde) for hvert bogstav (undgå helt øverst og nederst)
  valgte_raekker = [random.randint(2, HOJDE - 3) for _ in KODEORD]

  # Opret et opslag for de skjulte bogstaver: (række, søjle) -> bogstav
  skjulte_bogstaver = {}
  for i, bogstav in enumerate(KODEORD):
    skjulte_bogstaver[(valgte_raekker[i], valgte_sojler[i])] = bogstav

  # 3. Tegn selve Matrix-gitteret
  print("\n")
  for r in range(HOJDE):
    linje = "  "  # Lidt margen i venstre side
    for s in range(BREDDE):
      if (r, s) in skjulte_bogstaver:
        # Indsæt det skjulte bogstav i præcis samme grønne nuance
        linje += f"{GRON}{skjulte_bogstaver[(r, s)]} "
      else:
        # Indsæt et tilfældigt 0 eller 1
        tal = random.choice(["0", "1"])
        linje += f"{GRON}{tal} "
    print(linje + NULSTIL)
  print("\n")


if __name__ == "__main__":
  generer_matrix()