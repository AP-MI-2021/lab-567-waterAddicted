from Domain.inventar import get_id
from Logic.crud import create
from Logic.ordonare import ordonare_obiecte


def test_ordonare():
    obiecte = []
    obiecte = create(obiecte, 1, 'a', 'aa', 111, 'aaa')
    obiecte = create(obiecte, 2, 'b', 'bb', 23, 'b')
    obiecte = create(obiecte, 3, 'c', 'cc', 333, 'aaa')
    obiecte = create(obiecte, 4, 'd', 'dd', 27, 'def')
    lst_ord = ordonare_obiecte(obiecte)

    assert get_id(lst_ord[0]) == 2
    assert get_id(lst_ord[1]) == 4
    assert get_id(lst_ord[2]) == 1
    assert get_id(lst_ord[3]) == 3
