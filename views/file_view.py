import sys
import time
from os import system
from exceptions.custom_file_exception import CustomFileException
from repositories.read_file import read_file

# La siguiente vista contiene las opciones para trabajar con los archivos.
# A través de esta vista se puede: Cargar el archivo, volver al menú anterior
# y cerrar el sisteme
def file_view(participants):
    while True:
        system('cls')
        print("""
        1. Cargar Archivo
        2. Volver

        0. Cerrar Sesión
        """)

        ans = input('\tSeleccione una opción: ')
        if ans == '1':
            system('cls')
            try:
                file_name = input('\tIntroduce el nombre del archivo: ')
                participants = read_file(file_name)
                print('\n\t\tArchivo cargado satifactoriamente')
                print('\n\tPresione enter para continuar')
                skip = input()
                return participants
            except CustomFileException as e:
                print('\n\t\tError: ', e)
                print('\t\tPorfavor intente nuevamente.')
                print('\n\tPresione enter para continuar')
                skip = input()
        elif ans == '2':
            break

        elif ans == '0':
            system('cls')
            print('\t\tCerrando sesión. Nos vemos pronto..')
            time.sleep(1)
            sys.exit()

        else:
            system('cls')
            print("\n\t\tOpción no válida, intente de nuevo")
            time.sleep(2)
            system('cls')