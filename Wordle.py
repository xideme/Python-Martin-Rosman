import random
import imghdr
import tkinter as tk

with open('Wordlelist.txt', encoding="utf-8-sig") as file:
    word_list = file.read().lower().splitlines()

#выбираем случайное слово
word = random.choice(word_list)

#количество попыток
max_attempts = 6

#счетчик попыток
attempts = 0

#словарь для хранения угаданных букв
correct = {letter: False for letter in word}

def display_word():
    #текущее состояние угаданного слова
    display = ""
    for letter in word:
        if correct[letter]:
            display += letter
        else:
            display += "_"
    return display

def add_letter(letter):
    # букву в поле ввода
    textbox.insert(tk.END, letter)

def check():
    #проверяет угаданную букву и отображает сообщение
    global attempts #сохранять состояние количества попыток между вызовами функции
    guess = textbox.get().lower()

    if guess in word:
        for i, letter in enumerate(word): # проверить каждую букву и узнать ее позицию в слове
            if letter == guess:
                correct[guess] = True
                label_word.config(text=display_word())
                if display_word() == word:
                    label_msg.config(text="Вы угадали слово!")
                else:
                    label_msg.config(text=f"Буква '{guess}' угадана", fg="green")
    else:
        attempts += 1
        if attempts >= max_attempts:
            label_msg.config(text=f"Проигрыш. Загаданное слово было: {word}", fg="red")
        else:
            label_msg.config(text=f"Буквы '{guess}' нет в слове.", fg="white")

    textbox.delete(0, tk.END)  #очищаем текстовое поле

   


root = tk.Tk()
root.title("Wordle Game")

root.geometry("850x480")

# фон изображение
background_image = tk.PhotoImage(file="wordle_back.gif")

# отображение фонового изображения
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# задаем цвет текста
root.option_add('*foreground', 'white')

#вывод слова
label_word = tk.Label(root, text=display_word(), font=("Segoe UI", 24), fg="white", bg="black")
label_word.pack(pady=20)

#сообщения
label_msg = tk.Label(root, text="Введи букву что бы попробовать угадать слово", font=("Segoe UI", 14), fg="white", bg="black")
label_msg.pack()

#ввод
textbox = tk.Entry(root, font=("Segoe UI Bold", 18), bg="black", fg="white")
textbox.pack(pady=15)

#кнопка
button_check = tk.Button(root, text="Проверить", bg="black", fg="white", font=("Segoe UI Bold", 18), command=check)
button_check.pack(padx=5, pady=5)



# создаем клавиатуру
keyboard_frame = tk.Frame(root, bg="purple4")
keyboard_frame.pack()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

row1 = alphabet[0:10]
row2 = alphabet[10:19]
row3 = alphabet[19:26]

def key_buttons(row, frame):
    for i in range(len(row)):
        letter = row[i]
        tk.Button(frame, text=letter, font=("Segoe UI", 15), bg="black", fg="white",
                  width=6, height=1,
                  command=lambda l=letter: add_letter(l)).pack(side="left", padx=2, pady=2)

row_list = [row1, row2, row3]
for row_index in range(len(row_list)):
    row = row_list[row_index]
    frame = tk.Frame(keyboard_frame, bg="black")
    frame.grid(row=row_index, column=0, pady=5)
    key_buttons(row, frame)
   


root.mainloop()
