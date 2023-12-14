from random import *


#7

# Генерация списка из 10 случайных чисел в диапазоне от -10 до 10
numbers = [randint(-10, 10) for i in range(10)]

print("Исходный список:", numbers)

# Сортировка по возрастанию абсолютного значения
ascending = sorted(numbers, key=abs)
print("По возрастанию абсолютного значения:", ascending)

# Сортировка по убыванию абсолютного значения
descending = sorted(numbers, key=abs, reverse=True)
print("По убыванию абсолютного значения:", descending)





kokku=randint(2,20)
print("kokku jäerjedis on: ", kokku, "elementi")
num_list=[]
for i in range(kokku):
    num_list.append(round(random()*1000,2))
print(num_list)
max_=max(num_list)
n=num_list.index(max_)
print("\t",max_,"positsioonil:", n+1)
num_list.pop(n)
max_=max_/len(num_list)
num_list.insert(n,max_)
print(num_list)
#6

import random

# Генерируем список случайных чисел длиной 10
numbers = [random.randint(1, 100) for _ in range(10)]

print(f"Генерируем список из 10 случайных чисел \n{numbers}:")

# Находим максимальное число в списке
max_num = max(numbers)

# Делим максимальное число на длину списка
result = max_num / len(numbers)

# Заменяем максимальное число в списке результатом деления
numbers[numbers.index(max_num)] = result

# Заменяем максимальное число в списке результатом деления


print(f"Делим максимальное число на длину списка и заменяем максимальное число в списке результатом деления \n{result}:")






#5


# Запрашиваем список у пользователя
user_list = input("Введите список элементов, разделенных пробелом: ").split()

# Запрашиваем количество пар элементов для обмена
num_swaps = int(input("Введите количество пар элементов для обмена: "))

# Проверяем, что в списке достаточно элементов для обмена
if len(user_list) < 2*num_swaps:
    print("В списке недостаточно элементов для обмена.")
else:
    # Меняем местами элементы
    for i in range(num_swaps):
        user_list[i], user_list[-i-1] = user_list[-i-1], user_list[i]

    # Выводим обновленный список
    print("Обновленный список: ", ' '.join(user_list))





#4

indexid=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa" ]

while True:
    try:
        index=int(input("Sisesta postindex:" ))
        if len(str(index))==5:
            break
    except:
        print("Viga")
print("Indexi analüüs")
index_list=list(str(index))
s1=int(index_list[0])
print("Index {0} on {1} piirkonnas".format(index,indexid[s1-1]))



while True:
    indeks = input("Sisesta postiindeks: ")

    if len(indeks) != 5 or not indeks.isdigit():
        print("Vigane postiindeks!")
    else:
        n1 = int(indeks[0])
        if n1 == 1:
            print("Tallinn")
            print("Оставайтесь дома!")
            break
        elif n1 == 2:
            print("Narva, Narva-Jõesuu")
            print("Оставайтесь дома!")
            break
        elif n1 == 3:
            print("Kohtla-Järve")
            print("Оставайтесь дома!")
            break
        elif n1 == 4:
            print("Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
            print("Носите маски!")
            break
        elif n1 == 5:
            print("Tartu linn")
            print("Носите маски!")
            break
        elif n1 == 6:
            print("Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
            print("Носите маски!")
            break
        elif n1 == 7:
            print("Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
            print("Носите маски!")
            break
        elif n1 == 8:
            print("Pärnumaa")
            print("Носите маски!")
            break
        elif n1 == 9:
            print("Läänemaa, Hiiumaa, Saaremaa")
            print("Носите маски!")
            break
        else:
            print("Vigane postiindeks!")





#2

names = []
name_num = 0
for _ in range(5):
    name_num+=1
    name = input(f"{name_num} Enter a name:")
    names.append(name)

# Display names in alphabetical order
names_sorted = sorted(names)
print("\nNames in alphabetical order:", names_sorted)

# Display the last added name separately
last_added_name = names[-1]
print("Last added name:", last_added_name)

# Allow the user to change names in the list
change_index = int(input("Enter the index of the name you want to change (0-4): "))
if 0 <= change_index < 5:
    new_name = input("Enter the new name: ")
    names[change_index] = new_name
    print("\nUpdated names:", names)

# Remove duplicates from the list of students
students = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
unique_students = list(set(students))
print("\nUnique students:", unique_students)

# List of ages
ages = [25, 30, 22, 28, 35]

# Find the largest and smallest number
largest_age = max(ages)
smallest_age = min(ages)

# Calculate the total and average of ages
total_age = sum(ages)
average_age = total_age / len(ages)

# Display the results
print("\nAges:")
print(f"Largest age: {largest_age}")
print(f"Smallest age: {smallest_age}")
print(f"Total age: {total_age}")
print(f"Average age: {average_age:.2f}")


#1

vowels_ru = "аеёиоуыэюя"
consonants_ru = "бвгджзйклмнпрстфхцчшщ"

vowels_en = "aeiou"
consonants_en = "bcdfghjklmnpqrstvwxyz"

tekst = input("Введите слово или предложение: ")

vowel = 0
consonant = 0
punctuation = 0
space = 0
digits = 0

for char in tekst:
    if char.lower() in vowels_ru + vowels_en:
        vowel += 1
    elif char.lower() in consonants_ru + consonants_en:
        consonant += 1
    elif char in '.,;:!?':
        punctuation += 1
    elif char.isspace():
        space += 1
    elif char.isdigit():
        digits += 1

print("\nРезультаты:")
print(f"Гласные: {vowel}")
print(f"Согласные: {consonant}")

if punctuation > 0:
    print(f"Знаки препинания: {punctuation}")

if space > 0:
    print(f"Пробелы: {space}")

if digits > 0:
    print(f"Цифры: {space}")


import string

konsonanti="bcdfghjlmnpqrstvx"
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
markid=string.punctuation
v=k=m=t=0
while True:
    tekst=input("Sisesta sõna või lause: ") #.lower()
    if tekst.isdigit():
        break
    else:
        tekst_l=list(tekst)
        for e in tekst_l:
            if e.lower() in vokaali:
                v+=1
            elif e.lower() in konsonanti:
                k+=1
            elif e.lower() in markid:
                m+=1
            elif e.lower()==" ":
                t+=1

    print("Vokaali: ", v)
    print("Konsonanti:",k)
    print("Markid: ", m)
    print("Tuhikud:",t)