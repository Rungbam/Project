from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, \
    draw_rectangle

import time
import math

import game_over
import game_world
import game_framework
from hurdle import Hurdle

import server


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


def jump_out(e):
    return e[0] == 'JUMP_OUT'


def jump_down(e):
    return e[0] == 'JUMP_DOWN'


# Runner Run Speed
PIXEL_PER_METER = (55.0 / 1.0)  # 55 pixel 1m
RUN_SPEED_KMPH = 25.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Runner Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Wait:
    @staticmethod
    def enter(runner, e):
        runner.speed = 0
        runner.dir = 0
        runner.wait_time = get_time()

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if get_time() - runner.wait_time > 3:
            runner.state_machine.handle_event(("TIME_OUT", 0))


class Idle:
    @staticmethod
    def enter(runner, e):
        runner.speed = RUN_SPEED_PPS
        runner.dir = 0

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        pass


class Jump_up:
    @staticmethod
    def enter(runner, e):
        runner.speed = RUN_SPEED_PPS
        runner.dir = math.pi / 4.0

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if runner.y - 75 > 200:
            runner.state_machine.handle_event(('JUMP_DOWN', 0))


class Jump_down:
    @staticmethod
    def enter(runner, e):
        runner.speed = RUN_SPEED_PPS
        runner.dir = -math.pi / 4.0

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if runner.y - 75 < 74:
            runner.state_machine.handle_event(('JUMP_OUT', 0))


class StateMachine:
    def __init__(self, runner):
        self.runner = runner
        self.cur_state = Wait
        self.transitions = {
            Wait: {time_out: Idle},
            Idle: {space_down: Jump_up},
            Jump_up: {jump_down: Jump_down},
            Jump_down: {jump_out: Idle}
        }

    def start(self):
        self.cur_state.enter(self.runner, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.runner)
        self.runner.frame = (self.runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.runner.x += math.cos(self.runner.dir) * self.runner.speed * game_framework.frame_time
        self.runner.y += math.sin(self.runner.dir) * self.runner.speed * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.runner, e)
                self.cur_state = next_state
                self.cur_state.enter(self.runner, e)
                return True

        return False


class Runner:
    def __init__(self):
        self.x, self.y = 100, 150
        # self.x, self.y = 5300, 150
        self.frame = 0
        self.image = load_image('runner.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.score = 0

    def update(self):
        self.state_machine.update()
        self.x = clamp(50.0, self.x, server.track.w - 50.0)
        self.y = clamp(50.0, self.y, server.track.h - 50.0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        sx = self.x - server.track.window_left
        sy = self.y - server.track.window_bottom

        self.image.clip_draw(int(self.frame) * 115, 0, 115, 140, sx, sy, 100, 150)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 75, self.x + 30, self.y + 75

    def handle_collision(self, group, other):
        match group:
            case 'runner:hurdle':
                game_framework.change_mode(game_over)