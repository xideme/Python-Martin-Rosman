import math


#Kodutöö: Esimesed programmid. print(),input(), aritmeetilised operatsioonid

#Ülesanne 8

timeM = int(input("Перевод минут в часы. Введите время в минутах: "))

hours = timeM // 60
min = timeM % 60

print(f"{timeM} минут это {hours} часов и {min} минут")

#Ülesanne 7

speedkm = 29.9

time = float(input("Сколько минут на роликах будешь кататься? "))

travel = (speedkm / 60) * time

print(f"На роликах проедешь расстояние {travel:.2f} километра за {time} минут если твоя средняя скорость {speedkm} км в час")


#Ülesanne 6

fuel = float(input("Введите количество потребленного топлива в литрах: "))

distance = float(input("Введите пройденное расстояние в километрах: "))

fuel100 = (fuel / distance) * 100

print(f"Средний расход топлива составляет {fuel100:.2f} литра на 100 километров.")


#Ülesanne 5

lenght = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

perim = 2 * (lenght + width)
square = lenght * width

print(f"Периметр прямоугольника: {perim}")
print(f"Площадь прямоугольника: {square}")


#Ülesanne 4

choice=input("Какую песню хочешь увидеть? 1 или 2\n").lower()
if choice=="1" or choice=="первую" or choice=="да":

        song = """
        Rong see sõitis tuut tuut tuut,
        piilupart oli rongijuht.
        Rattad tegid kill koll koll,
        kill koll koll ja kill koll kill.
        """
else:
        song = """
        Rong see sõitis tsuhh tsuhh tsuhh,
        piilupart oli rongijuht.
        Rattad tegid rat tat taa,
        rat tat taa ja tat tat taa.
        Aga seal rongi peal,
        kas sa tead, kes olid seal?
        """

print(song)



#Ülesanne 3

kill_koll = "kill-koll "
killadi_koll = "killadi-koll "

row1 = (kill_koll * 3) + killadi_koll + (kill_koll * 3) + killadi_koll + (kill_koll * 2)
row2 = kill_koll

print(row1)
print(row2)

#Ülesanne 2.2

earthR = 6378  # Радиус земли
coinD = 2.55  # диаметр 2 евро в см


earthLenght = 2 * math.pi * earthR * 100000  # длина земли в см
coinDkm = coinD / 100000  # 2 евро диаметр в км

# подсчет
coins = earthLenght // coinDkm

print(f"Что бы линия из 2-х евровых монет обогнула землю, понадобится {int(coins)} 2-х евровых монет.")



#Ülesanne 2.1

radius = float(input("Введите радиус круга (R): "))

# Данные о квадрате
square = 2 * radius  # круг внутри квадрата, сторона квадрата вдвое больше радиуса
squareA = square ** 2
squareP = 4 * square

# Данные о круге
circleA = math.pi * radius ** 2
circleD = 2 * math.pi * radius

print(f"Площадь квадрата: {squareA}")
print(f"Периметр квадрата: {squareP}")
print(f"Площадь круга: {circleA}")
print(f"Длина окружности круга: {circleD}")



#Ülesanne 2

# Без скобок
resultWithout = 3 + 8 / 4 - 2 * 4
print("Без скобок ответ 3 + 8 / 4 - 2 * 4:", resultWithout)

# Со скобками
resultInside = 4 - 2
resultWith = 3 + 8 / resultInside * 4
print("С скобкой ответ 3 + 8 / (4 - 2) * 4:", resultWith)


#Ülesanne 1
name = input("Введи свое имя: ")
print("Привет, " + name + "!")
