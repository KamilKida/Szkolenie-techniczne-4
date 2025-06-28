from Decorators.LogDecorator import log_decorator 
from Classes.Menu import Menu as m
from StaticClass import BaseMethods as bs
import sys
import os




if __name__ == '__main__':

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'MetaClasses')))
    
    menu = m()

    menu.showStartMenu()

    if isinstance(menu.patient_list, Exception): 
        while True:
            bs.clearConsole()
            print("Podana ścieżka jest błędna lub plik .xlsx posiada błąd.\n" \
            "Aby spróbować ponownie, wpisz 1.\n" \
            "Aby zakończyć, wpisz dowolną wartość poza 1.\n")

            choice = input("Wybór: ")

            if choice == "1":
                menu.showStartMenu()
                if isinstance(menu.patient_list, Exception):
                    continue
                else:
                    menu.showMainMenu()
                    break
            else:
                break


    elif len(menu.patient_list) == 0:
        while True:
            bs.clearConsole()
            print("Podana ścieżka jest błędna lub plik .xlsx posiada błąd.\n" \
            "Aby spróbować ponownie, wpisz 1.\n" \
            "Aby zakończyć, wpisz dowolną wartość poza 1.\n\n")

            choice = input("Wybór: ")

            if choice == "1":
                menu.showStartMenu()
                if len(menu.patient_list) > 0:
                    menu.showMainMenu()
                    break
                else:
                    continue
            else:
                break
    else:
        menu.showMainMenu()

