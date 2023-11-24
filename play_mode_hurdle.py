from pico2d import *
import game_framework

import game_world
from runner import Runner

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            runner.handle_event(event)


def init():
    global runner

    runner = Runner()
    game_world.add_object(runner, 1)
    # 허들과 충돌 체크 추가 예정


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