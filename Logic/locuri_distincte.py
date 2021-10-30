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
    for i in range(0,len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                if len(new_lst) > 0:
                    if ver_rep(new_lst,lst[i]):
                        new_lst.append(lst[i])

                else:
                    new_lst.append(lst[i])


    return new_lst
