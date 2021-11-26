def get_histograma(participants):
    juniors = ''
    masters = ''
    seniors = ''
    icon = '*'
    for participant in participants:
        if participant.age in range (1,26):
            juniors = juniors + icon
        elif participant.age in range(26, 41):
            masters = masters + icon
        else:
            seniors = seniors + icon 
    print('HISTOGRAMA\n')
    print('Juniors (x): | ' + juniors)
    print('Masters (y): | ' + masters)
    print('Seniors (z): | ' + seniors)