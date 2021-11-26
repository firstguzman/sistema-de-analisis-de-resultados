import sys
import time
from os import system
from repositories.read_file import read_file

def file_view(participants):
    while True:
        print("""
        1. Cargar Archivo

        0. Cerrar Sesión
        """)

        ans = input('Seleccione una opción: ')
        if ans == '1':
            system('cls')
            participants = read_file(participants)
            return participants

        # elif ans == '2':
        #     system('cls')
        #     break

        elif ans == '0':
            system('cls')
            print('Adios..')
            time.sleep(1)
            sys.exit()

        else:
            system('cls')
            print("\n Opción no válida, intente de nuevo")
            time.sleep(2)
            system('cls')