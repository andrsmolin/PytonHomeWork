import modul_use_telefone_book as mt
from modul_use_telefone_book import add, read, delete
import preview as pr

msg = ""


def init(msg1):
    global msg
    msg = msg1


def choise_type(msg1):

    # global msg
    if msg1 == 1:
        return mt.read()
    elif msg1 == 2:
        return mt.create()
    elif msg1 == 3:
        return mt.delete()
    elif msg1 == 4:
        return mt.add()
    elif msg1 == 5:
        return pr.create()


def check_input(msg1):
    # global msg
    return msg1.isdigit() and 1 <= int(msg1) <= 5
