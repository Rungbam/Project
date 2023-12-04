import math
from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_UP, SDLK_DOWN, \
    draw_rectangle

from rock import Rock
from canoe_finish_line import Finish_Line
import game_world
import game_framework

import server


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def time_out(e):
    return e[0] == 'TIME_OUT'


# canoe speed
PIXEL_PER_METER = (10 / 1) # 10픽셀 1m
RUN_SPEED_KMPH = 50 #50km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Idle:
    @staticmethod
    def enter(canoe, e):
        canoe.speed = RUN_SPEED_PPS
        canoe.dir = 0
        canoe.speed_y = RUN_SPEED_PPS

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass


class Move_UP:
    @staticmethod
    def enter(canoe, e):
        canoe.dir = math.pi / 4.0
        canoe.speed = RUN_SPEED_PPS
        canoe.speed_y = RUN_SPEED_PPS

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass


class Move_DOWN:
    @staticmethod
    def enter(canoe, e):
        canoe.dir = -math.pi / 4.0
        canoe.speed = RUN_SPEED_PPS
        canoe.speed_y = RUN_SPEED_PPS

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass


class StateMachine:
    def __init__(self, canoe):
        self.canoe = canoe
        self.cur_state = Idle
        self.transitions = {
            Idle: {up_down: Move_UP, down_down: Move_DOWN, up_up: Move_DOWN, down_up: Move_UP},
            Move_UP: {up_up: Idle, down_down: Idle},
            Move_DOWN: {down_up: Idle, up_down: Idle}
        }

    def start(self):
        self.cur_state.enter(self.canoe, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.canoe)
        self.canoe.x += math.cos(self.canoe.dir) * self.canoe.speed_y * game_framework.frame_time
        self.canoe.y += math.sin(self.canoe.dir) * self.canoe.speed_y * game_framework.frame_time

        self.canoe.canoe_x += math.cos(self.canoe.dir) * self.canoe.speed * game_framework.frame_time
        self.canoe.canoe_y += math.sin(self.canoe.dir) * self.canoe.speed_y * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.canoe, e)
                self.cur_state = next_state
                self.cur_state.enter(self.canoe, e)
                return True

        return False

    # def draw(self):
    #     self.cur_state.draw(self.canoe)


class Canoe:
    def __init__(self):
        self.x, self.y = 400, 300
        self.canoe_x, self.canoe_y = 400, 300
        self.image = load_image('canoe.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        self.x = clamp(50.0, self.x, server.river.w - 50.0)
        self.y = clamp(50.0, self.y, server.river.h - 50.0)

        self.canoe_x = clamp(50.0, self.canoe_x, server.river.w - 50.0)
        self.canoe_y = clamp(50.0, self.canoe_y, server.river.h - 50.0)

        # 카누가 화면 밖으로 벗어날 경우
        if self.canoe_x < self.x - 450:
            game_framework.quit()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        sx = self.canoe_x - server.river.window_left
        sy = self.canoe_y - server.river.window_bottom

        self.image.clip_draw(0, 0, 100, 100, sx, sy)

        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.canoe_x - 20, self.canoe_y - 5, self.canoe_x + 20, self.canoe_y + 15

    def handle_collision(self, group, other):
        pass