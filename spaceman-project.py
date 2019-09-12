import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    
    if counter == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    #Thank you Alex Gray for helping me out with this function. My method was too complicated and he helped me simplify it.
    display = " "

    for i in secret_word:
        if i in letters_guessed:
            display += i
        else:
            display += " _ "
    return display

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet




def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False



def spaceman(secret_word):
    print("Welcome to the Spaceman Game! You have been chosen a random word that you must guess using one letter at a time!")
    letters_guessed = []
    count = 7
#guess tracking and correctness
    while count > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        guess = input ("Guess a letter please: ")
        print("You have " + str(count) + " guesses left.") 
        letters_guessed.append(guess)
        
        correct = is_guess_in_word(guess, secret_word)
        try:
            if correct:
                print ("Good job!")
            else:
                print ("Better luck next time! Guess again")
                count -= 1
        finally: 
            print(get_guessed_word(secret_word, letters_guessed))
#iterating through the word to check if it contains guessed letter
    is_word_guessed (letters_guessed, secret_word)
    if count == 0:
        print ("You lost! Try again please!")
        print("The word was " + secret_word + ", sorry partner!")
    if count > 0:
        print ("You got it!!")




#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
