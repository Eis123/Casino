import random
import time

# Liste mit möglichen Emojis
emojis = ["🍒", "🍋", "🍉", "🍇", "⭐", "💎", "🍀"]

def slot_machine(coins):
    einsatz = 10
    if coins < einsatz:
        print("❌ Du hast nicht genug Coins zum Spielen!")
        return coins

    print("\n🎰 Willkommen beim Emoji-Slot! 🎰")
    print(f"Aktueller Kontostand: {coins} Coins")
    input("Drücke ENTER um zu spielen...")

    coins -= einsatz
    print(f"\n💸 Einsatz: {einsatz} Coins")

    # Kleine Dreh-Animation
    for i in range(3):
        print("🎲 Rollen drehen...")
        time.sleep(0.7)

    rollen = [random.choice(emojis) for _ in range(3)]
    print(" | ".join(rollen))

    # Gewinn prüfen
    if rollen[0] == rollen[1] == rollen[2]:
        gewinn = einsatz * 10
        coins += gewinn
        print(f"💥 JACKPOT!!! Du gewinnst {gewinn} Coins! 💥")
    else:
        print("😢 Leider kein Jackpot, versuch’s nochmal!")

    print(f"💰 Neuer Kontostand: {coins} Coins")
    return coins


# Startkapital
coins = 100

while True:
    coins = slot_machine(coins)
    if coins < 10:
        print("\n💀 Du hast keine Coins mehr! Spiel vorbei.")
        break

    nochmal = input("\nNochmal spielen? (j/n): ").lower()
    if nochmal != "j":
        print(f"\n👋 Danke fürs Spielen! Du gehst mit {coins} Coins nach Hause!")
        break
