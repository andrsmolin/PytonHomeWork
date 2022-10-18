import view as v

id_person = ""
surname = ""
name_person = ""
number_person = ""
status_person = ""


def init(id, name, num, stat):
    global id_person
    global name_person
    global number_person
    global status_person
    id_person = id
    name_person = name
    number_person = num
    status_person = stat


def create_contact():
    # открыть файл, дописать строку, состоящую из номера контакта (id - придумать где хранить
    return 4
    # инфу), фио, номера, должности


def del_contact():
    # открыть файл, удалить строку и перенумеровать строки(? словарь)
    return 1


def add_contact():
    # открыть файл, дописать В строку после телефона
    return 2


def read_contact():  # прочитать строку контакта
    s_name = v.input_surname()
    f = open('telef.txt', 'r')
    for i in f:
        print(i)
    # data = f.read()
    f.close
    # for i in data:  # range(0, len.data):
    #     # if data[i] == s_name:
    #     # return 66
    #     print(i)
