def get_winner_by_age_group(participants):
    junior_winner_time = 0
    senior_winner_time = 0
    master_winner_time = 0
    junior_winner = []
    senior_winner = []
    master_winner = []
    for participant in participants:
        if participant.age in range (1,26):
            if junior_winner_time == 0:
                junior_winner_time = participant.time
                junior_winner.clear()
                junior_winner.append(participant)
            elif participant.time < junior_winner_time:
                junior_winner_time = participant.time
                junior_winner.clear()
                junior_winner.append(participant)
            elif participant.time == junior_winner_time:
                junior_winner.append(participant)
        elif participant.age in range(26, 41):
            if senior_winner_time == 0:
                senior_winner_time = participant.time
                senior_winner.clear()
                senior_winner.append(participant)
            elif participant.time < senior_winner_time:
                senior_winner_time = participant.time
                senior_winner.clear()
                senior_winner.append(participant)
            elif participant.time == senior_winner_time:
                senior_winner.append(participant)
        else:
            if master_winner_time == 0:
                master_winner_time = participant.time
                master_winner.clear()
                master_winner.append(participant)
            elif participant.time < master_winner_time:
                master_winner_time = participant.time
                master_winner.clear()
                master_winner.append(participant)
            elif participant.time == master_winner_time:
                master_winner.append(participant)
    win= [junior_winner, senior_winner, master_winner]
    winners = []
    for winner in win:
        for i in winner:
            winners.append(i)
    values = []
    for winner in winners:
        if winner.age in range (1,26):
            participant_details = ['Junior', winner.name(), winner.age, winner.time]
        elif winner.age in range(26, 41):
            participant_details = ['Senior', winner.name(), winner.age, winner.time]
        else:
            participant_details = ['Master', winner.name(), winner.age, winner.time]
        values.append(participant_details)
    
    print("-"*75)
    print("| {:^15} | {:^35} | {:^5} | {:^5}  |".format('Grupo Etario', 'Nombre','Edad','Tiempo'))
    print("-"*75)
    i = 0
    for value in values:
        i += 1
        print("| {:<15} | {:<35} | {:<5} | {:<5}|".format(value[0], value[1], value[2], str(value[3])))
        print("-"*75) 

    # print(tabulate(values, headers=['Grupo Etario', 'Nombre', 'Edad', 'Tiempo'], tablefmt='pretty'))