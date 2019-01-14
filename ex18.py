# Names, Variables, Code, Functions

#*args: take all the arguments and put them in args as a list
def print_two(*args): # define a function, like argv
    arg1, arg2 = args # unpacks the arguments
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_one(arg1):
    print("arg1: {}".format(arg1))

def print_none():
    print("I got nothin'.")

print_two("Morena", "Rivato")
print_two_again("Morena", "Rivato")
print_one("First!")
print_none()

