import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():

    word = get_valid_word(words).upper()
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print(word)
    #getting user input

    lives = 5

    while len(word_letters) != 0 and lives > 0:

        #letters used
        #" ".join(['a', 'b', 'c']) --> 'a b c'
        print("You have used these letters: ", " ".join(used_letters))

        #what the current word is --> (G E - R G E)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list)+"\n")

        user_letter = input("Make a guess: ")

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Letter {} is not in the word we are looking for ".format(user_letter))
                lives = lives-1
                print("\n \n You have {} remaining lives \n".format(lives))
        elif user_letter in used_letters:
            print ("You have already made that guuess. Try again")
        else:
            print("Invalid character. Try again")

    if lives == 0:
        print("You run out of lives!")
    else:
        print("You found it. The word was {}".format(word))

hangman()

