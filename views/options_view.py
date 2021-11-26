import time
from os import system
from controllers.get_all import get_all
from controllers.get_participants_number import get_participants_numbers
from controllers.get_by_age_group import get_by_age_group
from controllers.get_by_gender import get_by_gender
from controllers.get_winner_by_age_group import get_winner_by_age_group
from controllers.get_winner_by_gender import get_winner_by_gender
from controllers.get_winner_by_age_group_and_sex import get_winner_by_age_group_and_sex
from controllers.get_winner import get_winner
from controllers.get_histograma import get_histograma

def options_view(participants):
    while True:
        system('cls')
        print("""
        1. Lista de participantes
        2. Cantidad de participantes
        3. Cantidad de participantes por grupo etario
        4. Cantidad de participantes por sexo
        5. Ganadores por grupo etario
        6. Ganadores por sexo
        7. Ganadores por grupo etario y sexo
        8. Ganador general
        9. Histograma de participantes por grupo etario

        0. Volver
        """)

        ans = input('Seleccione una opción: ')
        if ans == '1':
            system('cls')
            get_all(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '2':
            system('cls')
            get_participants_numbers(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '3':
            system('cls')
            get_by_age_group(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '4':
            system('cls')
            get_by_gender(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '5':
            system('cls')
            get_winner_by_age_group(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '6':
            system('cls')
            get_winner_by_gender(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '7':
            system('cls')
            get_winner_by_age_group_and_sex(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '8':
            system('cls')
            get_winner(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '9':
            system('cls')
            get_histograma(participants)
            print('\n\tPresione enter para continuar')
            skip = input()

        elif ans == '0':
            system('cls')
            break

        else:
            system('cls')
            print("\n Opción no válida, intente de nuevo")
            time.sleep(2)
            system('cls')