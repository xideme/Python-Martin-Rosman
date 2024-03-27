import random
import tkinter as tk

with open('Wordlelist.txt', encoding="utf-8-sig") as file:
    word_list = file.read().lower().splitlines()

# Выбираем случайное слово
word = random.choice(word_list)

# Максимальное количество попыток
max_attempts = 6

# Счетчик попыток
attempts = 0

# Словарь для хранения состояния угаданных букв
correct = {letter: False for letter in word}

def display_word():
    """Отображает текущее состояние угаданного слова."""
    display = ""
    for letter in word:
        if correct[letter]:
            display += letter
        else:
            display += "_"
    return display

def add_letter(letter):
    """Добавляет угаданную букву в поле ввода."""
    textbox.insert(tk.END, letter)

def check():
    """Проверяет угаданную букву и отображает отчет."""
    global attempts
    guess = textbox.get().lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                correct[guess] = True
                label_word.config(text=display_word())
                if display_word() == word:
                    label_msg.config(text="Вы угадали слово!")
                    textbox.config(state='disabled')
                    return  # Используем return, чтобы завершить функцию после угадывания всего слова
                else:
                    label_msg.config(text=f"Буква '{guess}' угадана, но стоит не на своем месте.", fg="yellow")
    else:
        attempts += 1
        if attempts >= max_attempts:
            label_msg.config(text=f"Проигрыш. Загаданное слово было: {word}", fg="red")
            textbox.config(state='disabled')
        else:
            label_msg.config(text=f"Буквы '{guess}' нет в слове.", fg="white")

    textbox.delete(0, tk.END)  # Очищаем текстовое поле

   


root = tk.Tk()
root.title("Wordle Game")

root.geometry("850x480")

# Загружаем изображение
background_image = tk.PhotoImage(file="wordle_back.gif")

# Создаем метку для отображения фонового изображения и устанавливаем его
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Задаем цвет текста для окна
root.option_add('*foreground', 'white')

label_word = tk.Label(root, text=display_word(), font=("Arial", 24), fg="white", bg="black")
label_word.pack(pady=20)

label_msg = tk.Label(root, text="Please enter a symbol to guess a word", font=("Segoe UI", 14), fg="white", bg="black")
label_msg.pack()

textbox = tk.Entry(root, font=("Segoe UI Bold", 18), bg="black", fg="white")
textbox.pack(pady=10)

button_check = tk.Button(root, text="Проверить", bg="black", fg="white", font=("Segoe UI Bold", 18), command=check)
button_check.pack()



# Создаем клавиатуру
keyboard_frame = tk.Frame(root, bg="purple4")
keyboard_frame.pack()

# Буквы алфавита
alphabet = 'abcdefghijklmnopqrstuvwxyz'

row1 = alphabet[0:10]
row2 = alphabet[10:19]
row3 = alphabet[19:26]

def create_buttons(row, frame):
    for letter in row:
        tk.Button(frame, text=letter, font=("Segoe UI", 15), bg="black", fg="white",
                  width=6, height=2,
                  command=lambda l=letter: add_letter(l)).pack(side="left", padx=1, pady=1)

for row_index, row in enumerate([row1, row2, row3]):
    frame = tk.Frame(keyboard_frame, bg="black")
    frame.grid(row=row_index, column=0, pady=5)
    create_buttons(row, frame)
   


root.mainloop()
