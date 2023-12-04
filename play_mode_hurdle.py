from pico2d import *
import game_framework
import os

import game_world
import server
from hurdle import Hurdle
from track import Track
from runner import Runner

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.runner.handle_event(event)


def init():
    hide_cursor()

    server.track = Track()
    game_world.add_object(server.track, 0)

    server.runner = Runner()
    game_world.add_object(server.runner, 1)
    game_world.add_collision_pair('runner:hurdle', server.runner, None)

    for _ in range(20):
        hurdle = Hurdle()
        game_world.add_object(hurdle, 1)
        game_world.add_collision_pair('runner:hurdle', None, hurdle)


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