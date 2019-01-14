# Script that accepts arguments
from sys import argv
# unpacks argv. Arguments assiged to four variables
script, first, second, third = argv

colour = input("Favourite colour: ")

print("The script is called :", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your favourite colour is {}".format(colour))