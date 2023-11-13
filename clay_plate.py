from pico2d import *
import game_world
import game_framework

class Clay_plate:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Clay_plate.image == None:
            Clay_plate.image = load_image('clay_plate.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        pass

    def handle_collision(self, group, other):
        pass