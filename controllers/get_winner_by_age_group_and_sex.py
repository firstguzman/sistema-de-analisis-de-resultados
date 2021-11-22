def get_winner_by_age_group_and_sex(participants):
    juniorm_winner_time = 0
    juniorf_winner_time = 0
    seniorm_winner_time = 0
    seniorf_winner_time = 0
    masterm_winner_time = 0
    masterf_winner_time = 0
    juniorm_winner = []
    juniorf_winner = []
    seniorm_winner = []
    seniorf_winner = []
    masterm_winner = []
    masterf_winner = []
    for participant in participants:
        if participant.age in range (1,26) and participant.gender == 'M':
            if juniorm_winner_time == 0:
                juniorm_winner_time = participant.time
                juniorm_winner.clear()
                juniorm_winner.append(participant)
            elif participant.time < juniorm_winner_time:
                juniorm_winner_time = participant.time
                juniorm_winner.clear()
                juniorm_winner.append(participant)
            elif participant.time == juniorm_winner_time:
                juniorm_winner.append(participant)
        elif participant.age in range(26, 41) and participant.gender == 'M':
            if seniorm_winner_time == 0:
                seniorm_winner_time = participant.time
                seniorm_winner.clear()
                seniorm_winner.append(participant)
            elif participant.time < seniorm_winner_time:
                seniorm_winner_time = participant.time
                seniorm_winner.clear()
                seniorm_winner.append(participant)
            elif participant.time == seniorm_winner_time:
                seniorm_winner.append(participant)
        elif participant.gender == 'M':
            if masterm_winner_time == 0:
                masterm_winner_time = participant.time
                masterm_winner.clear()
                masterm_winner.append(participant)
            elif participant.time < masterm_winner_time:
                masterm_winner_time = participant.time
                masterm_winner.clear()
                masterm_winner.append(participant)
            elif participant.time == masterm_winner_time:
                masterm_winner.append(participant)
        elif participant.age in range (1,26) and participant.gender == 'F':
            if juniorf_winner_time == 0:
                juniorf_winner_time = participant.time
                juniorf_winner.clear()
                juniorf_winner.append(participant)
            elif participant.time < juniorf_winner_time:
                juniorf_winner_time = participant.time
                juniorf_winner.clear()
                juniorf_winner.append(participant)
            elif participant.time == juniorf_winner_time:
                juniorf_winner.append(participant)
        elif participant.age in range(26, 41) and participant.gender == 'F':
            if seniorf_winner_time == 0:
                seniorf_winner_time = participant.time
                seniorf_winner.clear()
                seniorf_winner.append(participant)
            elif participant.time < seniorf_winner_time:
                seniorf_winner_time = participant.time
                seniorf_winner.clear()
                seniorf_winner.append(participant)
            elif participant.time == seniorf_winner_time:
                seniorf_winner.append(participant)
        elif participant.gender == 'F':
            if masterf_winner_time == 0:
                masterf_winner_time = participant.time
                masterf_winner.clear()
                masterf_winner.append(participant)
            elif participant.time < masterf_winner_time:
                masterf_winner_time = participant.time
                masterf_winner.clear()
                masterf_winner.append(participant)
            elif participant.time == masterf_winner_time:
                masterf_winner.append(participant)
    win= [juniorm_winner, juniorf_winner, seniorm_winner, seniorf_winner, masterm_winner, masterf_winner]
    winners = []
    for winner in win:
        for i in winner:
            winners.append(i)
    values = []
    for winner in winners:
        if winner.age in range (1,26) and winner.gender == 'M':
            participant_details = ['Junior', winner.gender, winner.name(), winner.age, winner.time]
        elif winner.age in range(26, 41) and winner.gender == 'M':
            participant_details = ['Senior', winner.gender, winner.name(), winner.age, winner.time]
        elif winner.gender == 'M':
            participant_details = ['Master', winner.gender, winner.name(), winner.age, winner.time]
        elif winner.age in range (1,26) and winner.gender == 'F':
            participant_details = ['Junior', winner.gender, winner.name(), winner.age, winner.time]
        elif winner.age in range(26, 41) and winner.gender == 'F':
            participant_details = ['Senior', winner.gender, winner.name(), winner.age, winner.time]
        elif winner.gender == 'F':
            participant_details = ['Master', winner.gender, winner.name(), winner.age, winner.time]
        values.append(participant_details)

    print(values)
    print("-"*84)
    print("| {:^15} | {:^6} | {:^35} | {:^5} | {:^5}  |".format('Grupo Etario', 'Genero', 'Nombre','Edad','Tiempo'))
    print("-"*84)
    for value in values:
        print("| {:^15} | {:^6} | {:^35} | {:^5} | {:^5}|".format(value[0], value[1], value[2], value[3], str(value[4])))
        print("-"*84) 