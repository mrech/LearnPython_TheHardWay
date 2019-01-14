# Alter Before or After

class Parent(object):
    
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()") #altered parent version overitten
        super().altered() # get the Parent (inheritance) altered version
        print("CHILD, AFTER PARENT altered()") # return to Child and print out the after message

 
dad = Parent()
son = Child()