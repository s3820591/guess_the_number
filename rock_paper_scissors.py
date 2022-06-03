import random

arr = ['r', 'p', 's']
def game():
    player = ''
    print('Welcome to rock, paper, scissors game!!!')
    while player != 'e':
        player = input('What is your choice: rock(r), paper(p), scissors(s): ')
        computer = random.choice(arr)
        print(f'Computer chose :{computer}')

        if player == computer:
            print('You tie') 

        elif is_win(computer, player):
            print('You lose')

        else: 
            print('You win')

def is_win(winner, loser):
    if (winner == 'r' and loser == 's') or (winner == 's' and loser == 'p') or (winner == 'p' and loser == 'r'):
        return True

game()