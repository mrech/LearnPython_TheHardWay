
# Learning to Speak Object Oriented
# Reading Test

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = [] # create an empty list

# create a dictionary
PHRASES = {
    "class $$$($$$)":
        "Make a class named $$$ that is-a $$$.",
    "class $$$(object):\n\tdef __init__(self, ***)":
        "class $$$ has-a __init__ that takes self and *** parameters.",
    "class $$$(object):\n\tdef ***(self, @@@)":
        "class $$$ has-a function named *** that takes self and @@@ parameters.",
    "*** = $$$()":
        "Set *** to an instance of class $$$",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute, and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    word = word.decode("utf-8")
    WORDS.append(word.strip()) #  python -m pydoc str

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in # capitalize the first letter
                   random.sample(WORDS, snippet.count("$$$"))] # chooses k unique random elements from a population (WORDS)
    other_names = random.sample(WORDS, snippet.count("***"))
    results = [] # create an empty list named results
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) # add numbers of parameters
        param_names.append(', '.join(random.sample(WORDS, param_count))) # join random words base on the number of parameters

    for sentence in snippet, phrase: # for in snippet get phrase
        result = sentence[:] # copying phrase from the end to the beginning 

        # fake class names
        for word in class_names:
            result = result.replace("$$$", word, 1) # string.replace() python -m pydoc str

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try: # specifies exception handlers and/or cleanup code
    while True:
        snippets = list(PHRASES.keys()) # get the keys of PHRASES dict and put it into a list
        random.shuffle(snippets) # shuffle the list just created

        for snippet in snippets: # for each component inside a list
            phrase = PHRASES[snippet] 
            question, answer = convert(snippet, phrase) # snippet = key (code) = question, phrases = value (english) = answer
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER: {}\n\n".format(answer))
except EOFError:
    print("\nBye")