# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games

import string

class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        self.mywords= self.mywords.split()
        temp = self.mywords[0]
        self.mywords[0] = self.mywords[(len(self.mywords)-1)]
        self.mywords[(len(self.mywords)-1)] = temp
        for i in range(len(self.mywords)):
            print(self.mywords[i], end=" ")

class WordDupli(WordGames):
    super.__init__()
    def word_play(self):
        self.mywords = mywords
        print(self.mywords, " ", self.mywords)
        print("hello")


class WordScramble(WordGames):
    pass

#wg = WordGames()
wd = WordDupli()