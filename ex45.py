# YOU MAKE A GAME: Lost in the forest

"""
* Map
- next_scene
- opening_scene
* Engine
- play
* Scene
    - enter
    * Drown
    * Shot
    * Accident
    * Main Path
    * Hunter house
    * The River
    * Escape Van
"""

# Basic import for the game
from sys import exit
import random as rand
from sys import argv
from engine import *
script, room = argv

# Base class scene


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        print("\n--------------")
        exit(1)

# Death scene - Drown


class Drown(Scene):

    def enter(self):
        print("The current of the river is too strong. You hit a rock,")
        print("you lose consciousness and drown in the deep water.")
        print("\n--------------")
        exit(1)

# Death scene - shot


class Shot(Scene):

    def enter(self):
        print("The hunter is a very jealous guy,")
        print("he strongly believe that you want")
        print("all the animals of the forest and let him starve.")
        print("You left him with")
        print("not other choice. He shoots you straight in the head.")
        print("\n--------------")
        exit(1)

# Death scene - accident


class Accident(Scene):

    def enter(self):
        print("The driver bored to death waiting for you got heavely drunk.")
        print("Unfortunatly,")
        print("you can not help, since you do not have a driver lincense.")
        print("The van invaded the opposite lane when a track was coming.")
        print("The accident is fatal.")
        print("--------------")
        exit(1)

# MainPath is the start of the game


class MainPath(Scene):

    def enter(self):
        print("You are late for a dinner, but you got lost.")
        print("You are in the middle of the forest in a dark walking path.")
        print("You are running down the path, when you see a shelter")
        print("with the light on.")
        print("Maybe somebody is in there..")

        action = input(
            """\n > 1: Enter to ask info
            \n > 2: Continue to run down the path
            \n > """)

        if action == "1":
            print("\n--------------")
            print("You decide to enter into the shelter.")
            print("Dead animals hang everywhere.")
            print("You knock the door..")
            print("Immediately, you hear a gun shooting and a man screaming:")
            print("WHO IS THERE?????")
            return 'hunter_house'

        elif action == "2":
            return 'run_forever'

        else:
            print("\n--------------")
            print("\nDOES NOT COMPUTE! Type 1 or 2.")
            return 'main_path'


class RunForever(Scene):

    def enter(self):
        print("Forever run down the dark path until the end of the days.")
        print("--------------")
        exit(1)


class HunterHouse(Scene):

    def enter(self):
        print("An old man with a riffle open the door..")
        print("Two actions are available:")
        print("""\n 1. Tell a joke
              \n 2. Stay serious
              \n """)

        action = input("> ")

        if action in ("1", "Tell a joke"):
            print("\n--------------")
            print("Lucky for you they made you learn some Forest insutls.")
            print("You tell him the joke they tought you at the academy..")
            print("The stingy hunter laugh at you.")
            print("You gain all his trust and he shows you the way")
            print("to the party house, 10 kilometers away after")
            print("crossing the turbulent river nearby.")
            return 'river'

        elif action in ("2", "Stay serious"):
            print("\n--------------")
            print("The hunter starts thinking that you want")
            print("to know the best hunting spot.")
            print("He gets suspicious and he points the gun at you.")
            return 'shot'

        else:
            print("\n--------------")
            print("DOES NOT COMPUTE! Type 1, 2, 'Tell a joke'.")
            print("or 'Stay serious'.")
            return 'hunter_house'


class River(Scene):
    def enter(self):
        print("After a good laugh and a nice walk you reach the river.")
        print("Close to the river there is a sign:")
        print("'Unfortunatly the bridge collapsed during last storm.")
        print("We are working to give you a better bridge this time.")
        print("Meanwhile KEEP OUT!")
        print("Do not cross the river until a new bridge is built.")
        print("The current is strong and only few make it to the other side.'")

        survival_rate = rand.randint(0, 1)

        if survival_rate == 0:
            print("\n--------------")
            print("You jump into the river kareless of the warning.")
            print("Unfortunalty, today was NOT your lucky day.")
            return 'Drown'

        elif survival_rate == 1:
            print("\n--------------")
            print("You cannot read, so you jump into the river anyway.")
            print("You're damn strong or it is your lucky day..")
            print("You made it all the way through the other side!")
            return 'van'

        else:
            print("C'mon is not hard. Jump into that river.")
            print("A van is waiting for you on the other side.")


class Van(Scene):
    def enter(self):
        print("You are now definitely late for this damn dinner.")
        print("And look at you! You are soaking wet!")
        print("Your are lucky if they let you in.")
        print("Anyway there are 10 km left, before your reach the house,")
        print("and the poor guy in the van has been waiting you until now.")

        drunkness_rate = 0.70

        if rand.random() < drunkness_rate:
            return 'accident'

        else:
            print("You come up with huge amount of excuses. The driver")
            print("does not believe you, but he is nice and he drives you")
            print("all the way to the party and")
            print("then he says: 'Enjoy a--hole'.")
            return 'finished'


# Storing each scene by name in a dictionary.
class Map(object):
    scenes = {
        'Drown': Drown(),
        'shot': Shot(),
        'accident': Accident(),
        'main_path': MainPath(),
        'hunter_house': HunterHouse(),
        'run_forever': RunForever(),
        'river': River(),
        'van': Van()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map(room)
a_game = Engine(a_map)
a_game.play()
