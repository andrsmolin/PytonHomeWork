import modul_use_telefone_book as mt
from modul_use_telefone_book import add, read1, delete
import preview as pr


def choise_type(type):
    if type == 1:
        return mt.contact(read1)
    elif type == 2:
        return mt.create()
    elif type == 3:
        return mt.contact(delete)
    elif type == 4:
        return mt.contact(add)
    elif type == 5:
        return pr.create()
