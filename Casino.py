import random
import time

# Farben (ANSI-Farbcodes)
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Emoji-Auswahl
emojis = ["🍒", "🍋", "🍉", "🍇", "⭐", "💎", "🍀"]

def slot_machine(coins):
    einsatz = 10
    if coins < einsatz:
        print(RED + "❌ Du hast nicht genug Coins zum Spielen!" + RESET)
        return coins

    print(CYAN + "\n🎰 Willkommen beim Emoji-Slot! 🎰" + RESET)
    print(f"{YELLOW}Aktueller Kontostand: {coins} Coins{RESET}")

    coins -= einsatz
    print(f"\n💸 Einsatz: {einsatz} Coins")

    # Dreh-Animation
    for i in range(3):
        print("🎲 Rollen drehen...")
        time.sleep(0.6)

    rollen = [random.choice(emojis) for _ in range(3)]
    print(" | ".join(rollen))

    # Gewinn oder Verlust
    if rollen[0] == rollen[1] == rollen[2]:
        gewinn = einsatz * 10
        coins += gewinn
        print(GREEN + f"💥 JACKPOT!!! Du gewinnst {gewinn} Coins! 💥" + RESET)
    else:
        print(RED + "😢 Leider kein Jackpot, versuch’s nochmal!" + RESET)

    print(f"{YELLOW}💰 Neuer Kontostand: {coins} Coins{RESET}")
    return coins


# Startkapital
coins = 100
max_runden = 10  # maximal 10 Runden pro Durchlauf

for runde in range(max_runden):
    print(CYAN + f"\n--- Runde {runde + 1} von {max_runden} ---" + RESET)
    coins = slot_machine(coins)

    if coins < 10:
        print(RED + "\n💀 Du hast keine Coins mehr! Spiel vorbei." + RESET)
        break

    if runde < max_runden - 1:  # nur warten, wenn noch Runden übrig sind
        print(CYAN + "\n⏳ Nächste Runde startet in 5 Sekunden..." + RESET)
        time.sleep(5)

print(GREEN + f"\n👋 Spiel beendet! Du gehst mit {coins} Coins nach Hause!" + RESET)