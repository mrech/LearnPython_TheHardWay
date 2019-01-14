# Gothons from Planet Percal #25

'''
* noun (classes)
- verbs (functions)


* Map
- next_scene
- opening_scene
* Engine
- play
* Scene
    -enter
    * Death
    * Central Corridor
    * Laser Weapon Armory
    * The Bridge
    * Escape Pod

'''
# Basic imports for the game
from sys import exit  # exit the interpreter
from random import randint

# base class Scene that will have the common things that all scenes do


class Scene(object):
    def enter(self):
        print('This scene is not yet configured. Subclass it and implement enter().')
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map  # Engine has-a scene_map of some kind

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print('\n--------')
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


# first scene Death

class Death(Scene):

    quips = [
        'You died. You kinda suck at this.',
        'Such a loser.',
        'I have a small puppy that\'s beter at this.'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

# CentralCorridor the start of the game
# I'm doing the scenes for the game before the Map because I need to reference them later


class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print(
            "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filed body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input("> ")

        if action == "shoot!":
            print(
                "Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print(
                "off your aim. Your laser hits his costume but misses him entirely. This")
            print("makes him fly into a rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you.")
            return 'death'

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you.")
            return 'death'

        elif action == "tell ajoke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Ljb jfkdlas tyjkdfak jkfldsaufd, fullrearfek fdfas thiirs.")
            print(
                "The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You do a dive roll into the Wapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times then the lcok closes forever and you can't")
        print("get the bomb. The code is 3 digits.")
        # Permutation with repetitions 9**3
        code = "{}{}{}".format(randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decided to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")
        print("clown costume than the last. They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            return 'death'

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("Now that the bomb is placed you run to the escape pod to")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the bridge'


class EscapePod(Scene):
    def enter(self):
        print("You rush through the ship desperately tring to make it")
        print("You get to the chamber with the escape pods, and now need")
        print("to pick one to take. Some of them could be damaged but you")
        print("don't gave time to look. There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod {} and hit the eject button.".format(guess))
            print("The pod escapes out into the void of space.")
            return 'death'
        else:
            print("You jump into pod {} and hit the eject button.".format(guess))
            print("The pod easily slides out into space heading to")
            print("the planet below. The Gothon ship explode. You won!")
            return 'finished'


class Map(object):
    # Map's methods
    # storing each scene by name in a dictionary, ref. to it Map.scenes
    # Map come after scenes, because the dic btionary has to refer to them so they have to exist

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')  # code that runs the game by making map
a_game = Engine(a_map)  # handling that map to an Engine
a_game.play()  # running - play to make the game work
