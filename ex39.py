# Dictionaries

# You can only use numbers to get items out of a list
# dict let you use anything, not just numbers. 
# a dict associates one thing to another, not matter what it is.

stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Fancisco"
print(stuff['city']) 

stuff[1] = 'Wow'
stuff[2] = 'Neato'
print(stuff[1])

print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]