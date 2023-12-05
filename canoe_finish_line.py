from pico2d import *

import game_framework
import game_world

import server

class Finish_Line:
    image = None

    def __init__(self, x = None, y = None):
        if Finish_Line.image == None:
            Finish_Line.image = load_image('finish_flag.png')
        self.x = x if x else server.river.w - 200
        self.y = y if y else server.river.h - 25

    def draw(self):
        self.image.draw(self.x - server.river.window_left, self.y - server.river.window_bottom, 50, 50)
        # draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 300, self.x + 25, self.y + 300

    def handle_collision(self, group, other):
        match group:
            case 'canoe:finish_line':
                game_framework.change_mode(canoe_completed_mode)