# Создайте программу для игры в ""Крестики-нолики""

import os
import random
# from typing import Dict


def desk(dct):
    # os.system("clear")
    print(f"   1   2  3")
    print(f"A {dct['a']['1']} | {dct['a']['2']} | {dct['a']['3']}")
    print(f"---------------")
    print(f"B {dct['b']['1']} | {dct['b']['2']} | {dct['b']['3']}")
    print(f"---------------")
    print(f"C {dct['c']['1']} | {dct['c']['2']} | {dct['c']['3']}")


def chek_inp(elem, check_list):
    return not (check_list.count(elem))


def chek_empty(fld, x, y):
    return fld[x][y] == ' '


def check_win(elem, fld):
    a1 = ((fld['a']['1'] + fld['a']['2'] + fld['a']['3']).count(elem) == 3)
    a2 = ((fld['b']['1'] + fld['b']['2'] + fld['b']['3']).count(elem) == 3)
    a3 = ((fld['c']['1'] + fld['c']['2'] + fld['c']['3']).count(elem) == 3)
    a4 = ((fld['a']['1'] + fld['b']['1'] + fld['c']['1']).count(elem) == 3)
    a5 = ((fld['a']['2'] + fld['b']['2'] + fld['c']['2']).count(elem) == 3)
    a6 = ((fld['a']['3'] + fld['b']['3'] + fld['c']['3']).count(elem) == 3)
    a7 = ((fld['a']['1'] + fld['b']['2'] + fld['c']['3']).count(elem) == 3)
    a8 = ((fld['a']['3'] + fld['b']['2'] + fld['c']['1']).count(elem) == 3)
    if a1 or a2 or a3 or a4 or a5 or a6 or a7 or a8:
        return True


def move(count):
    if count:
        print(f"игрок {player1}, Ваш ход!: ")
    else:
        print(f"игрок {player2}, Ваш ход!: ")
    while (True):
        goriz = input("gorizont? (1,2,3): ")
        if not chek_inp(goriz, ['1', '2', '3']):
            break
    while (True):
        vert = input("vert? (a,b,c): ")
        if not chek_inp(vert, ['a', 'b', 'c']):
            break
    return (vert, goriz)


field = {
    'a': {'1': ' ', '2': ' ', '3': ' '},
    'b': {'1': ' ', '2': ' ', '3': ' '},
    'c': {'1': ' ', '2': ' ', '3': ' '}
}
# mark = ''
player1 = input("player1(X): ")  # имена игроков
player2 = input("player2(0): ")
# vert, goriz = 'a', '1'

# Жеребъевка
count = not random.randint(0, 1)

if count:
    # Жеребъевка
    print(f"В результате жеребъевки первым ходит игрок {player1}(X)")
else:
    # Жеребъевка
    print(f"В результате жеребъевки первым ходит игрок {player2}(0)")

# Пустое поле
desk(field)

# обнуляем ходы
moves = 0

while moves <= 9:
    vert, goriz = move(count)
    if count:
        mark = 'X'
        player = player1
    else:
        mark = '0'
        player = player2

    while not chek_empty(field, vert, goriz):
        print("is closed! Try again")
        vert, goriz = move(count)

    field[vert][goriz] = mark
    desk(field)
    if check_win(mark, field):
        print(f"игрок {player} выиграл!")
        break
    elif moves == 9:
        print("Ничья")
        break
    else:
        count = not count
        moves += 1
