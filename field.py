from pico2d import *

class Field:
    def __init__(self):
        self.image = load_image('field.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)