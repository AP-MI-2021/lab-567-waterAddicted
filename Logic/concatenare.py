from Domain.inventar import get_pret, get_id, get_nume, get_descriere, creeaza_obiect, get_locatie


def concatenare_string(element1: str, element2: str):
    """
    Comcateneaza doua stringuri
    :param element1: string 1
    :param element2: strung 2
    :return: concatenarea element1 si element2
    """
    return element1 + element2


def concatenare(lista: list, string_citit: str, pret: float):
    """
    Concateneaza un string citit la descrierea obiectelor din lista care au un pret mai mare decat unul dat
    :param lista: lista de obiecte
    :param string_citit: stringul de concatenat la descriere
    :param pret: pretul dat
    :return: noua lista in care elementele cu un pret mai mare decat pret au concatenat la descriere string_citit
    """
    if type(pret) is not float:
        raise ValueError('Dati pretul un numar!')
    rezultat = []
    for element in lista:
        if get_pret(element) <= pret:
            rezultat.append(element)
        else:
            id = get_id(element)
            nume = get_nume(element)
            descriere = concatenare_string(get_descriere(element), string_citit)
            pret_achizitie = get_pret(element)
            locatie = get_locatie(element)
            obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
            rezultat.append(obiect)
    return rezultat