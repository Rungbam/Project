import random

from pico2d import *
import game_world
import game_framework

class Clay_plate:
    # image = None

    def __init__(self):
        self.x, self.y = random.choice([0, 800]), random.randint(350, 500)
        self.image = load_image('clay_plate.png')

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        # draw_rectangle(*self.get_bb())
        pass

    def update(self):
        self.x += 1
        pass

    def get_bb(self):
        pass

    def handle_collision_in(self, group, other):
        if group == 'aiming_point:clay_plate':
            game_world.remove_object(self)