from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_UP, SDLK_DOWN

from rock import Rock
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
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def time_out(e):
    return e[0] == 'TIME_OUT'


# canoe speed
PIXEL_PER_METER = (10 / 1) # 10픽셀 1m
RUN_SPEED_KMPH = 10 #1.5km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Canoe Action Speed
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 8


class Idle:
    @staticmethod
    def enter(canoe, e):
        canoe.speed = RUN_SPEED_PPS

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass


class Move_UP:
    @staticmethod
    def enter(canoe, e):
        canoe.speed = RUN_SPEED_PPS

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass


class Move_DOWN:
    @staticmethod
    def enter(canoe, e):
        canoe.speed = RUN_SPEED_PPS

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
        self.canoe.x += self.canoe.speed * game_framework.frame_time
        self.canoe.y += self.canoe.speed * game_framework.frame_time

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
        self.image = load_image('canoe_1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        self.x = clamp(50.0, self.x, server.river.w - 50.0)
        self.y = clamp(50.0, self.y, server.river.h - 50.0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        sx = self.x - server.river.window_left
        sy = self.y - server.river.window_bottom

        self.image.clip_draw(0, 0, 100, 100, sx, sy)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, other):
        pass