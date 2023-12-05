import random
import server

from pico2d import *


class River:
    def __init__(self):
        self.image = load_image('river.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.bgm = load_music('Canoe-Nintendo-Switch-Sports.mp3')
        self.bgm.set_volume(55)
        self.bgm.repeat_play()
        # self.count_down_bgm = load_music('count_down.wav')
        # self.count_down_bgm.set_volume(200)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(server.canoe.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.canoe.y) - self.ch // 2, self.h - self.ch - 1)

    def handle_event(self, event):
        pass