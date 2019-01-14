# While-Loops

i = 0
numbers = []


while i < 6:
    print("At the top i is {}".format(i))
    numbers.append(i)

    i = i + 1 
    print("Numbers now: ", numbers)
    print("At the bottom i is {}".format(i))

print("The numbers:")

for num in numbers:
    print(num)

# Convert this while-loop to a function
n = 0
numberlist = []

top_num = int(input("top_num = "))
increment = int(input("increment = "))

def print_range(top_num, increment):
    '''print a list based on defined stop value and step
        print_range(top_num, increment)'''
    for n in range(0, top_num, increment):
        print("Adding {} to the list.".format(n))
        numberlist.append(n)
        print(numberlist)

# CTRL-C to abort


