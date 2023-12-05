from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework

def init():
    global image
    global bgm
    image = load_image('hurdle_completed.jpg')
    bgm = load_music('Results-_Win_-Nintendo-Switch-Sports.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()

def finish():
    global image
    global bgm
    del image
    del bgm


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()