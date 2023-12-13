#Mäng "Kivi-paber-käärid"
#Mängijad loevad koos valjusti "kivi... käärid... paber... üks... kaks... kolm", samal ajal rusikat raputades.  
#Kui nad loevad "Kolm", näitavad nad korraga käega ühte kolmest märgist: kivi, käärid või paber.

import random

players = ["Игрок 1", "Игрок 2"]
results = {player: 0 for player in players}
rounds = 3 

for round_num in range(1, rounds + 1):
    print(f"\nРаунд {round_num}:")

    input("Нажми Enter для продолжения...")

    choices = ['камень', 'ножницы', 'бумага']
    random.shuffle(choices)

    p1_choice = input(f"{players[0]}, выбери камень, ножницы, или бумагу: ").lower()
    p2_choice = random.choice(choices)

    print(f"{players[0]}: {p1_choice}")
    print(f"{players[1]}: {p2_choice}")

    if p1_choice == p2_choice:
        print("Ничья")
    elif (p1_choice, p2_choice) in [('камень', 'ножницы'), ('ножницы', 'бумага'), ('бумага', 'камень')]:
        print(f"{players[0]} выйгрывает раунд!")
        results[players[0]] += 1
    else:
        print(f"{players[1]} выигрывает раунд!")
        results[players[1]] += 1

print("\nРезультаты игры:")
for player, points in results.items():
    print(f"{player}: {points} очков")
