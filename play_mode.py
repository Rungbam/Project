import random

from pico2d import *
import game_framework

import game_world
from field import Field

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    

def init():

    field = Field()
    game_framework.add_object(field, 0)

    pass


def finish():
    game_world.clear()()
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass