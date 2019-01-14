
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()  # instantiate
        print("3", current_scene)

        while True:
            print("\n--------------")
            next_scene_name = current_scene.enter()
            print("4", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("5", current_scene)
