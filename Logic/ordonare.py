def ordonare_obiecte(lista):
    '''
    Ordoneaza crescator obiecte din inventar in functie de pret.
    :param lista: lista de obiecte
    :return: lista sortata dupa valoarea pretului
    '''
    return sorted(lista, key= lambda x:x["pret"])