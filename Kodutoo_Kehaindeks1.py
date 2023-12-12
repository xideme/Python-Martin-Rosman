#Praktiline töö "Kehamassi indeks"


try:
    print("Tere! Olen sinu uus sõber - Python!")
    
    nimi = input("Sisesta oma nimi: ")
    
    print(nimi.capitalize() + ", oi kui ilus nimi!")
    
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    
    if vastus == 1:
        pikkus = int(input("Sisesta oma pikkus (cm): "))
        mass = float(input("Sisesta oma kaal (kg): "))
        
        #расчет индекса массы тела
        indeks = mass / (0.01 * pikkus) ** 2
        
        print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
        
        #индекс массы тела
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ülekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
    
    print() #вывод пустой строки
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Viga! Palun sisesta ainult arv!")
