import pico2d
from pico2d import load_image


class Mario:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 3
        self.image = load_image('')
        pass
