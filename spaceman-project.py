import random
import unittest


#This function pulls words from a text file and selects a random word
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word


#This function will check if all the letters of the word have been guessed
def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    
    if counter == len(secret_word):
        return True
    else:
        return False


#This function will display either underscores or correctly guessed letters in their respective places to the user in the terminal
def get_guessed_word(secret_word, letters_guessed):
    #Thank you Alex Gray for helping me out with this function. My method was too complicated and he helped me simplify it.
    display = ""

    for i in secret_word:
        if i in letters_guessed:
            display += i
        else:
            display += " _ "
    return display


#This function checks is a guessed letter is in a word
def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False


#This function is what controls the flow of the game
def spaceman(secret_word):
    letters_guessed = []
    count = 7
    print("Welcome to the Spaceman Game! You have been chosen a random word that you must guess using one letter at a time!")
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
                print ("Oof so close! Guess again")
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



#These function calls will start the game
secret_word = load_word()
spaceman(secret_word)

class spaceman_Tests(unittest.TestCase):
    def test_is_word_guessed(self):
        self.assertEqual(is_word_guessed('dog','god'), True)

    def test_get_guessed_word(self):
        self.assertEqual(get_guessed_word('dog', 'god'), 'dog')

    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word('apple', 'l'), False)


unittest.main()