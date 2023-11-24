from pico2d import *
import game_framework

import game_world
from canoe import Canoe

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            canoe.handle_event(event)


def init():
    global canoe

    canoe = Canoe()
    game_world.add_object(canoe, 1)
    # 카누와 장애물 간 충돌 체크 추가 예정


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