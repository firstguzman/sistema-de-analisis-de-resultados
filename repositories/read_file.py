from repositories.participant import Participant

def read_file(participants):
    with open ("competencia.txt") as f:
        for line in f:
            values = line.split(',')
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