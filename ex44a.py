# Implicit Inheritance

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass # empty block

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # call the implicit from the Parent even though son does not have an implicit function defined

# Child class will inherit all its behavior from Parent.

# If you put functions in a base class (Parent), then all subclasses (i.e. Child) will automatically get those features.
# Handy for repetitive code you need in many classes. 


