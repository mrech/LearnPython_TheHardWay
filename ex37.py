## KEYWORDS
# del 
houses = ["Condo", "Villa", "Appartment", ]
del(houses[0])

# assert if True nothing happens if False AssertionError

assert False
assert False, "Oh no!"
assert 2 + 2 == 5, "Houston we've got a problem"

# global
#1.
globalvar = 0

def set_globalvar_to_one():
    global globalvar
    globalvar = 1


def print_globavar():
    print(globalvar)

set_globalvar_to_one()
print_globavar()

#2.
def bob():
    me = "localy defined"
    print(me)

bob()
print(me) # Asking for a global variable

# with global statement, the variable will become available "outside"
# the scope of the function

def bob_global():
    global me
    me = "locally defined"
    print(me)

bob()
print(me)

# pass statement
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

# yield statement
# iterables for... in... read them as much as you wish, but store all the values in memory
mylist = [1, 2, 3] 
for i in mylist:
    print(i)

# generator you can only iterate over them once.
# they generate values on the fly (NOT in memory)

mygenerator = (1, 2, 3)
for i in mygenerator:
    print(i)

# yield used like return, except func retrun a generator

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)

# useful function will return a huge set of values that you will only need to read once.
# when you call the func., the func. body does not run. The function return the generator object.

# break
for val in "string":
    if val == "i":
        break
    print(val)

# except
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# file does not exist this is only informative msg. The code continue to run

# Class

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobject = MyClass() # holds an object of the class "MyClass"
myobject.variable # Access the variable inside the newly created object

myobject.function() #Access object functions

# exec

prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

# raise
x = 10
if x > 5:
    raise Exception("x should not exceed 5. This x = {}".format(x))

# continue

for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter:', letter)

# finally

try:
    f = open("C:/PyWorkSpace/LearnPython_TheHardWay/ex17_to_file.txt", encoding = 'utf-8')
    print(f)
finally:
    f.close() # makes sure the file is closed even if an exception occurs

# lambda

g = lambda x: x*x*x
print(g(7))

#otherwise
def cube(y):
    return y*y*y

## DATA TYPES
'h' == 'h'


## STRING ESCAPE SEQUENCES

definition = '''
The \'''global" \rstatement is a declaration which \vholds for the entire
current code block.  \fIt means that the listed identifiers are to be
interpreted as globals.
'''

print(definition)

x = 2530
x //= 153
x
2530/153 

y = 2530
y = y % 153
y

z = 2530
z %= 153
z

w = 2530
w **= 153
w 

w^153

w = 15 ** 2
# exponential formatting in the scientific notation
'{:e}'.format(w)
