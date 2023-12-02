from pico2d import *

import random
import game_framework
import game_world

import server

class Rock:
    image = None

    def __init__(self, x = None, y = None):
        if Rock.image == None:
            Rock.image = load_image('rock.png')
        self.x = x if x else random.randint(500, server.river.w - 100)
        self.y = y if y else random.randint(50, server.river.h - 50)

    def draw(self):
        self.image.draw(self.x - server.river.window_left, self.y - server.river.window_bottom, 50, 50)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        # match group:
            pass