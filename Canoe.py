from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_UP, SDLK_DOWN
from rock import Rock
import game_world
import game_framework

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
PIXEL_PER_METER = (1 / 1) # 1픽셀 1m
RUN_SPEED_KMPH = 1.5 #1.5km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Canoe Action Speed
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 8


class UP_and_DOWN:
    @staticmethod
    def enter(canoe, e):
        if up_down(e) or down_up(e): # 위로 이동
            pass
        if down_down(e) or up_up(e):
            pass

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass

    @staticmethod
    def draw(canoe):
        pass


class Speed_up:
    @staticmethod
    def enter(canoe, e):
        pass

    @staticmethod
    def exit(canoe, e):
        pass

    @staticmethod
    def do(canoe):
        pass

    @staticmethod
    def draw(canoe):
        pass


class StateMachine:
    def __init__(self, canoe):
        self.canoe = canoe
        self.cur_state = Speed_up
        self.transitions = {

        }

    def start(self):
        pass

    def update(self):
        pass

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.canoe, e)
                self.cur_state = next_state
                self.cur_state.enter(self.canoe, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.canoe)


class Canoe:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('canoe.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()