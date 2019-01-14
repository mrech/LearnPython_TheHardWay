# Override Explicitly

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()") # overrides that function by defining its own version

mum = Parent()
daughter = Child()

mum.override()
daughter.override()
