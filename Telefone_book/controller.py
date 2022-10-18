import modul_use_telefone_book as mt
import view as v


def choise_type(type):
    if type == 1:
        return mt.read_contact()
    elif type == 2:
        return mt.create_contact()
    elif type == 3:
        return mt.del_contact()
    elif type == 4:
        return mt.add_contact()
