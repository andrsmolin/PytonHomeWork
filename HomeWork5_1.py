# Создайте программу для игры в ""Крестики-нолики"

import os
import random

def desk(dct):
    print(f"   1  2   3")
    print(f"A {dct['a']['1']} | {dct['a']['2']} | {dct['a']['3']}")
    print(f"---------------")
    print(f"B {dct['b']['1']} | {dct['b']['2']} | {dct['b']['3']}")
    print(f"---------------")
    print(f"C {dct['c']['1']} | {dct['c']['2']} | {dct['c']['3']}")

def check_win(elem, fld):
    a1 = ((fld['a']['1'] + fld['a']['2'] + fld['a']['3']).count(elem) == 3)         #Проверка на победу
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
    os.system("clr||clear")
    list_g = ['1', '2', '3']
    list_v = ['a', 'b', 'c']
    desk(field)
    if count:
        print(f"игрок {player1}, Ваш ход!: ")                                   # ход игрока
    else:
        print(f"игрок {player2}, Ваш ход!: ")
    while (True):
        goriz = input("gorizont? (1,2,3): ")
        if (list_g.count(goriz) == 1):
            break
    while (True):
        vert = input("vert? (a,b,c): ")
        if (list_v.count(vert) == 1):
            break
    return(vert, goriz)

field = {
    'a': {'1': ' ', '2': ' ', '3': ' '},                                    # Пустое поле для игры
    'b': {'1': ' ', '2': ' ', '3': ' '},
    'c': {'1': ' ', '2': ' ', '3': ' '}
}

player1 = input("player1(X): ")                                         # имена игроков
player2 = input("player2(0): ")

count = not random.randint(0, 1)                                          # Жеребъевка

if count:
    print(f"В результате жеребъевки первым ходит игрок {player1}(X)")      # Жеребъевка
else:
    print(f"В результате жеребъевки первым ходит игрок {player2}(0)")    # Жеребъевка

desk(field)                                                               # Вывод поля для игры

moves = 0                                                                   # обнуляем ходы

while moves <= 8 :
    vert, goriz = move(count)
    if count:
        mark = 'X'
        player = player1
    else:
        mark = '0'
        player = player2
        
    while (field[vert][goriz] != ' '):
        print("клетка занята!")
        vert, goriz = move(count)
    
    field[vert][goriz] = mark
    desk(field)    
    if check_win(mark, field):
        print(f"игрок {player} выиграл!")
        break
    elif moves == 8 :
        print("Ничья")
        break
    else:
        count = not count
        moves += 1
