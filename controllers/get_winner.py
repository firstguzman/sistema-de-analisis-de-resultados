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
        participant_details = [w.name(), w.time]
        values.append(participant_details)


    print('FELICIDADES\n')
    for value in values:
        print(value[0] + ' Obtuvo el menor tiempo de toda la competencia: ' + str(value[1]))