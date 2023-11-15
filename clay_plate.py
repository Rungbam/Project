import random

from pico2d import *
import game_world
import game_framework

class Clay_plate:
    image = None

    def __init__(self):
        if Clay_plate.image == None:
            Clay_plate.image = load_image('clay_plate.png')
        self.x, self.y = random.choice([0, 800]), random.randint(100, 350)
        if self.x == 0:
            self.dir = 1
        elif self.x == 800:
            self.dir = -1


    def draw(self):
        Clay_plate.image.draw(self.x, self.y, 50, 50)
        # draw_rectangle(*self.get_bb())

    def update(self):
        if self.dir == 1:
            self.x += self.dir * 50 * game_framework.frame_time
        elif self.dir == -1:
            self.x += self.dir * 50 * game_framework.frame_time

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

        self.x = clamp(0, self.x, 800)

    def get_bb(self):
        pass

    def handle_collision_in(self, group, other):
        if group == 'aiming_point:clay_plate':
            game_world.remove_object(self)