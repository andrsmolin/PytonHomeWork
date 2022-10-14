from cProfile import label
from operator import index
import os
import random
import math

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def work5():
    a = input('Введите вещественное число: ')
    print(sum([int(i) for i in a if i != ',']))
# work5()

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def work4():
    def input_numbers(input_text):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"{input_text}"))
                is_OK = True
            except ValueError:
                print("Это не число!")
        return number

    def calc_check(input_num):
        my_list = list(map(math.factorial, [i for i in range(1, input_num+1)]))
        return (my_list)

    n = input_numbers("введите число для расчета  ")

    print(calc_check(n))


# work4()

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def work1():
    os.system("cls")

    new_list = [random.randint(0, 100)
                for i in range(0, random.randint(5, 15))]
    sum_list = list(filter(lambda i: new_list.index(i) % 2 != 0, new_list))
    print(new_list, "-> на нечетных позициях ",
          sum_list, "ответ", sum(sum_list))


# work1()

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


def mult_position():
    def filt(a, b):
        c = []
        for i in range(0, len(b)):
            c.append(a[b[i]])
        print(c)
        return c

    n = int(input('Введите N, которое больше 8: '))
    list_n = [random.randint(-n, n+1) for i in range(0, n)]
    print(list_n)

    f = open('file_dz6.txt', 'r')
    data = f.read()
    f.close
    pos = [int(i) for i in data if i != '\n']
    print(pos)

    filt(list_n, pos)
    # list_new = [i for i in list_n if pos.count(list_n.index(i)) > 0]
    # cort = [(i, j) for i in pos for j in list_n if list_n.index(j) == pos[i]]
    # list_pos = [i for i in list_n if list_n.index(i) == pos[i]]
    # # print(pos)
    # # mult = math.prod(filter(lambda i: list_n.index(i) == pos[i], list_n))
    # # cort = list(zip(pos, list(filter(lambda i: list_n.index(i) == pos[i], list_n))))
    # print(list_pos)


mult_position()
# Реализуйте алгоритм перемешивания списка.
