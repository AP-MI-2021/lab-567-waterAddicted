from Tests.test_crud import test_crud
from UserInterface.console import run_ui

def main():
    obiecte = []
    obiecte = run_ui(obiecte)

if __name__=='__main__':
    test_crud()
    main()