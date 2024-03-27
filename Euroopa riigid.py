from random import *

def failist_to_dict(f: str):  
    riik_pealinn = {}  
    pealinn_riik = {}  
    riigid = []  
    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')  
            riik_pealinn[k] = v
            pealinn_riik[v] = k
            riigid.append(k)
    
    return riik_pealinn, pealinn_riik, riigid

def Dict_to_files(fail: str, jarjend: list): 
    with open(fail, 'w', encoding="utf-8") as f:
        for item in jarjend:
            f.write(item + "\n")
        print("Dictionary saved!")

def RiikPealinn(riik_pealinn: dict, pealinn_riik: dict):
    print("\nSearch for capital 1 or country 2\n")
    Choice1 = input("Enter your choice: ")
    if Choice1 in ['1', '2']:
        Choice1 = int(Choice1)
        if Choice1 == 1:
            pealinn = input("Enter the capital: ")
            if pealinn in pealinn_riik:
                print("Country:", pealinn_riik[pealinn])
            else:
                print("Capital not found in the list!")
                add = input("Do you want to add it to the dictionary? (yes/no): ").lower()
                if add == 'yes':
                    new_country = input("Enter the country for the capital: ")
                    riik_pealinn[new_country] = pealinn
                    pealinn_riik[pealinn] = new_country
                    print("Capital and country added to the dictionary.")
                    Dict_to_files("RiigidPealinnad.txt", sorted(riik_pealinn.keys()))  # Save to file
        elif Choice1 == 2:
            riik = input("Enter the country: ")
            if riik in riik_pealinn:
                print("Capital:", riik_pealinn[riik])
            else:
                print("Country not found in the list!")
                add = input("Do you want to add it to the dictionary? (yes/no): ").lower()
                if add == 'yes':
                    new_capital = input("Enter the capital for the country: ")
                    riik_pealinn[riik] = new_capital
                    pealinn_riik[new_capital] = riik
                    print("Country and capital added to the dictionary.")
                    Dict_to_files("RiigidPealinnad.txt", sorted(riik_pealinn.keys()))  # Save to file
    else:
        print("Invalid choice.")

def AddDelete(riik_pealinn: dict, pealinn_riik: dict, riigid: list):
    print("\nAdd 1 or Delete 2\n")
    Choice2 = input("Your choice: ")
    if Choice2 in ['1', '2']:
        Choice2 = int(Choice2)
        if Choice2 == 1:
            NewRiik = input("Enter new country: ")
            NewPealinn = input("Enter the capital of the country: ")
            if NewRiik in riik_pealinn:
                print("This country already exists in the list!")
            else:
                riik_pealinn[NewRiik] = NewPealinn
                pealinn_riik[NewPealinn] = NewRiik
                Dict_to_files("RiigidPealinnad.txt", [f"{NewRiik}-{NewPealinn}" for NewRiik, NewPealinn in riik_pealinn.items()])
        elif Choice2 == 2:
            DelRiik = input("Do you want to delete by country 1 or by capital 2\n")
            DelRiik = int(DelRiik)
            if DelRiik in [1, 2]:
                if DelRiik == 1:
                    DeleteRiik = input("Enter the capital of the country: ")
                    if DeleteRiik in riik_pealinn:
                        V = riik_pealinn.get(DeleteRiik)
                        riik_pealinn.pop(DeleteRiik)
                        pealinn_riik.pop(V)
                        riigid.remove(V)
                        Dict_to_files("RiigidPealinnad.txt", [f"{riik}-{pealinn}" for riik, pealinn in riik_pealinn.items()])
                    else:
                        print("This country is not in the list!")
                elif DelRiik == 2:
                    DeletePealinn = input("Enter the country: ")
                    if DeletePealinn in pealinn_riik:
                        K = pealinn_riik[DeletePealinn]
                        pealinn_riik.pop(DeletePealinn)
                        riik_pealinn.pop(K)
                        riigid.remove(K)
                        Dict_to_files("RiigidPealinnad.txt", [f"{riik}-{pealinn}" for riik, pealinn in riik_pealinn.items()])
                    else:
                        print("This capital is not in the list!")
            else:
                print("Invalid choice.")
    else:
        print("Invalid choice.")

def Game(riik_pealinn: dict, pealinn_riik: dict, riigid: list): 
    Score = 0
    percent = 0
    Gameanswer = []  # список заданных вопросов
    Choice3 = input("\nChoose Country To Capital 1 or Capital To Country 2: ")
    if Choice3 == '1' or Choice3 == '2':
        Choice3 = int(Choice3)
        if Choice3 == 1:
            for i in range(5):
                j = randint(0, len(riigid) - 1)
                while j in Gameanswer:  # проверяем что бы дубликатов не было
                    j = randint(0, len(riigid) - 1)
                Gameanswer.append(j)  
                print("Lets ", i + 1, ": Guess the capital of " + riigid[j] + "?")
                Gameinput1 = input("Your answer: ")
                if Gameinput1.lower() == riik_pealinn[riigid[j]].lower():
                    Score += 1
                    print("Correct answer!")
                else:
                    print("Wrong answer!")
            percent = (Score / 5) * 100
            print("Game over! Your score:", Score, "out of 5 turns (", percent, "%)...")
        elif Choice3 == 2:
            for i in range(5):
                j = randint(0, len(pealinn_riik) - 1)
                while j in Gameanswer:
                    j = randint(0, len(pealinn_riik) - 1)
                Gameanswer.append(j)
                print("Turn ", i + 1, ": Guess the country of capital " + pealinnad[j] + "?")
                Gameinput2 = input("Your answer: ")
                if Gameinput2.lower() == pealinn_riik[pealinnad[j]].lower():
                    Score += 1
                    print("Correct answer!")
                else:
                    print("Wrong answer!")
            percent = (Score / 5) * 100
            print("Game over! Your score:", Score, "out of 5 turns (", percent, "%)...")
    else:
        print("Invalid choice.")

        

riik_pealinn, pealinn_riik, riigid = failist_to_dict("RiigidPealinnad.txt")
riigid = list(dict.fromkeys(riigid))  
pealinnad = list(pealinn_riik.keys())  

while True:
    print("\n")
    print("View Country or Capital - 1\nAdd/Delete Country or Capital - 2\nGame - 3\nEXIT - 4\n")
    choice = input("What option do you choose? ")
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        choice = int(choice)
        if choice == 1:
            RiikPealinn(riik_pealinn, pealinn_riik)
        elif choice == 2:
            AddDelete(riik_pealinn, pealinn_riik, riigid)
        elif choice == 3:
            Game(riik_pealinn, pealinn_riik, riigid)  
        elif choice == 4:
            break
    else:
        print("Invalid choice.")
