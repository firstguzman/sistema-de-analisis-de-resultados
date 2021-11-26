def get_by_age_group(participants):
    juniors = 0
    masters = 0
    seniors = 0
    for participant in participants:
        if participant.age in range (1,26):
            juniors +=1
        elif participant.age in range(26, 41):
            masters +=1
        else:
            seniors +=1
    values = [['Juniors', juniors], ['Masters', masters], ['Seniors', seniors]]
    print("-"*26)
    print("| {:<5} | {:<5}|".format('Grupo Etario','Cantidad'))
    print("-"*26)
    i = 0
    for value in values:
        i += 1
        print("| {:<12} | {:<7} |".format(value[0], value[1]))
        print("-"*26) 