#define a class with is methods (functions)
class Shark:
    def swim(self):
        print("The shark is swimming.")
    
    def be_awesome(self):
        print("The shark is being awesome.")

# function object
# create a variable called main that point the function object
def main():
    sammy = Shark() # Initialize the object
    sammy.swim() # use the mothod of the class
    sammy.be_awesome()

if __name__ == "__main__":
    main()

# module as part of a program
# if Py interpreter is running that module (source file) as the main program,
# it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__
# will be set to the module's name.

