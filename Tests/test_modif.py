from Domain.inventar import get_id, creeaza_obiect, get_nume, get_descriere, get_pret, get_locatie
from Logic.mdificare import modif
from Logic.crud import create

def test_modif():
    obiect_aux = creeaza_obiect(2,'b','bb',2,'bbb')
    modif(obiect_aux,'id',1)
    assert get_id(obiect_aux) == 1

    modif(obiect_aux,'nume','a')
    assert get_nume(obiect_aux) == 'a'

    modif(obiect_aux,'desc','aa')
    assert get_descriere(obiect_aux) == 'aa'

    modif(obiect_aux,'pret',1)
    assert get_pret(obiect_aux) == 1

    modif(obiect_aux,'locatie','aaa')
    assert get_locatie(obiect_aux) == 'aaa'