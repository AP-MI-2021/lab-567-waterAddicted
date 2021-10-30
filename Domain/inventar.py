def creeaza_obiect(id_obicet: int,nume,descriere,pret,locatie):
    """
    Creeaza o achizitie
    :param id_obicet:id-ul obicetului trebuie sa fie unic
    :param nume:numele obiectului ,nenul
    :param descriere:descrierea obiectului ,nenul
    :param pret:pretul obiectului
    :param locatie:locatia achizitionarii obiectului ,exact 4 caractere
    :return:
    """
    return {
        'id' : id_obicet,
        'nume': nume,
        'desc': descriere,
        'pret': pret,
        'locatie': locatie,
    }

def get_id(obicet):
    """
    Getter pentru id-ul obieectului.
    :param obicet: obiectul
    :return: id-ul obiectului
    """
    return obicet['id']

def get_nume(obiect):
    """
    Getter pentru numele obicetului.
    :param obiect: obiectul
    :return: numele obiectului
    """
    return obiect['nume']

def get_descriere(obiect):
    """
    Getter pentru descrierea obiectului.
    :param obiect: obiectul
    :return: descrierea obiectului
    """
    return obiect['desc']

def get_pret(obiect):
    """
    Getter pentru descrierea obiectului.
    :param obiect: obiectul
    :return: descrierea obiectului
    """
    return obiect['pret']


def get_locatie(obiect):
    """
    Getter pentru locatia obiectului.
    :param obiect: obiectul
    :return: locatia de unde a fost achizat obiectul.
    """
    return obiect['locatie']

def get_str(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)}, denumit {get_nume(obiect)}, cu descrierea {get_descriere(obiect)},care costa {get_pret(obiect)},avand locul achiztionarii {get_locatie(obiect)}'






