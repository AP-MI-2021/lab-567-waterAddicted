from Logic.crud import create
from Logic.locuri_distincte import loc_sep


def test_loc_sep():
    obiecte = []
    obiecte = create(obiecte, 1, 'a', 'aa', 1, 'aaa')
    obiecte = create(obiecte, 2, 'b', 'bb', 2, 'b')
    obiecte = create(obiecte, 3, 'c', 'cc', 3, 'aaa')
    obiecte = create(obiecte, 4, 'd', 'dd', 4, 'b')

    lst = loc_sep(obiecte)
    assert len(lst) == 2
    assert lst[0] == 'aaa'
    assert lst[1] == 'b'