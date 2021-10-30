def ver_rep(lst,val):
    '''
    Functia verifica daca intr-o lista NU s-a repetat o valoare.
    :param lst: lista data de numere
    :param val: valoare pe care o verificam daca s-a repetat
    :return: True daca valoarea nu s-a repetat sau False in caz contrat
    '''
    for i in range(len(lst)):
        if lst[i] == val:
            return False

    return True