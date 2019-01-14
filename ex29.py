# What if

people = 20
cats = 30
dogs = 15

if people < cats: # colon and indent
    print("Too many cats!") # block

if people > cats:
    print("Not many cats!")

if people < dogs:
    print("The world is drooled on")

if people > dogs:
    print("The world is dry!")

# INCREMENT BY operator
dogs += 5 #add five and assign it to a variable. Same as doing: (x = x + 1) == (x += 1)

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs")