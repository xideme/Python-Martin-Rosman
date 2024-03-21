import random

#открытие и чтение из файла
def read_from_file(f):
    file = open(f, 'r', encoding="utf-8")
    array = [] 
    for line in file:
        array.append(line.strip()) #удаляем лишние пробелы
    file.close()
    return array

#сохранение в файл
def save_to_file(f, array):
    file = open(f, 'w', encoding="utf-8")
    for element in array:
        file.write(element + '\n')
    file.close()
    
#указание файла словаря
rusd:list = read_from_file("RUS.txt")
estd:list = read_from_file("EST.txt")

#перевод на русский
def rustrans(word, estd, rusd):
    if word in estd:
        index = estd.index(word) #получение индекса эстонского слова
        trans = rusd[index] #индекс эст для русского слова
        print(f"The translation of '{word}' is '{trans}'.")
    else:
        print(f"The word '{word}' was not found in the dictionary.")

#перевод на эстонский
def esttrans(word, estd, rusd):
    if word in rusd:
        index = rusd.index(word)
        trans = estd[index]
        print(f"The translation of '{word}' is '{trans}'.")
    else:
        print(f"The word '{word}' was not found in the dictionary.")




#добавление слова в словарь
def add(word, array, f):
    if word not in array:
        print(f"The word '{word}' is not in the dictionary. Do you want to add it?")
        answer = input("Yes (y) / No (n): ").lower()
        if answer == 'y':
            array.append(word)
            save_to_file(f, array)  # Сохраняем изменения в файле
            print(f"The word '{word}' has been added to the dictionary.")
        else:
            print("The word was not added.")
    else:
        print(f"The word '{word}' is already in the dictionary.")






        
#изменение слова в словаре
def edit(old_word, new_word, array, f):
    if old_word in array:
        index = array.index(old_word)
        array[index] = new_word
        save_to_file(f, array)  # Сохраняем изменения в файле
        print(f"The word '{old_word}' has been successfully replaced with '{new_word}'.")
    else:
        print(f"The word '{old_word}' was not found in the dictionary.")

#подсчет количества правильных ответов
def check(input_array, check_array):
    correct = 0
    for i in input_array:
        if i in check_array:
            correct += 1
    return correct

while True:
    print("\nChoose an action:")
    print("1. Translate from Estonian to Russian")
    print("2. Translate from Russian to Estonian")
    print("3. Test your knowledge")
    print("4. Add a word in the dictionary")
    print("5. Edit a word to the dictionary")
    print("6. Exit the program")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        word = input("Enter a word in Estonian: ")
        rustrans(word, estd, rusd)
    elif choice == '2':
        word = input("Enter a word in Russian: ")
        esttrans(word, estd, rusd)
    elif choice == '3':
        print("\nTest your knowledge:")
        check_array = random.sample(estd, 5)  # выбор 5 случайных слов из эст словаря
        print("Random 5 words in Estonian:")
        for i in range(len(check_array)): #перечисление слов из списка по номерам
            estword = check_array[i]
            print(f"{i+1}. {estword}")

        estrusdict = dict(zip(estd, rusd)) # создание словаря с парами "эстонское слово: русский перевод"
        correct = [estrusdict[estword] for estword in check_array] # создание списка правильных слов для проверки
        user_array = []
        for estword in check_array:
            user_word = input(f"Enter the translation of the word '{estword}': ")
            user_array.append(user_word)
        correctnum = check(user_array, correct)  # правильные ответы
        percentage = (correctnum / 5) * 100
        print(f"Your result: {percentage}% or {correctnum} out of 5")
    elif choice == '4':
         word = input("Enter a word you want to add to the dictionary: ")
         dictionary_choice = input("Choose the dictionary to add the word (RUS or EST): ").upper()
         if dictionary_choice == 'RUS':
            add(word, rusd, "RUS.txt")  #сохранение нового слова в русский словарь
         elif dictionary_choice == 'EST':
            add(word, estd, "EST.txt")  #сохранение нового слова в эстонский словарь
         else:
            print("Invalid dictionary choice.")
    elif choice == '5':
        old_word = input("Enter the word you want to edit: ")
        new_word = input("Enter the new word: ")
        dictionary_choice = input("Choose the dictionary to edit the word (RUS or EST): ").upper()
        if dictionary_choice == 'RUS':
            edit(old_word, new_word, rusd, "RUS.txt")  #сохранение нового слова в русский словарь
        elif dictionary_choice == 'EST':
            edit(old_word, new_word, estd, "EST.txt")  #сохранение нового слова в эстонский словарь
        else:
            print("Invalid dictionary choice.")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
