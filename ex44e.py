# Composition: use other classes and modules
# HAS-A RELATIONSHIP

# Other could just make it into a module named other.py


class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

# Child HAS-A Other that it uses to get its work done


class Child(object):

    def __init__(self):
        self.other = Other()  # Instantiate Other class

    def implicit(self):
        self.other.implicit()  # calling functions in another class to exploit inheritance

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()
