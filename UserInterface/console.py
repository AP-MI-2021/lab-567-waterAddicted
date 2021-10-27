from Domain.inventar import get_str, get_locatie, modif, creeaza_obiect
from Logic.crud import create, update, delete


def show_menu():
    print('2.1   CRUD.')
    print('a.    Afisare.')
    print ('x.    Exit.')

def handle_add(obiecte):
    id_obiect = int(input('Dati id-ul obiectului.'))
    nume = input('Dati numele obiectului.')
    descriere = input('Dati descrierea obiectului.')
    pret = int(input('Dati pretul obiectului.'))
    locatie = input('Dati locatia obiectului obiectului.')
    return create(obiecte,id_obiect,nume,descriere,pret,locatie)


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_str(obiect))


def handle_modify(obiecte):
    id_obiect = int(input('Dati id-ul obiectului care se actualizeaza.'))
    nume = input('Dati noul nume al obiectului.')
    descriere = input('Dati noua descrierea a obiectului.')
    pret = float(input('Dati noul pret al obiectului.'))
    locatie = input('Dati noua locatie a obiectului.')
    return update(obiecte,creeaza_obiect(id_obiect,nume,descriere,pret,locatie))

def handle_delete(obiecte):
    id_obiect = int(input('Dati id-ul obiectului care se va sterge:'))
    return delete(obiecte,id_obiect)



def handle_crud(obiecte):
    while True:
        print('1.   Adaugare.')
        print('2.   Modificare.')
        print('3.   Stergere.')
        print('a.   Afisare.')
        print('b.   Revenire.')

        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            obiecte = handle_modify(obiecte)
        elif optiune == '3':
            obiecte =handle_delete(obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'b':
            return obiecte
        else:
            print('Optiune invalida.')


def handle_mutare_obicete_din_loc_in_altul(obiecte,fosta_loc,noua_loc):
    for obiect in obiecte:
        if get_locatie(obiect) == fosta_loc:
            modif(obiect,'locatie',noua_loc)




def run_ui(obiecte):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '2.1':
            obiecte = handle_crud(obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')