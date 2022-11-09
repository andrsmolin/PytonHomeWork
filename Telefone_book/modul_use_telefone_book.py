# from os import statvfs_result
# from unicodedata import name
import view as v
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# async def run_choise(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     global msg
#     msg = update.message.text
#     # c.init(msg)
#     if c.check_input(msg):
#         c.choise_type(int(msg))
#     else:
#         await update.message.reply_text(f'{update.effective_user.first_name}, неверный ввод')


def read():
    tel_dect = return_data()
    surname = v.input_surname()
    count = 0
    for i in range(1, len(tel_dect)+1):
        if tel_dect[i]['surname'].find(surname) > 0:
            print(tel_dect[i])  # ['surname']['name']['telefon']['status'])
            count += 1
    else:
        if count == 0:
            print("Контакт не найден")


def delete():
    idd = int(v.input_id())
    tel_dect = return_data()
    tel_dect[idd] = {'idd': idd, 'surname': 'delete',
                     'name': 'delete', 'telefon': '_', 'status': '_'}
    exp_dect(tel_dect)


def create():
    tel_dect = return_data()
    surname = v.input_surname()
    name = v.input_name()
    number_person = v.input_number()
    status = v.input_status()
    i = len(tel_dect)+1
    tel_dect[i] = {'idd': i, 'surname': surname, 'name': name,
                   'telefon': number_person, 'status': status}
    exp_dect(dict(tel_dect))
    print(tel_dect[i])


def add():
    tel_dect = return_data()
    surname = v.input_surname()
    name = v.input_name()
    number_person = v.input_number()
    status = v.input_status()
    i = len(tel_dect)+1
    tel_dect[i] = {'idd': i, 'surname': surname, 'name': name,
                   'telefon': number_person, 'status': status}
    exp_dect(dict(tel_dect))
    print(tel_dect[i])


def return_data():
    imp_dect = {}
    with open("C:/e/tel.txt", 'r', encoding='utf-8') as f:
        for line in f:
            key, sur, nam, tel, stat_ = line.split()
            imp_dect[int(key)] = {'idd': key, 'surname': sur,
                                  'name': nam, 'telefon': tel, 'status': stat_}
    return imp_dect


def exp_dect(tel_dect):
    f = open('C:/e/tel.txt', 'w', encoding='utf-8')
    for i in range(1, len(tel_dect)+1):
        f.write(str(tel_dect[i]['idd']) + '  ')
        f.write(tel_dect[i]['surname'] + ' ')
        f.write(tel_dect[i]['name'] + ' ')
        f.write(tel_dect[i]['telefon'] + ' ')
        f.write(tel_dect[i]['status'] + '\n')
        # print(tel_dect[i]['name'], tel_dect[i]['surname'], tel_dect[i]['telefon'])
    f.close()


tel_dect = {}
