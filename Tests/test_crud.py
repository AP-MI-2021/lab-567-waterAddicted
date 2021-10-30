from Domain.inventar import creeaza_obiect, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_obiect(1,'birou','foarte folositor si spatios',150,'CNTM'),
        creeaza_obiect(2, 'desc2', 'foarte folositor si spatios2', 152, 'CNTM'),
        creeaza_obiect(3, 'desc3', 'foarte folositor si spatios3', 153, 'CNTN'),
        creeaza_obiect(4, 'desc4', 'foarte folositor si spatios4', 154, 'CNTO'),
        creeaza_obiect(5, 'desc5', 'foarte folositor si spatios5', 155, 'CNTP'),
        creeaza_obiect(6, 'desc6', 'foarte folositor si spatios6', 156, 'CNTR')
    ]

def test_create():
    obiecte = get_data()
    params = (100,'pix','scrie albastru',2,'LTPM')
    o_new = creeaza_obiect(*params)
    new_obiecte = create(obiecte,*params)
    assert len(new_obiecte) == len(obiecte) + 1

    assert o_new in new_obiecte

def test_read():
    obiecte = get_data()
    some_o = obiecte[2]
    assert read(obiecte,get_id(some_o)) == some_o
    assert read(obiecte,None) == obiecte

def test_update():
    obiecte = get_data()
    o_updated = creeaza_obiect(1,'new name','new desc',111,'CLUJ')
    updated = update(obiecte,o_updated)
    assert o_updated in updated
    assert o_updated not in obiecte
    assert len(updated) == len(obiecte)

def test_delete():
    obiecte = get_data()
    to_delete = 3
    o_deleted = read(obiecte,to_delete)
    deleted = delete(obiecte,to_delete)
    assert o_deleted not in deleted
    assert o_deleted in obiecte
    assert len(deleted) == len(obiecte) - 1

def test_crud():
    test_create()
    test_read()