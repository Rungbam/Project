from pico2d import open_canvas, delay, close_canvas, hide_cursor
import game_framework

import play_mode_shooting as start_mode
# import logo_mode as start_mode

open_canvas(800, 600)
hide_cursor()
game_framework.run(start_mode)
close_canvas()