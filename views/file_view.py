import sys
import time
from os import system

def file_view():
    while True:
        print("""
        1. Cargar Archivo
        2. Volver

        0. Cerrar Sesión
        """)

        ans = input('Seleccione una opción: ')
        if ans == '1':
            system('cls')
            'Cargando archivo'

        elif ans == '2':
            system('cls')
            break

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