# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print("This is count {}".format(number))

for fruit in fruits:
    print("A fruit of type: {}".format(fruit))

for i in change:
    print("I got {}".format(i))

# build a list
elements = []

for i in range(0, 6):
    print("Adding {} to the list.".format(i))
    # append is a function that lists understand
    elements.append(i)

# print them out

for i in elements:
    print("Element was: {}".format(i))

