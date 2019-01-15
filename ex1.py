#ex1

# Print different messages

print("Hello World!")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#ex3
print("Hens", 25 + 30 / 6)
print("Roosters", float(100-25*3%4))
print(float(5/3))
print(int(5/3))
print("Is it greater?", 5>-2)

#ex4
cars = 100
print("There are", cars, "cars available")

#ex5
my_name = "Zed A. Shaw"
print(f"Let's talk about {my_name}") #formatted strings

#ex6
types_of_people = 10
x = f"There are {types_of_people} types of people."
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# apply format to an already created strings 
print(joke_evaluation.format(hilarious)) 
print("Isn't that joke so funny?! {}".format(False))

w = "This is ..."
e = " right side."

print(w + e)
