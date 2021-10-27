from Domain2.inventar2 import creeaza_obiect
from Domain2.inventar2 import get_id

def create(lst_obiecte,id_obiect: int,nume,desccriere,pret,locatie):
    """
    Creeaza un obiect,cu campurile lui.
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului
    :param nume: numele obiectului
    :param desccriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia achizitionarii obiectului
    :return:lista initiala de obicete impreuna cu ultimul noul obiect adaugat
    """
    obiect = creeaza_obiect(id_obiect,nume,desccriere,pret,locatie)
    return lst_obiecte + [obiect]


def read(lst_obiecte,id_obiect:int = None):
    """
    Citeste un obiect din "baza de date".
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului dorit
    :return:
    """
    obiect_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_cu_id = obiect

    if obiect_cu_id:
        return obiect_cu_id
    return lst_obiecte

def delete(lst_obiecte,id_obiect: int):
    """
    Sterge din lista de obiecte un obiect cu un id dat.
    :param lst_obiecte: lsita de obiecte
    :param id_obiecte:  id-ul obiectului pe care vrem sa il stergem
    :return:  lsita cu cu obiecte fara elementul cu id-ul transmis prin parametru
    """
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != id_obiect:
            new_obiecte.append(obiect)

    return new_obiecte

def update(lst_obiecte,new_obiect):
    """
    Actualizeaza un obiect.
    :param lst_obiecte: lista de obiecte
    :param new_obiect:  obiectul care se va acutliza -id-ul trebuie sa fie unul existent
    :return: lista de obiecte actualizata
    """
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) == get_id(new_obiect):
            new_obiecte.append(new_obiect)

        else:
            new_obiecte.append(obiect)

    return new_obiecte
