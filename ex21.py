# Functions can return something

def add(a, b):
    print("ADDING {} + {}".format(a, b))
    return a + b # set variables to be a value from a function

def subtract(a,b):
    print("SUBTRACTING {} - {}".format(a,b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

print("Let's do some math with functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)

print("Age: {}, Height: {}, Weight: {}".format(
    age, height, weight
))

print("Where is a puzzle.")

what = add(age, subtract(height, multiply(weight, 2)))

print("That becomes: ", what, "Can you do it by hand?")




