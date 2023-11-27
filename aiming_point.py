from pico2d import get_time, load_image, load_font, clamp, draw_rectangle, get_events
from sdl2 import SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, SDL_MOUSEMOTION

import game_world
import game_framework

# def left_click_down(e):
#     return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT
#
# def left_click_up(e):
#     return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT
#
# def time_out(e):
#     return e[0] == 'TIME_OUT'


class Aiming_point:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('aiming_point.png')
        self.bullet_count = 6


    def fire_bullet(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            # 마우스 좌표 저장?
            # 충돌 체크(마우스 좌표와 clay_plate 간)

    def update(self, event=None):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x, self.y = event.x, 600 - 1 - event.y
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    self.x, self.y = event.x, 600 - 1 - event.y

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, self.x, self.y, 50, 50)

    def get_bb(self):
        return self.x, self.y

    def handle_colllision_in(self, group, other):
        if group == 'aiming_point:clay_plate':
            # 점수 증가
            print('적중')
            pass