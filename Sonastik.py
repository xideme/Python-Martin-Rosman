import random

# Функция для чтения данных из файла
def loe_failist(f):
    with open(f,'r',encoding="utf-8") as fail:
        mas = [rida.strip() for rida in fail]
    return mas

# Функция для добавления слова в словарь
def add_word(word, translation, lang):
    with open(f"{lang}.txt", 'a', encoding="utf-8") as f:
        f.write(f"\n{word}:{translation}")

# Функция для исправления ошибки в словаре
def correct_word(old_word, new_word, new_translation, lang):
    words = loe_failist(f"{lang}.txt")
    with open(f"{lang}.txt", 'w', encoding="utf-8") as f:
        for word in words:
            if word.split(':')[0] == old_word:
                f.write(f"{new_word}:{new_translation}\n")
            else:
                f.write(f"{word}\n")

# Функция для проверки знания слов
def check_knowledge(lang):
    words = loe_failist(f"{lang}.txt")
    random.shuffle(words)
    correct = 0
    for word in words:
        print(f"Переведите слово: {word.split(':')[0]}")
        answer = input()
        if answer == word.split(':')[1]:
            print("Верно!")
            correct += 1
        else:
            print("Неверно!")
    print(f"Ваш результат: {correct / len(words) * 100}%")


def main():
    rus = loe_failist("RUS.txt")
    eng = loe_failist("ENG.TXT")

    while True:
        print("1. Добавить слово")
        print("2. Исправить слово")
        print("3. Проверить знания")
        print("4. Проговорить слово")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            word = input("Введите слово: ")
            translation = input("Введите перевод: ")
            lang = input("Введите язык (rus или eng): ")
            add_word(word, translation, lang)
        elif choice == "2":
            old_word = input("Введите старое слово: ")
            new_word = input("Введите новое слово: ")
            new_translation = input("Введите новый перевод: ")
            lang = input("Введите язык (rus или eng): ")
            correct_word(old_word, new_word, new_translation, lang)
        elif choice == "3":
            lang = input("Введите язык (rus или eng): ")
            check_knowledge(lang)
        elif choice == "4":
            word = input("Введите слово: ")
            speak_word(word)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()


