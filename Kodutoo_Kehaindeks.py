try:
    print("Tere! Olen sinu uus sõber - Python!")
    
    # Ввод имени пользователя
    nimi = input("Sisesta oma nimi: ")
    
    # Вывод приветствия с использованием введенного имени
    print(nimi + ", oi kui ilus nimi!")
    
    # Задаем вопрос и получаем ответ
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    
    if vastus == 1:
        # Ввод длины и массы для расчета индекса массы тела
        pikkus = int(input("Sisesta oma pikkus (cm): "))
        mass = float(input("Sisesta oma kaal (kg): "))
        
        # Расчет индекса массы тела
        indeks = mass / (0.01 * pikkus) ** 2
        
        # Вывод результата
        print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
        
        # Оценка индекса массы тела
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
    
    # Вывод пустой строки
    print()
    
    # Прощальное сообщение
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Viga! Palun sisesta korrektne arv.")
