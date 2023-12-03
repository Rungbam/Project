import os

from pico2d import *
import game_framework
import game_world

import server
from canoe import Canoe
from river import River
from rock import Rock

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.canoe.handle_event(event)


def init():
    server.river = River()
    game_world.add_object(server.river, 0)

    server.canoe = Canoe()
    game_world.add_object(server.canoe, 1)
    game_world.add_collision_pair('canoe:rock', server.canoe, None)

    for _ in range(125):
        rock = Rock()
        game_world.add_object(rock, 1)
        game_world.add_collision_pair('canoe:rock', None, rock)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()