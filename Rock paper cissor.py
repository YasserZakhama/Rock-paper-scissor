import random
while True:
    yes_no=['yes','no']
    choices = ['rock','paper','scissors']
    computer = random.choice(choices)
    player = None

    player = input('choose= rock, paper, scissors : ').lower()
    
    while player not in choices:
        player = input('oooo tchnouwa tww tnarvznich 3aawed akthar haja mn hadhom(rock, paper, scissors): ').lower()

    if player == computer:
        print('computer:', computer)
        print('player:', player)
        print('Ta3adelt maa 3amek lbot')

    elif player == 'rock':
        if computer == 'paper':
            print('computer:', computer)
            print('player:', player)
            print('ahah hak khsaret')
        if computer == 'scissors':
            print('computer:', computer)
            print('player:', player)
            print('good jooob <3')

    elif player == 'paper':
        if computer == 'rock':
            print('computer:', computer)
            print('player:', player)
            print('good jooob <3')
        if computer == 'scissors':
            print('computer:', computer)
            print('player:', player)
            print('ahah hak khsaret')

    elif player == 'scissors':
        if computer == 'paper':
            print('computer:', computer)
            print('player:', player)
            print('good jooob <3')
        if computer == 'rock':
            print('computer:', computer)
            print('player:', player)
            print('ahah hak khsaret')

    play_again = input('Play again? (yes/no):').lower()
    while play_again not in yes_no:
    	 play_again = input('Play again? (yes/no):').lower()
    if play_again != 'yes':
        break

print('Hayy tarter tarter')