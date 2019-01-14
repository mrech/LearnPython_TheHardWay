## Modules, Classes, and Objects

# Modules Are Like Dictionaries
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple']) # get X from Y

# Common pattern in Python:
# 1. Take a key=value style container
# 2. Get something out of it by the key's name

# In the case of the dictionary, the key is a string and the syntax is [key]. 
# mystuff['apple']
# In case of the module, the key is an identifier, and the syntax is .key.
# mystuff.apple()


class MyStuff(object):
    def __init__(self):
        
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print('I AM CLASSY APPLES')

# Use a class to craft millions of object at a time
# module only one fpr the entire program


# Object are like a 'mini-imports' though  instantiate
thing = MyStuff()
thing.apple()
print(thing.tangerine)

