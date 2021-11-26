def get_winner(participants):
    winner_time = 0
    winner = []
    for participant in participants:
        if winner_time == 0:
            winner_time = participant.time
            winner.clear()
            winner.append(participant)
        elif participant.time < winner_time:
            winner_time = participant.time
            winner.clear()
            winner.append(participant)
        elif participant.time == winner_time:
            winner.append(participant)
    values = []
    for w in winner:
        participant_details = [w.name(), w.age, w.time]
        values.append(participant_details)

    print("-"*57)
    print("| {:^53} |".format('FELICIDADES GANADOR'))
    print("-"*57)
    print("| {:^35} | {:^5} | {:^5}  |".format('Nombre','Edad','Tiempo'))
    print("-"*57)
    i = 0
    for value in values:
        i += 1
        print("| {:^35} | {:^5} | {:^5}|".format(value[0], value[1], str(value[2])))
        print("-"*57) 