from pico2d import *

import game_framework
import game_world
import hurdle_completed_mode

import server

class Hurdle_finish_Line:
    image = None

    def __init__(self, x = None, y = None):
        if Hurdle_finish_Line.image == None:
            Hurdle_finish_Line.image = load_image('track_finish_line.png')
        self.x = x if x else server.track.w - 64 # 100
        self.y = y if y else server.track.h - 500 # 388

    def draw(self):
        self.image.draw(self.x - server.track.window_left, self.y - server.track.window_bottom, 72, 210)
        # draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 36, self.y - 106, self.x + 36, self.y + 106

    def handle_collision(self, group, other):
        match group:
            case 'runner:hurdle_finish_line':
                game_framework.change_mode(hurdle_completed_mode)