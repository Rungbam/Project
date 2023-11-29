from pico2d import get_time, load_image, load_font, clamp, draw_rectangle, get_events
from sdl2 import SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, SDL_MOUSEMOTION, SDL_MOUSEBUTTONUP

import game_world
import game_framework

def left_click_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT

def left_click_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT

def mouse_move(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEMOTION

# def time_out(e):
#     return e[0] == 'TIME_OUT'


class Bang:
    @staticmethod
    def enter(aiming_point, e):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    aiming_point.bang_x, aiming_point.bang_y = event.x, 600 - 1 - event.y
        pass

    @staticmethod
    def exit(aiming_point, e):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONUP:
                if event.button == SDL_BUTTON_LEFT:
                    aiming_point.bang_x, aiming_point.bang_y = event.x, 600 - 1 - event.y
            if event.type == SDL_MOUSEMOTION:
                aiming_point.x, aiming_point.y = event.x, 600 - 1 - event.y
            pass

    @staticmethod
    def do(aiming_point):
        pass

    @staticmethod
    def draw(aiming_point):
        aiming_point.image.clip_draw(0, 0, 512, 512, aiming_point.x, aiming_point.y, 50, 50)



class Move:
    @staticmethod
    def enter(aiming_point, e):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                aiming_point.x, aiming_point.y = event.x, 600 - 1 - event.y

    @staticmethod
    def exit(aiming_point, e):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    aiming_point.x, aiming_point.y = event.x, 600 - 1 - event.y
                    aiming_point.bang_x, aiming_point.bang_y = event.x, 600 - 1 - event.y

        pass

    @staticmethod
    def do(aiming_point):
        pass

    @staticmethod
    def draw(aiming_point):
        aiming_point.image.clip_draw(0, 0, 512, 512, aiming_point.x, aiming_point.y, 50, 50)


class StateMachine:
    def __init__(self, aiming_point):
        self.aiming_point = aiming_point
        self.cur_state = Move
        self.transitions = {
            Move: {left_click_down: Bang},
            Bang: {left_click_up: Move}
        }

    def start(self):
        self.cur_state.enter(self.aiming_point, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.aiming_point)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.aiming_point, e)
                self.cur_state = next_state
                self.cur_state.enter(self.aiming_point, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.aiming_point)


class Aiming_point:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('aiming_point.png')
        self.bullet_count = 6
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.bang_x, self.bang_y = 0, 0


    def fire_bullet(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            # 마우스 좌표 저장?
            # 충돌 체크(마우스 좌표와 clay_plate 간)

    def update(self):
        self.state_machine.update()

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x, self.y = event.x, 600 - 1 - event.y
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    self.bang_x, self.bang_y = event.x, 600 - 1 - event.y


    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.bang_x - 5, self.bang_y - 5, self.bang_x + 5, self.bang_y + 5

    def handle_collision(self, group, other):
        if group == 'aiming_point:clay_plate':
            # 점수 증가
            print('적중')