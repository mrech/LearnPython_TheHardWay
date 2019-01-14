# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ",  states["Florida"])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    print("{} is abbreviated {}".format(
        state, abbrev
    ))

# print every city in state
print('-'*10)
for abbrev, city in cities.items():
    print("{} has the city {}".format(
        abbrev, city
    ))

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    print("{} state is abbreviated {} and has city {}".format(
        state, abbrev, cities[abbrev]
    ))

print('-'*10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas') #default=None

if not state: #state = None
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print('The city for the state \'TX\' is: {}'.format(city))

# get a city with a default value
city1 = cities.get('OR', 'Does Not Exist')
print('The city for the state \'TX\' is: {}'.format(city1))

# DICTIONARY LIMITATIONS: they do not have order
# LIST ordered list of items (look them up by a numeric index)
# DICTIONARY (DICT) match keys to values (look up tables)

# Oder dictionaries
# collections.OrderedDict data structure in Python

scores = [('Nikhil', 6), ('Rohan', 7), ('Manish', 8), ('Ram', 10)] #list
d = {} #empty dictionary

for name, score in scores:
    d[name] = score

d.keys()
d.values()

from collections import OrderedDict
odict = OrderedDict(scores)
odict.move_to_end('Rohan')
odict.move_to_end('Manish', last=False) # moved to the beginning

scores = [('Nikhil', 6), ('Rohan', 7), ('Manish', 8), ('Ram', 10)] #list#
OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse = False)) # sorted by value.
#lambda t: t[1] sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse = True)) 

# Dictionary methods

example = {"ex1" : "list", "ex2" : "formatting", "ex3" : "dict"}
example.clear()
example = {"ex1" : "list", "ex2" : "formatting", "ex3" : "dict"}
example1 = example.copy()
example1.pop('ex2')
