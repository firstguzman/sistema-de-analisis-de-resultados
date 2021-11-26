def get_winner_by_gender(participants):
    m_winner_time = 0
    f_winner_time = 0
    m_winner = []
    f_winner = []
    for participant in participants:
        if participant.gender == 'M':
            if m_winner_time == 0:
                m_winner_time = participant.time
                m_winner.clear()
                m_winner.append(participant)
            elif participant.time < m_winner_time:
                m_winner_time = participant.time
                m_winner.clear()
                m_winner.append(participant)
            elif participant.time == m_winner_time:
                m_winner.append(participant)
        elif participant.gender == 'F':
            if f_winner_time == 0:
                f_winner_time = participant.time
                f_winner.clear()
                f_winner.append(participant)
            elif participant.time < f_winner_time:
                f_winner_time = participant.time
                f_winner.clear()
                f_winner.append(participant)
            elif participant.time == f_winner_time:
                f_winner.append(participant)
    win= [m_winner, f_winner]
    winners = []
    for winner in win:
        for i in winner:
            winners.append(i)
    values = []
    for winner in winners:
        if winner.gender == 'M':
            participant_details = ['Masculino', winner.name(), winner.age, winner.time]
        elif winner.gender == 'F':
            participant_details = ['Femenino', winner.name(), winner.age, winner.time]
        values.append(participant_details)
    print("-"*70)
    print("| {:^10} | {:^35} | {:^5} | {:^5}  |".format('Genero', 'Nombre','Edad','Tiempo'))
    print("-"*70)
    i = 0
    for value in values:
        i += 1
        print("| {:<10} | {:<35} | {:<5} | {:<5}|".format(value[0], value[1], value[2], str(value[3])))
        print("-"*70) 