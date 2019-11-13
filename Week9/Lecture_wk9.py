#Composition
#Creates a part-of relationship
#e.g. home --> room
#game design

#abstract classes
#like an abstract idea, you have an idea of how it will work but you aren't sure how you will do it yet
#lile Scaffolding
#have to import abc module

#polymorphism
#the same function ise defined for objects of different types

#encapsulation
#To hide something
# __ is the notation

class NonEncapsulated:
    def __init__(self):
        self.a=10

n=NonEncapsulated()
print(n.a)

class Encapsulated:
    def __init__(self):
        self.__a=10

e=Encapsulated()
print(e.__a)

