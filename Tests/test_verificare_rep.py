from Logic.verifacre_repetare import ver_rep


def test_ver_rep():
    list1 = [1,2,3]
    ver_list1 = ver_rep(list1,2)
    ver_list2 = ver_rep(list1,4)

    assert ver_list1 == False
    assert ver_list2 == True