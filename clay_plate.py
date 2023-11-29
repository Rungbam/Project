import random

from pico2d import *
import game_world
import game_framework

class Clay_plate:
    # image = None

    def __init__(self):
        self.x, self.y = random.choice([0, 800]), random.randint(350, 500)
        self.image = load_image('clay_plate.png')
        self.dir = 0
        if self.x < 0:
            self.dir = 1
        elif self.x > 800:
            self.dir = -1

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        if self.dir == 1:
            self.x += 1
        elif self.dir == -1:
            self.x -= 1
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25


    def handle_collision(self, group, other):
        if group == 'aiming_point:clay_plate':
            game_world.remove_object(self)