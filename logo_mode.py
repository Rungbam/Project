import title_mode
from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework


def init():
    global image
    image = load_image('tuk_credit.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_frame_time = get_time()
        game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()