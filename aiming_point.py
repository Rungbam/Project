from pico2d import get_time, load_image, load_font, clamp, draw_rectangle
from sdl2 import SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, SDL_MOUSEBUTTONUP

import game_world
import game_framework

def left_click_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT

def left_click_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT

def time_out(e):
    return e[0] == 'TIME_OUT'


class Aiming_point_move:
    pass


class Bang:
    pass


class StateMachine:
    pass


class Aiming_point:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('aiming_point.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.bullet_count = 6


    def fire_bullet(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            # 마우스 좌표 저장?
            # 충돌 체크(마우스 좌표와 clay_plate 간)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        pass

    def get_bb(self):
        pass

    def handle_colllision(self, group, other):
        pass