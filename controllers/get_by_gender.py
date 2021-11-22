def get_by_gender(participants):
    m = 0
    f = 0
    for participant in participants:
        if participant.gender == 'M':
            m += 1
        elif participant.gender == 'F':
            f += 1
    print('Masculinos: ' + str(m))
    print('Femeninos:  ' + str(f))