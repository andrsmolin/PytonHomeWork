from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


def check_input(input_text):
    while True:
        number = input(f"{input_text}")
        if number.isdigit() and 1 <= int(number) <= 5:
            break
        else:
            print("Неверный ввод типа работы книги. Пожалуйста введите цифру от 1 до 5.")
    return int(number)


def start():
    # return
    data = "Выберите тип работы с телефонным справочником:\n /1 - посмотреть контакт \n /2 - добавить новый контакт \n /3 - удалить контакт \n"

    # type = check_input("Тип работы: ")

    return data


def input_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = update.message.text
    update.message.reply_text(f'{surname}, невод')
    # surname = input("Введите фамилию: ")
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
