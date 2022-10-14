# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import random
# import string


def work1():
    text = "Я помню чудное мнгнабвение, передо мной яабвилась ты..."
    print(text)

    list1 = [x for x in text.split()]

    list2 = list(filter(lambda i: i.count('абв') == 0, list1))

    text = list2[0] + ' '
    for i in range(1, len(list2)):
        text += list2[i] + ' '

    print(text)

# work1()

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


def work2():
    name1 = input("Введите имя первого игрока: ")
    name2 = input(
        "Введите имя второго игрока (если введете 'бот', то будете играть с компьютором): ")

    def input_numbers(input_text):
        is_OK = False
        while not is_OK:
            number = input(f"{input_text}")
            if number.isdigit() and int(number) > 0:
                is_OK = True
            else:
                print("Внимание!")
        return int(number)

    def bot(konf, count):
        while (konf > 0):
            if count:
                print(f"ходит игрок {name1}")
                decr = input_numbers("сколько конфет Вы хотите взять? ")
                while decr > konf or decr > 28:
                    print("столько брать нельзя!")
                    decr = input_numbers("сколько конфет Вы хотите взять? ")

            else:
                if konf > 58:
                    decr = random.randint(1, 29)
                    print(f"Бот берет {decr} конфет")
                else:
                    if konf < 29:
                        decr = konf
                        print(f"Бот берет {decr} конфет")
                    else:
                        decr = konf - 29
                        print(f"Бот берет {decr} конфет")

            konf -= decr
            count = not count
            print(f"Осталось конфет: {konf}")
        else:
            if count:
                print(f"игрок {name2} победил")
            else:
                print(f"игрок {name1} победил")

    def human(konf, count):
        while (konf > 0):
            if count:
                print(f"ходит игрок {name1}")
            else:
                print(f"ходит игрок {name2}")

            decr = input_numbers("сколько конфет Вы хотите взять? ")

            while decr > konf or decr > 28:
                print("столько брать нельзя!")
                decr = input_numbers("сколько конфет Вы хотите взять? ")
            konf -= decr
            count = not count
            print(f"Осталось конфет: {konf}")
        else:
            if count:
                print(f"игрок {name2} победил")
            else:
                print(f"игрок {name1} победил")

    print("Начало игры")

    count = not random.randint(0, 1)
    print("На столе лежит 2021 конфета. Игроки делают ход друг после друга. За один ход можно забрать не более чем 28 конфет. Побеждает тот, кто забирает последнюю конфету! Начинаем.")
    if count:
        print(f"В результате жеребъевки первым ходит игрок {name1}")
    else:
        print(f"В результате жеребъевки первым ходит игрок {name2}")
    konf = 221
    if name2 == 'Бот' or name2 == 'бот' or name2 == 'bot' or name2 == 'Bot':
        bot(konf, count)
    else:
        human(konf, count)

# work2()

# Создайте программу для игры в ""Крестики-нолики""(в отдельном файле)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression():
    f = open('file_data.txt', 'r')
    data = f.read() + ' '
    f.close
    new_data = ""
    count = 1
    for i in range(0, len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            new_data += str(count) + '*' + data[i] + ' '
            count = 1
    print(new_data)
    f1 = open('file_data1.txt', 'w')
    f1.write(new_data)
    f1.close


def recovery():
    f2 = open('file_data1.txt', 'r')
    data2 = f2.read()
    f2.close()
    numbers = []

    line1 = ''
    while data2 != '':
        sp_pos = data2.index('*')
        space_pos = data2.index(' ')
        k = int(data2[:sp_pos])
        for i in range(1, k+1):
            line1 += data2[sp_pos+1:space_pos]
        data2 = data2[space_pos+1:]

    print(line1)


# compression()
# recovery()
