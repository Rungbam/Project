import random

from pico2d import *
import game_framework

import game_world
from field import Field
from clay_plate import Clay_plate
from aiming_point import Aiming_point

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():

    field = Field()
    game_world.add_object(field, 0)

    aiming_point = Aiming_point()
    game_world.add_object(aiming_point, 1)
    game_world.add_collision_pair('aiming_point:clay_plate', aiming_point, None)

    clay_plates = [Clay_plate() for _ in range(6)]
    game_world.add_objects(clay_plates, 1)

    for clay_plate in clay_plates:
        game_world.add_collision_pair('aiming_point:clay_plate', None, clay_plate)


def finish():
    game_world.clear()
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