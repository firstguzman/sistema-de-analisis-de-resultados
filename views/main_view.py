import time
from os import system
from views.file_view import file_view
from views.options_view import options_view

def main_view():
    while True:
        print("""
        1. Archivo
        2. Acciones

        """)

        ans = input('Seleccione una opción: ')
        if ans == '1':
            system('cls')
            file_view()

        elif ans == '2':
            system('cls')
            options_view()

        else:
            system('cls')
            print("\n Opción no válida, intente de nuevo")
            time.sleep(2)
            system('cls')