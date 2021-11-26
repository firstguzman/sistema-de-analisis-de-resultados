from exceptions.custom_file_exception import CustomFileException
from repositories.participant import Participant

def read_file(file_name):
    if not file_name.endswith('.txt'):
        raise CustomFileException('Tipo de archivo incorrecto')

    participants = []
    with open (file_name) as f:
        for line in f:
            values = line.split(',')
            if not values.__len__() == 10:
                raise CustomFileException('Cantidad de columnas incorrectas')
            participant = Participant(
                int(values[0]),
                values[1],
                values[2],
                values[3],
                values[4],
                values[5],
                int(values[6]),
                int(values[7]),
                int(values[8]),
                int(values[9].replace('\n','')),
            )
            participants.append(participant)
    return participants