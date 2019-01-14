# Reading and Writing Files
from sys import argv

script, filename = argv

print("We're going to erase {}".format(filename))
print("If you don't want that, hit CTRL-C (^C)")
print("If you do wnat that, hit RETURN")

input("?")
print("Opening the file ...")
target = open(filename, 'w+') #+ modifier

#print("Truncating the file. Goodbye!")
#target.truncate() #empties the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write("{}\n{}\n{}".format(line1,line2,line3))


print("And finally, we close it.")
target.close()