# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 29-09-2019
# purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)

        # print only first and last of the sentence
        print(message[0] + message[-1])

        # use slice notation
        print(message[0:len(message):len(message)] + message[-1:len(message):len(message)])

        # escaping a character
        print("He said \"That\'s fantastic\"")

        # find all a's in the input word and count how many there are
        message2 = input("Please enter a string:")
        counter = message2.count('a')
        print("The number of times \'a\' is in this string is " + str(counter))

        # replace all occurences of the character a with the - sign

        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(message2.replace('a', '_'))

        # printing only characters at even index positions
        print(message[0:len(message):2])

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out
        array = message.split()
        for i in range(len(array)):
            print(array[i])

        # append a new element to the list and print
        array.append('new')
        for i in range(len(array)):
            print(array[i])

        # remove from the list in 3 ways
        # array = array[:len(array)-1]
        # array.remove('sentence')
        # array.remove(array[-1])
        print(array)

        # check if the word cake is in your input list
        print('cake' in array)

        # reverse the items in the list and print
        array.reverse()
        print(array)

        # reverse the list with the slicing trick
        print(array[::-1])

        # print the list 3 times by using multiplication
        print(array * 3)


tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()