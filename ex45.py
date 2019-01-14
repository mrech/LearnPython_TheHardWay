# YOU MAKE A GAME: Lost in the forest

"""
* Map
- next_scene
- opening_scene
* Engine
- play
* Scene
    - enter
    * Drawn
    * Shot
    * Accident
    * Main Path
    * Hunter house
    * The River
    * Escape Van
"""

from sys import exit
from random import randint
from sys import argv
from engine import *
script, room = argv


class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Drawn(Scene):

    def enter(self):
        print("The current of the river is so strong that you hit a rock,")
        print("you lose consciousness and drawn on the deep water.")
        exit(1)


class Shot(Scene):

    def enter(self):
        print("The hunter is a very jealous guy, he strongly believe that you want")
        print("all the animals of the forest and let him starve. You left him with")
        print("not choice. He shot you straight in the head.")
        exit(1)


class Accident(Scene):

    def enter(self):
        print("The driver bored to death waiting for you got heavely drunk,")
        print("so your escape from the forest is not an easy one. Unfortunatly,")
        print("you can not help since you'are without driver lincense.")
        print("You invede the opposite lane when a track was coming.")
        print("The car accident is fatal.")
        exit(1)


class MainPath(Scene):

    def enter(self):
        print("You are late for a dinner, but you got lost.")
        print("You are in the middle of the forest in a dark walking path.")
        print("You are running down the path, when you see a shelter")
        print("with the light on.")
        print("Maybe somebody is in there..")

        action = input(
            "> 1: Enter to ask info \n > 2: Continue to run down the path")

        if action == 1:
            print("You decide to enter into the shelter.")
            print("Dead animals hang everywhere.")
            print("You knock the door")
            print("Immediatly, you hear a gun shot and screaming")
            print("WHO IS THERE?")
            return 'hunter_house'

        if action == 2:
            return 'run_forever'


class RunForever(Scene):

    def enter(self):
        print("Forever run down the dark path until the end of the days")
        exit(1)


class HunterHouse(Scene):

    def enter(self):
        print("An old man with a riffle open you the door")



        
class Map(object):
    scenes = {
        'drawn': Drawn(),
        'shot': Shot(),
        'accident': Accident(),
        'hunter_house': HunterHouse(),
        'run_forever': RunForever()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        print("1", Map.scenes.get(scene_name))
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        print("2", self.next_scene(self.start_scene))
        return self.next_scene(self.start_scene)


a_map = Map(room)
a_game = Engine(a_map)
a_game.play()
