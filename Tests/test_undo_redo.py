from Domain.inventar import creeaza_obiect
from UserInterface.console import handle_undo, handle_redo, list_versions
from Domain.inventar import *
from Logic.crud import create

def test_undo_redo():
    obiecte = []
    versions_list = [obiecte]
    current_version = 0
    obiecte = create(obiecte, 1, 'a', 'aa', 111, 'aaaa')
    versions_list, current_version = list_versions(versions_list, current_version, obiecte)
    obiecte = create(obiecte, 2, 'b', 'bb', 23, 'b')
    versions_list, current_version = list_versions(versions_list, current_version, obiecte)
    obiecte = create(obiecte, 3, 'c', 'cc', 333, 'aaaa')
    versions_list, current_version = list_versions(versions_list, current_version, obiecte)
    obiecte = create(obiecte, 4, 'd', 'dd', 27, 'deff')
    versions_list, current_version = list_versions(versions_list, current_version, obiecte)
    try:
        current_version -= 1
        obiecte = handle_undo(versions_list, current_version)
    except ValueError as ve:
        current_version += 1
        print("Error:", ve)
    assert get_id(obiecte[len(obiecte)-1]) == 3
    assert get_nume(obiecte[len(obiecte) - 1]) == 'c'
    assert get_descriere(obiecte[len(obiecte) - 1]) == 'cc'
    assert get_pret(obiecte[len(obiecte) - 1]) == 333
    assert get_locatie(obiecte[len(obiecte) - 1]) == 'aaaa'

    try:
        current_version += 1
        obiecte = handle_redo(current_version, versions_list)
    except ValueError as ve:
        current_version -= 1
        print("Error:", ve)

    assert get_id(obiecte[len(obiecte)-1]) == 4
    assert get_nume(obiecte[len(obiecte) - 1]) == 'd'
    assert get_descriere(obiecte[len(obiecte) - 1]) == 'dd'
    assert get_pret(obiecte[len(obiecte) - 1]) == 27
    assert get_locatie(obiecte[len(obiecte) - 1]) == 'deff'



