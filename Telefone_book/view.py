# type = ""
#surname = ""
# name = ""
# number = ""
# status = ""


def check_input(input_text):
    while True:
        number = input(f"{input_text}")
        if number.isdigit() and 1 <= int(number) <= 4:
            break
        else:
            print("Неверный ввод типа работы книги. Пожалуйста введите цифру от 1 до 4.")
    return int(number)


def start():
    # global type
    print("Выберите тип работы с телефонным справочником: ")
    print("1 - посмотреть контакт")
    print("2 - добавить новый контакт")
    print("3 - удалить контакт")
    print("4 - дополнить контакт")

    type = check_input("Тип работы: ")

    return type


def input_surname():  # метод просит ввести фамилию
    # global surname
    surname = input("Введите фамилию: ")
    return surname


def input_name():  # метод просит ввести имя
    # global name
    name = input("Введите имя: ")
    return name


def input_number():  # метод просит ввести номер
    # global number
    number = input("Введите номер телефона: ")
    return number


def input_status():  # метод просит ввести статус
    # global status
    status = input("Введите должность: ")
    return status
