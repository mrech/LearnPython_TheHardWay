#Is-A, Has-A, Objects, and Classes
class Animal(object): # object lowercase is the 'class' you inherit from to make a class.
    # A class inherits from the class named object to make a class, but it is not an object.
    # Simplify, Pthon always requires (object) when you make a class.
    def __init__(self, name):
        self.name = name
        print(name, "can't talk")
    
    def behave(self):
        print("Animals sleep a lot") # function in base class

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print(name, 'is MOWINGGGGGG')
        super(Cat, self).__init__(name)
        super().behave()
    
    def sleep(self):
        print("Cats must get an average of 12 to 16 hours of shut-eye a day.")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name 
        self.pet = None # set default None
        self.pets = None

class Employee(Person):

    def __init__(self, name, salary):  # how you can run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name) # allows us to avoid using base class explicity, this case Person - Working with multiple inheritance
        self.salary = salary
    
    

satan = Cat("Satan")
tiger = Cat("Tiger")
rover = Dog("Rover")

mary = Person("Mary")
mary.pet = satan
# What if Mary has-many pets
mary.pets = [satan, tiger, rover] #list of pets
mary.pets[0].name
mary.pets = {'cats': [satan, tiger], 'dogs':[rover]} #dictionary of lists of pets
mary.pets['cats']

for value in mary.pets.values():
    print(value[0].name)

frank = Employee("Frank", 12000)
frank.pet = tiger

# Method Resolution Order (MRO) order in which the method should be inherited in presence of multiple inheritance.
Employee.__mro__

# IS-MANY relationship - Multiple inheritance (to avoid)

class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.')

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.')
    super().__init__('Dog')
    
d = Dog()
Dog.__mro__
