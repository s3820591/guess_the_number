import random

def guess(x):
    ran_num = random.randint(1, x)
    guess = 0
    while guess != ran_num:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < ran_num:
            print('Sorry. Too low')
        elif guess>ran_num:
            print('Sorry. Too high')
    print(f'Correct!!! The number is {ran_num}')

def com_guess(x):
    low = 1
    high = x
    answer = ''
    while answer != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        answer = input(f'Is {guess} too high (H), too low (L) or correct(C)??')
        if answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1

    print(f'So the correct number is {guess}')   

com_guess(1000)
