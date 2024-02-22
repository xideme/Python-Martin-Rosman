
import random
import tkinter as tk
from tkinter import messagebox

# Список слов (можно считать из файла)
word_list = ["apple", "banana", "cherry", "grape", "orange", "pear"]

# Выбираем случайное слово
secret_word = random.choice(word_list)

# Максимальное количество попыток
max_attempts = 6

# Счетчик попыток
attempts = 0

# Словарь для хранения состояния угаданных букв
guessed_letters = {letter: False for letter in secret_word}

def display_word():
    """Отображает текущее состояние угаданного слова."""
    display = ""
    for letter in secret_word:
        if guessed_letters[letter]:
            display += letter
        else:
            display += "_"
    return display

def check_guess():
    """Проверяет угаданную букву."""
    guess = entry.get().lower()

    if guess in secret_word:
        guessed_letters[guess] = True
        label_word.config(text=display_word())
        if display_word() == secret_word:
            messagebox.showinfo("Поздравляем!", f"Вы угадали слово: {secret_word}")
            root.destroy()
    else:
        messagebox.showerror("Ошибка", "Этой буквы нет в слове.")

    entry.delete(0, tk.END)



root = tk.Tk()
root.title("Игра в слова")

label_word = tk.Label(root, text=display_word(), font=("Arial", 24))
label_word.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(pady=10)

button_check = tk.Button(root, text="Проверить", command=check_guess)
button_check.pack()

root.mainloop()
