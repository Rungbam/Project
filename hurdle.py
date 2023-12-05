from pico2d import *

import random
import game_world
import game_framework
import server

# animation_names = ['hurdle', 'fall_down']


class Hurdle:
    image = None

    def __init__(self, x = 460, y = None):
        if Hurdle.image == None:
            Hurdle.image = load_image('hurdle.png')


        self.current_value = 360

        # self.x = x if x and x % 100 == 0 else random.randint(36, 550) * 10
        self.x = x
        self.y = y if y else 100

    def draw(self):
        self.image.draw(self.x - server.track.window_left, self.y - server.track.window_bottom, 100, 100)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 0, self.y - 50, self.x + 40, self.y + 40

    def handle_collision(self, group, other):
        pass