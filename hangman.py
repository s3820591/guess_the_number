import random
from re import A
import string
from word import words

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():

    life = 6
    word = get_valid_word(words)
    word_letter = set(word) # set of letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # set of the word the user has guessed

    while len(word_letter) > 0 and life > 0: 
        print (f'Current life is {life}')
        print ('You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print ('Current word: ', ' '.join(word_list))
        user_guess = input('Guess a letter: ').upper()

        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)     
            if user_guess in word_letter:
                word_letter.remove(user_guess)
            else:
                life -= 1
    
        elif user_guess in used_letters:
            print('You have guess that letter. Try again')
        else:
            print ('Invalid input')

    if life == 0:
        print('Sorry! You lose')
        print('The correct word is', word)
    print('Congratulation! You guess it')
    print('The correct word is', word)

hangman()
    