# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from random import randint
from cmath import pi
import math


def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def work1():

    accur = input_numbers("введите число - точность вычисления: ")
    print(round(pi, accur))


# work1()

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def work2():
    numb1 = input_numbers(
        "Введите число для нахождения списка простых множителей: ")
    list_simple = []

    def is_simple(numeros):
        if numeros <= 3:
            return True
        for i in range(numeros-1, int(numeros**0.5)-1, -1):
            if numeros % i == 0:
                return False
        else:
            return True

    for i in range(2, numb1, 1):
        if numb1 % i == 0 and is_simple(i):
            while (numb1 % i == 0):
                list_simple.append(i)
                numb1 /= i
    print(list_simple)


# work2()


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def work3():
    new_string = input(
        "Введите последовательность чисел через пробел: ").split()
    temp_string = []
    for i in range(0, len(new_string)):
        if new_string.count(new_string[i]) == 1:
            temp_string.append(new_string[i])
    print(*new_string, " -> ", *temp_string)


# work3()

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def work4(name):
    k = input_numbers("Введите степень многочлена (от 3 до 5): ")
    coe = [randint(0, 101) for i in range(0, k)]
    data = open(f'{name}.txt', 'w')
    for i in range(0, len(coe)):
        if k-i == 1:
            data.write(f"{coe[i]}*x")
        else:
            data.write(f"{coe[i]}*x**{k-i} + ")
    data.write(f" = 0")

    data.close

# work4("file1")

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def work5():
    data = open('file_2x.txt', 'w')
    data1 = open('file.txt', 'r')
    data2 = open('file1.txt', 'r')
    list1 = [line.split() for line in data1].pop()
    list2 = [line.split() for line in data2].pop()
    list2.insert(0, "+")
    list1.remove("=")
    list1.remove("0")
    for i in range(0, len(list1)):
        data.write(f"{list1[i]} ")
    for i in range(0, len(list2)):
        data.write(f"{list2[i]} ")
    data.close
    data1.close
    data2.close


work5()
