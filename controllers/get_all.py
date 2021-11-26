def get_all(participants):
    print("-"*86)
    print("| {:<5} | {:<10} | {:<35} | {:<5} | {:<5} | {:<5}  |".format('Nº','Cedula','Nombre','Sexo','Edad','Tiempo'))
    print("-"*86)
    i = 0
    for participant in participants:
        i += 1
        print("| {:<5} | {:<10} | {:<35} | {:<5} | {:<5} | {:<5}|".format(i, participant.ci, participant.name(),participant.gender,participant.age,str(participant.time)))
        print("-"*86) 