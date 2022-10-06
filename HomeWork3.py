
# from curses.ascii import isdigit
import random
import os


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def work1():
    os.system("cls")
    new_lenght = random.randint(5, 15)
    new_list = []
    list_elem = []
    for i in range(0, new_lenght):
        new_list.append(random.randint(0, 100))
        if i % 2 != 0:
            list_elem.append(new_list[i])
    print(new_list, "-> на нечетных позициях ",
          list_elem, "ответ", sum(list_elem))


work1()

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def work2():
    # os.system("cls")
    new_lenght = random.randint(4, 10)
    new_list = []
    list_elem = []
    j = int(new_lenght/2)
    for i in range(0, new_lenght):
        new_list.append(random.randint(0, 10))
    for i in range(0, j):
        list_elem.append(new_list[i]*new_list[new_lenght-1-i])
    print(new_list, "=>", list_elem)


work2()

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def work3():
    # os.system("cls")
    new_lenght = random.randint(4, 10)
    new_list = []
    for i in range(0, new_lenght):
        new_list.append(round((random.randint(20, 200)/17.5), 2))
    max1 = min1 = new_list[0] % 1
    for i in range(0, new_lenght):
        if new_list[i] % 1 > max1:
            max1 = new_list[i] % 1
        if new_list[i] % 1 < min1:
            min1 = new_list[i] % 1
    print(new_list, "=>", round(max1 - min1, 2))


work3()


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def work4():
    # os.system("cls")

    def input_numbers(input_text):
        is_OK = False
        while not is_OK:
            number = input(f"{input_text}")
            if number.isdigit() and int(number) > 0:
                is_OK = True
            else:
                print("Внимание!")
        return int(number)
    num_dec = input_numbers("Введите целое положительное число: ")
    num_bin = []
    str_bin = "dec " + str(num_dec) + " = bin "
    while num_dec > 1:
        num_bin.append(num_dec % 2)
        num_dec = int(num_dec/2)
    else:
        num_bin.append(1)
    for i in range(len(num_bin)-1, -1, -1):
        str_bin += str(num_bin[i])

    print(str_bin)


work4()
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def work5():
    def input_numbers(input_text):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"{input_text}"))
                is_OK = True
            except ValueError:
                print("Это не число!")
        return number
    # os.system("cls")
    indx = input_numbers("Задайте число ")
    list1 = [0]

    def fibonacci(k):
        if k in [1, 2]:
            return 1
        elif k > 0:
            return fibonacci(k-1) + fibonacci(k-2)
    k1 = 1
    for i in range(1, indx+1):
        list1.insert(0, fibonacci(i)*k1)
        list1.append(fibonacci(i))
        k1 = k1*-1
    print(list1)


work5()
