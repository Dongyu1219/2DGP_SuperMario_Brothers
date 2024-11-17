from pico2d import load_image

class Opening:
    def __init__(self):
        self.opening = load_image('opening_image.png')
        self.screen_size = 260
        pass
    def draw(self):
        self.opening.draw_now(260, 260, self.screen_size, self.screen_size)
    def update(self):
        pass
