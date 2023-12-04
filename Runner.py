from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, \
    draw_rectangle

import game_world
import game_framework
from hurdle import Hurdle

import server


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


# Runner Run Speed
PIXEL_PER_METER = (55.0 / 1.0)  # 55 pixel 1m
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Runner Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Idle:
    @staticmethod
    def enter(runner, e):
        runner.speed = RUN_SPEED_PPS

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        pass


class Jump:
    @staticmethod
    def enter(runner, e):
        runner.speed = RUN_SPEED_PPS
        pass

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        pass


class StateMachine:
    def __init__(self, runner):
        self.runner = runner
        self.cur_state = Idle
        self.transitions = {

        }

    def start(self):
        self.cur_state.enter(self.runner, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.runner)

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
        self.x, self.y = 50, 90
        self.frame = 0
        self.action = 3
        self.image = load_image('yoshi.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        self.x = clamp(50.0, self.x, server.track.w - 50.0)
        self.y = clamp(50.0, self.y, server.track.h - 50.0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        sx = self.x - server.track.window_left
        sy = self.y - server.track.window_bottom

        self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, sx, sy)

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50

    def handle_collision(self, group, other):
        pass