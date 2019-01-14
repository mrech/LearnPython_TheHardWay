
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count))
    print("You have {} boxes of crackers!".format(
        boxes_of_crackers))
    print("That's enogh for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

amount_of_cheese = int(input("> "))
amount_of_crackers = int(input("> "))
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
