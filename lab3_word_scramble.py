# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        word=list(self.user_input)
        temp=word[1]
        word[1]=word[2]
        word[2]=temp
        for i in range(len(word)):
            print(word[i], end ="")
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        word='switch'
        wordlst=list(word)
        temp1=wordlst[4]
        temp2=wordlst[5]
        wordlst[4]=wordlst[0]
        wordlst[5]=wordlst[1]
        wordlst[0]=temp1
        wordlst[1]=temp2
        print("")
        for i in range(len(word)):
            print(wordlst[i], end ="")
        print("")




        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        sentence='This is the sentence to scramble.'
        sentencelst=sentence.split()
        temp=sentencelst[0]
        sentencelst[0]=sentencelst[5]
        sentencelst[5]=temp
        for i in range(len(sentencelst)):
            print(sentencelst[i], end=" ")

word_scrambler = WordScramble()
word_scrambler.scramble()

