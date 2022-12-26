import random 

while True: 
    choice = ['rock','paper','scissors']
    computer = random.choice(choice)
    
    player = None
    while player not in choice:
        player = input('paper, rock or scissors ?: ').lower()
    
    if player == computer:
        print(f'computer : {computer}')
        print(f'player : {player}')
        print('Tie!')
    
    elif player == 'rock':
        if computer == 'paper':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You lost!')
        elif computer == 'scissors':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You won!')          
    elif player == 'paper':
        if computer == 'scissors':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You lost!')
        elif computer == 'rock':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You won!')
    elif player == 'scissors':
        if computer == 'rock':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You lost!')
        elif computer == 'paper':
            print(f'computer : {computer}')
            print(f'player : {player}')
            print('You won!')

    play_again = input('Do you want to play again (yes/no) ?').lower()
    if play_again != 'yes':
        break
