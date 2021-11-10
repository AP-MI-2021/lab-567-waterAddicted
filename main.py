from Tests.test_crud import test_crud
from Tests.test_locuri_dis import test_loc_sep
from Tests.test_modif import test_modif
from Tests.test_ordonare import test_ordonare
from Tests.test_undo_redo import test_undo_redo
from Tests.test_verificare_rep import test_ver_rep
from UserInterface.console import run_ui
from Logic.crud import create

def main():
    obiecte = []
    run_ui(obiecte)

if __name__=='__main__':
    test_crud()
    test_loc_sep()
    test_modif()
    test_ordonare()
    test_ver_rep()
    test_undo_redo()
    main()