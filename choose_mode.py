from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_1, SDLK_2

import game_framework
import canoe_rule_mode
import hurdle_rule_mode

def init():
    global image
    global bgm
    image = load_image('choose.jpg')
    bgm = load_music('Title-Screen-Nintendo-Switch-Sports.mp3')
    bgm.set_volume(150)
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            game_framework.change_mode(canoe_rule_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            game_framework.change_mode(hurdle_rule_mode)


def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()