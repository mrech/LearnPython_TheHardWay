# All Three Combined

class Parent(object):

    def __init__(self, parent):
        print(parent)

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super().__init__(self.stuff)

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()") # override
        super().altered() # no override
        print("CHILD, AFTER PARENT altered()") # override

dad = Parent()
son = Child('child') # most common use of super() == Child.altered exaple above

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


