# MAKE SURE THAT YOU ENCAPSULATE ALL YOUR VARIABLES
class MagicalCreature():
    def __init__(self, name, type, height, colour):
        self.weapon = "Battle armour"
        self.name = name
        self.type = type
        self.colour = colour
        self.height = height


    def talk(self):
        print ("I am ", self.name)

    def fight(self):
        if self.weapon == "Battle armour":
            print("I can fight")
        elif self.weapon == "None":
            print("I cannot fight")





class Horse(MagicalCreature):
    def __init__(self, name, type, wings, height, colour):
        super.__init__(name, height, colour)
        self.wings = wings
        self.type = type

    def fly(self):
        if self.wings == True:
            print("I can fly flying")
        elif self.wings == False:
            print("I cannot fly")


class Cat(MagicalCreature):
    def __init__(self, name, height, colour):
        super().__init__(name, height, colour)


class Spirit(Horse):
    def __init__(self, name, type, height):
        Horse.__init__(type)
        self.name =  name
        self.height = height
        self.colour = "white"
        self.wings = True
        self.weapon = "None"




class Swiftwind(Spirit):
    def __init__(self, name, type, height, colour):
        Horse.__init__(name, type, height, colour)
        self.wings = True
        self.weapon = "Battle armour"


class ThirtyThirty(Horse):
    def __init__(self, name, type, height, colour):
        Horse.__init__(name, type, height, colour)
        self.wings = False
        self.weapon = "Battle armour"


class Starlite(Horse):
    def __init__(self, name, type, height, colour):
        Horse.__init__(name, type, height, colour)
        self.wings = False
        self.weapon = "None"

    def travel(self):
        print("I am traveling on the rainbow")

class Cringer(Cat):
    pass

class Battlecat(Cringer):
    pass

class Panthor(Cat):
    pass

horse = Horse('Alfie', 'horse', True, 'height', 'white')
horse.talk()