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
        # self.x = x if x else random.randint(10, server.river.w - 10) * 50
        self.x = x if x and x % 50 == 0 else random.randint(10, (server.river.w - 10) // 50) * 50
        # self.y = y if y else random.randint(50, server.river.h - 100)
        self.y = y if y and y % 50 == 0 else random.randint(1, 10) * 50

    def draw(self):
        self.image.draw(self.x - server.river.window_left, self.y - server.river.window_bottom, 50, 50)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        match group:
            case 'canoe:rock':
                server.canoe.speed = 0