from words import words
import random
import string


print("-----WELCOME TO THE HANGMAN:THE GAME-----")

def get_valid_word(words):
    #getting the valid word to guess
    word = random.choice(words)

    #if word contains '-' or space them we will keep choosing the word and after we find the valid word we will return the word
    while ' ' in word and '-' in word:
        word  = random.choice(words)
    return word

#printing the hangman for every wrong guess
def print_hangman(wrong_guessed):
    if wrong_guessed == 7:
        print('\n(---------)')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 6:
        print('\n(---------)')
        print('    |   |    ')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 5:
        print('\n(---------)')
        print('    |   |    ')
        print('    O   |    ')
        print('        |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 4:
        print('\n(---------)')
        print('    |   |    ')
        print('    O   |    ')
        print('    |   |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 3:
        print('\n(---------)')
        print('    |   |    ')
        print('    O   |    ')
        print('   /|   |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 2:
        print('\n(---------)')
        print('    |   |    ')
        print('    O   |    ')
        print('   /|\  |    ')
        print('        |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 1:
        print('\n(---------)')
        print('    |   |    ')
        print('    O   |    ')
        print('   /|\  |    ')
        print('   /    |    ')
        print('        |    ')
        print('=============')
    elif wrong_guessed == 0:
        print('\n(---------)')
        print('    |   | G O')
        print('    O   | A V')
        print('   /|\  | M E')
        print('   / \  | E R')
        print('        |    ')
        print('=============')
        print('')

#to print dash to hide the word from user and if user letter is already present in the word than return the correctly guessed letter
def print_dash(used_letter,word):
    word_list = [l if l in used_letter else '-' for l in word]
    return word_list 

#to check if user value is in alphabets and not in numerical or any other value
def verify_user_letter():
    alphabets = list(string.ascii_lowercase)

    while True:
        user_input = input('Guess any letter here:').lower()
        
        if user_input in alphabets:
            return user_input
        else:
            print('Invalid letter guessed!')

#to append or add user input or guessed letter in list called used letter which contains the letters which are already used.
def verify_used_letter(user_input,used_letter):
    if user_input not in used_letter:
        used_letter.append(user_input)
    else:
        print('the letter is already used!')

#to ask the user whether he/she want to continue playing the game or quit game
def replay():
    p_again = input('Enter -y- to play again and -n- to quit: ').lower()

    while p_again not in ['y' ,'n']:
        p_again = input('Enter -y- to play again and -n- to quit: ').lower()

    if p_again == 'y':
        play()
    else:
        print('------Game Over:(------')
        quit()
        
def play():
    #random word from the get_valid_word() function.
    word = get_valid_word(words)
    #to store random word in list form
    words_letter = list(word)
    #chances that user gets to guess the correct letter
    live = 8 
    #contains the previously choiced letters by user
    letter_used = list()

    #we will keep play until this following conditions are not true.
    while live > 0 and len(words_letter) > 0:

        #saws the used letters separated by dash(-)
        print('Current used letters are:','-'.join(letter_used))
        #saws the current word in dash(-) form if user has not choosen the correct word
        print('Current word:',' '.join(print_dash(letter_used,word)))
        #shows the remaining or chances user has to guess the word 
        print('You have',live,' lives remaining')

        user_letter = verify_user_letter()

        verify_used_letter(user_letter,letter_used)

        #to check if user guessed letter is in the word list(words_letter),if their remove the letter from the words_letter else decrease the user live 
        if user_letter in word:
            while user_letter in words_letter:
                words_letter.remove(user_letter)
        else:
            live -= 1

        #print the visual structure of hangman if their is any decrement in the user's lives(chances)
        print_hangman(live)

    #now if user live are over show a corresponding message with the word or congrats the user if he/she guesses the word correctly.
    if live == 0:
        print('You lose the game,the word was:( ',word)
    else:
        print('Congrats you guessed the word:) ',word)
        
    replay()

play()




