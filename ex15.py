from sys import argv
# filename inserted in the comand line before running the code
script, filename = argv
txt = open(filename) # create a file object

print("Here's your file {}:".format(filename))
print(txt.read())
txt.close()

# filename inserted while the code is running
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
#It's important to close the files when you're done
txt_again.close()
