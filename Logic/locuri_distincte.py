from Logic.verifacre_repetare import ver_rep
from Domain.inventar import get_locatie

def loc_sep(obiecte):
    '''
    Returneaza o lista de locatii distincte.
    :param obiecte: lista de obiecte
    :return: o lista cu locatii diferite in care se afla obiectele
    '''
    lst = []
    for obiect in obiecte:
        lst.append(get_locatie(obiect))
    new_lst = []
    for i in lst:
        if len(new_lst) == 0:
            new_lst.append(i)
        elif ver_rep(new_lst,i):
            new_lst.append(i)



    return new_lst
