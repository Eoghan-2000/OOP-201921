import string


class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence")
        self.word_play()

    def word_play(self):
        print("User input was: " + self.mywords)


class WordDupli(WordGames):\
    def word_play(self):
        print("User input doubled: ")
        dupli = self.mywords + ' ' + self.mywords
        print(dupli)


class WordScramble(WordGames):
    def __init__(self):
        print("word scrambler")
        super().__init__()
        # WordGames.__init__(self)

    def word_play(self):
        list_of_words = self.mywords.split()
        scrambled = ''
        for word in list_of_words:
            if len(word) > 4:
                if any(p in word for p in string.punctuation):
                    scrambled += word[0] + word[-2] + word[2:-2] + word[1] + word[-1] + ' '
                else:  # no punctuation
                    scrambled += word[0] + word[-1] + word[2:-1] + word[1] + ' '
            else:
                print("too few characters in a word")
        print(scrambled)


# wg = WordGames()
# wd = WordDupli()
ws = WordScramble()

# word_play(word, amount)
# word_play(* args)    --> * means 0 or many 
# if args:      --> check arguments