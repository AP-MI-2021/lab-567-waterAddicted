from Domain.inventar import get_locatie, creeaza_obiect, get_id, get_nume, get_descriere, get_pret


def change_location(lista: list, sursa: str, destinatie: str):
    """
    Muta obiectele dintr-o anumita locatie, intr-o alta locatie
    :param lista: lista ce contine obiectele
    :param sursa: locatia de unde vrem sa mutam
    :param destinatie: locatia unde vrem sa mutam
    :return: lista cu obiectele mutate din locatia sursa, in locatia destinatie
    """
    if sursa == '' or destinatie == '' or len(sursa) != 4 or len(destinatie) != 4:
        raise ValueError('Dati sursa si destinatia nenule, de exact 4 caractere')
    rezultat = []
    for element in lista:
        if get_locatie(element) != sursa:
            rezultat.append(element)
        else:
            id = get_id(element)
            nume = get_nume(element)
            descriere = get_descriere(element)
            pret_achizitie = get_pret(element)
            obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, destinatie)
            rezultat.append(obiect)
    return rezultat