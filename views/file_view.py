import sys
import time
from os import system
from exceptions.custom_file_exception import CustomFileException
from repositories.read_file import read_file

def file_view(participants):
    while True:
        print("""
        1. Cargar Archivo
        2. Volver

        0. Cerrar Sesión
        """)

        ans = input('Seleccione una opción: ')
        if ans == '1':
            system('cls')
            try:
                file_name = input('Introduce el nombre del archivo: ')
                participants = read_file(file_name)
                return participants
            except CustomFileException as e:
                print('Error: ', e)
                print('Porfavor intente nuevamente.', e)

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