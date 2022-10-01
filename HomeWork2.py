# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
from itertools import count
import random
a = random.randint(0, 100)
b = random.randint(3, 20)
inp_numb = round(a/b, 5)
print(inp_numb)
count = 0
while (inp_numb % 10 > 0):
    inp_numb *= 10
    count += 1

current_numb = int(inp_numb/10)


def summ_numb(num):
    summ = 0
    for i in range(0, count+1):
        summ += num % 10
        num = int(num/10)

    return (summ)


print(summ_numb(current_numb))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


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
    my_list = [1]
    for i in range(1, input_num):
        my_list.append(my_list[i-1]*(i+1))
    return (my_list)


n = input_numbers("введите число для расчета  ")

print(calc_check(n))


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def create_list(input_num):
    my_list = []
    sum_2 = 0
    for i in range(0, input_num):
        my_list.append(round((1+1/input_num)**input_num, 1))
        sum_2 += round((1+1/input_num)**input_num, 1)
    return (my_list, round(sum_2, 1))


nm = input_numbers("введите число для расчета  ")

print(create_list(nm))
