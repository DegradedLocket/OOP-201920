# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games
import random

class WordGames:
    def __init__(self):
        self.myWords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: " + self.myWords)




class WordDupli(WordGames):
    dupe = WordGames.myWords * 2

    print("Duplicated: ")
    print(dupe)

class WordScramble(WordGames):
    scramble = WordGames.myWords.split()

    scramble = [''.join(random.sample(word, len(word))) for word in scramble]
    print("Scrambled:")
    print(scramble)



wg = WordGames()