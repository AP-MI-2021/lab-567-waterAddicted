from Domain.inventar import get_str, get_locatie, creeaza_obiect, get_pret, get_descriere
from Logic.change_location import change_location
from Logic.concatenare import concatenare
from Logic.crud import create, update, delete
from Logic.ordonare import ordonare_obiecte
from Logic.locuri_distincte import loc_sep
from Logic.mdificare import modif

def list_versions(versions_list, current_version, lista):
    versions_list.append(lista)
    current_version +=1
    return versions_list, current_version


def show_menu():
    '''
    Functia care afiseaza meniul pentru utilizator.
    '''
    print('2.1   CRUD.')
    print('2.2   Mutarea obiectelor dintr-o locatie data in alta.')
    print('2.3   Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.')
    print('2.4   Determinarea celui mai mare preț pentru fiecare locație.')
    print('2.5   Ordonarea obiectelor crescător după prețul de achiziție.')
    print('2.6   Afișarea sumelor prețurilor pentru fiecare locație.')
    print('2.7   Undo.')
    print('r     Redo.')
    print('a.    Afisare')
    print('x.    Exit.')

def handle_add(obiecte):
    '''
    Introduce un obiect inlista de obiecte.
    :param obiecte: lista de obiecte in care se aduaga obiecte
    :return: lista de obiecte in care se adauga noul obiect introdus de catre utilizator
    '''
    try:
        id_obiect = int(input('Dati id-ul obiectului:'))
        nume = input('Dati numele obiectului:')
        descriere = input('Dati descrierea obiectului:')
        pret = float(input('Dati pretul obiectului:'))
        locatie = input('Dati locatia obiectului formata din  exact 4 litere:')
        print('Adaugarea s-a efectuat cu succes!')
        return create(obiecte,id_obiect,nume,descriere,pret,locatie)
    except ValueError as ve:
        print('Erorare:', ve)
    return obiecte

def handle_show_all(obiecte):
    '''
    Afisarea tuturor obiectelor din lista de obiecte.
    :param obiecte: lista de biecte
    :return:
    '''
    for obiect in obiecte:
        print(get_str(obiect))


def handle_modify(obiecte):
    '''
    Da update unui obiect existent in lista, care este ales de catre utilizator dupa id-ul acestuia.
    :param obiecte: lista de obiecte
    :return: lista de obiecte cu un anumit element modificat
    '''
    try:
        id_obiect = int(input('Dati id-ul obiectului care se actualizeaza:'))
        nume = input('Dati noul nume al obiectului:')
        descriere = input('Dati noua descrierea a obiectului:')
        pret = float(input('Dati noul pret al obiectului:'))
        locatie = input('Dati noua locatie a obiectului formata din  exact 4 litere:')
        print(f'Modificarea obiectului cu id-ul: {id_obiect},s-a efectuat succes!')
        return update(obiecte,creeaza_obiect(id_obiect,nume,descriere,pret,locatie))
    except ValueError as ve:
        print('Eroare:',ve)

def handle_delete(obiecte):
    '''
    Sterge un anumit obiect extent in lista,dupa id-ul acestuia.
    :param obiecte: lista de obiecte
    :return: lista de obiecte construita prin excluderea elementului sters
    '''
    try:
        id_obiect = int(input('Dati id-ul obiectului care se va sterge:'))
        print(f'Stergerea obiectului cu id-ul: {id_obiect},s-a efectuat cu succes!')
        return delete(obiecte,id_obiect)
    except ValueError as ve:
        print('Eroare',ve)


def handle_crud(obiecte,versions_list, current_version):
    '''
    Submeniu pentru operarea calculelor CRUD.
    :param obiecte: lista de  obiecte
    :return:se va returna in cazul in care utilizatorul selecteaza optounea 'b' ,lista de obiecte modificata de operatiile CRUD
    '''
    while True:
        print('1.   Adaugare.')
        print('2.   Modificare.')
        print('3.   Stergere.')
        print('a.   Afisare.')
        print('b.   Revenire.')

        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            obiecte = handle_add(obiecte)
            versions_list, current_version = list_versions(versions_list, current_version, obiecte)
        elif optiune == '2':
            obiecte = handle_modify(obiecte)
            versions_list, current_version = list_versions(versions_list, current_version, obiecte)
        elif optiune == '3':
            obiecte =handle_delete(obiecte)
            versions_list, current_version = list_versions(versions_list, current_version, obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'b':
            return obiecte,versions_list,current_version
        else:
            print('Optiune invalida.')


def handle_mutare_obicete_din_loc_in_altul(obiecte,fosta_loc,noua_loc):
    '''
    Muta toate obiectele dintr-un loc existent in care se afla obiectele(introsdus de utilizator) in unul nou(introdus de utilizator).
    :param obiecte:  lista de obiecte
    :param fosta_loc:   locatia initiala a obiectelor care vor fi mutate in alta locatie
    :param noua_loc:    locatia noua in care vor fi mutate toate
    :return:
    '''
    try:
        return change_location(obiecte, fosta_loc, noua_loc)
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def handle_concatenare_descriere(obiecte, pretul, str):
    '''

    :param obiecte: lista de obiecte
    :param pretul: pretul pe care obiectele trebuie sa il depaseasca ca sa primeasca descrierea furnizata de catre utilizator.
    :param str: adaosul din descriere(introdus de utilizator) care se va aplica pentru obiectele are  caror pret depsasesc pretul introdus de utilizator
    :return:lista  modificata dupa criteriul de mai sus(adaosul in descriere de text venit din partea utilizatorului)
    '''
    return concatenare(obiecte, str, pretul)


def handle_cel_mai_mare_pret_din_ficare_loc(obiecte):
    '''
    O sa calculeze cel mai mai mare pret din fiecare locatie.
    :param obiecte: lista de obiecte
    :return:
    '''
    lst = loc_sep(obiecte)
    print(lst)
    for i in lst:
        p_maxim = -1
        for obiect in obiecte:
            if get_locatie(obiect) == i:
                if p_maxim<get_pret(obiect):
                    p_maxim= get_pret(obiect)

        print(f'Pretul cel mai mare din {i} este {p_maxim}')


def handle_ordonare_cresc_dupa_pret(obiecte):
    '''
    Ordoneaza crescator lista de obiecte in functie de pretul acestora
    :param obiecte: lista de obiecte
    :return: lista de obiecte ordonata crscator in functie de pretul obiectelor
    '''
    return ordonare_obiecte(obiecte)


def handle_afisare_sum_pret_loc(obiecte):
    '''
    Afiseaza suma preturilor obiectelor din fiecare loc.
    :param obiecte: lista de obiecte.
    :return:
    '''
    lst = loc_sep(obiecte)
    for i in lst:
        suma = 0
        for obiect in obiecte:
            if get_locatie(obiect) == i:
                suma = suma + get_pret(obiect)

        print(f'Suma tutror obiectelor din zona {i} este {suma}')



def handle_undo(list_versions, current_version):
    if current_version < 0:
        raise ValueError("Can't undo anymore!")
    return list_versions[current_version]


def handle_redo(current_version,list_versions):
    if current_version == len(list_versions) :
        raise ValueError("You're running on the latest version.")
    return list_versions[current_version]


def run_ui(obiecte):
    '''
    Opereaza mediul principal de optiuni pentru utilizator.
    :param obiecte:lista de obiecte
    :return:
    '''
    versions_list = [obiecte]
    current_version = 0
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '2.1':
            obiecte,versions_list,current_version = handle_crud(obiecte,versions_list,current_version)
        elif optiune == '2.2':
            fosta_loc = input('Introduceti fosta locatie :')
            noua_loc = input('Introduceti noua locatie formata din  exact 4 litere:')
            obiecte = handle_mutare_obicete_din_loc_in_altul(obiecte,fosta_loc,noua_loc)
            versions_list,current_version = list_versions(versions_list,current_version,obiecte)
            print(f'Toate obiectele care se afla in locatia {fosta_loc} au fost mutate cu succes in locatia {noua_loc}!')
        elif optiune =='2.3':
            try:
                pretul = float(input('Intorduceti pretul pentru care pretul obiectelor trebuie sa fie mai mare ca sa primeasca o anumta descriere:'))
                str = input(f'Introduceti descrierea care se va adauga tuturor obiectelor a caror pret depaseste {pretul} : ')
                obiecte = handle_concatenare_descriere(obiecte,pretul,str)
                print(f'Descirearea " {str} "a fost adaugata cu succes tuturor obiectelora caror pret este mai mare decat {pretul}!')
                versions_list, current_version = list_versions(versions_list, current_version, obiecte)
            except ValueError as ve:
                print('Eroare!',ve)
        elif optiune == '2.4':
            handle_cel_mai_mare_pret_din_ficare_loc(obiecte)
        elif optiune == '2.5':
            obiecte = handle_ordonare_cresc_dupa_pret(obiecte)
            versions_list, current_version = list_versions(versions_list, current_version, obiecte)
            print('Ordonarea obiectelor in functie de pret a avut loc cu succes.')
        elif optiune == '2.6':
            handle_afisare_sum_pret_loc(obiecte)
        elif optiune == '2.7':
            try:
                current_version -= 1
                obiecte = handle_undo(versions_list, current_version)
                print("Undo!")
            except ValueError as ve:
                current_version += 1
                print("Error:", ve)
        elif optiune == 'r':
            try:
                current_version += 1
                obiecte = handle_redo(current_version, versions_list)
            except ValueError as ve:
                current_version -= 1
                print("Error:", ve)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')