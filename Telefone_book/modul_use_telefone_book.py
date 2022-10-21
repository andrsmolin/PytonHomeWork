import view as v

id_person = ""
surname = ""
name_person = ""
number_person = ""
status_person = ""


def init(id, sur, name, num, stat):
    global id_person
    global name_person
    global number_person
    global status_person
    global surname
    id_person = id
    name_person = name
    number_person = num
    status_person = stat
    surname = sur


def contact(func):  # общий метод дописать и прочитать
    strings = return_data().split("\n")
    surname = v.input_surname()
    for i in range(0, len(strings)):
        if strings[i].find(surname) > 0:
            func(strings[i])
            break
    else:
        print("Контакт не найден")


def read1(str):
    print(str)


def add(str):
    number_person = v.input_number()
    new_data = return_data().replace(str, str + " " + number_person)
    f = open('telef.txt', 'w')
    f.write(new_data)
    f.close
    print(new_data)


def delete(str):
    list_data = str.split()
    del list_data[1:]
    new_str = list_data[0] + ' delete'
    new_data = return_data().replace(str, new_str)
    f = open('telef.txt', 'w')
    f.write(new_data)
    f.close
    print(new_data)


def create():
    strings = return_data().split("\n")
    surname = v.input_surname()
    number_person = v.input_number()
    for i in range(0, len(strings)):
        if strings[i].find('delete') > 0:
            list_data = strings[i].split()
            new_str = (f'{list_data[0]} {surname} {number_person}')
            new_data = return_data().replace(strings[i], new_str)
            f = open('telef.txt', 'w')
            f.write(new_data)
            f.close
            break
    else:
        new_str = (f'\n{len(strings)+1} {surname} {number_person}')
        f = open('telef.txt', 'a')
        f.writelines(new_str)
        f.close
        print(new_str)


def return_data():
    f = open('telef.txt', 'r')
    data = f.read()
    f.close
    return data

# def add_contact():  # открыть файл, дописать В строку после телефона
#     f = open('telef.txt', 'r')
#     data = f.read()
#     f.close
#     strings = data.split("\n")
#     surname = v.input_surname()
#     for i in range(0, len(strings)):
#         if strings[i].find(surname) > 0:
#             number_person = v.input_number()
#             new_data = data.replace(
#                 strings[i], strings[i] + " " + number_person)
#             f = open('telef.txt', 'w')
#             data = f.write(new_data)
#             f.close
#             print(new_data)
#             break
#         else:
#             continue
#     else:
#         print("Контакт не найден")


# def read_contact():  # прочитать строку контакта
#     f = open('telef.txt', 'r')
#     data = f.read()
#     f.close
#     strings = data.split("\n")
#     surname = v.input_surname()
#     for i in range(0, len(strings)):
#         if strings[i].find(surname) > 0:
#             print(strings[i])
#             break
#         else:
#             continue
#     else:
#         print("Контакт не найден")
