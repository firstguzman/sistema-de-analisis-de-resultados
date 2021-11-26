import time
from os import system
from views.file_view import file_view
from views.options_view import options_view

# Este menú es nuestro menú principal el cual nos redirecciona a:
# el menu de archivos y al menu de acciones
def main_view():
    participants = []
    while True:
        system('cls')
        print("""
        SISTEMA DE ANALISIS DE RESULTADOS

        1. Archivo
        2. Acciones
        """)

        ans = input('\tSeleccione una opción: ')
        if ans == '1':
            system('cls')
            participants = file_view(participants)

        elif ans == '2':
            system('cls')
            options_view(participants)

        else:
            system('cls')
            print("\n\t\tOpción no válida, intente de nuevo")
            time.sleep(2)