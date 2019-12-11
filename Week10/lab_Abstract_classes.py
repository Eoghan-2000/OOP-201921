from abc import ABC, abstractmethod


class mathsGames(ABC):

    def game(self):
        pass


class fibbo(mathsGames):

    def game(self):
        current = 1
        previous = 1
        fibSequence = [0, 1, 1]
        amount = input('Please enter the amount of numbers you would like in your sequence:')

        for i in range(int(amount)):
            current = int(current + previous)
            previous = int(current - previous)
            fibSequence.append(current)

        print('Fibonacci numbers are: ', fibSequence)


mg = fibbo()
mg.game()
