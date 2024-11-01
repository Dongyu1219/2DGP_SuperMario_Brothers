from pico2d import load_image


class Mario:
    def __init__(self):
            self.x, self.y = 100, 126
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
    def update(self):
        self.frame = (self.frame+1) %4
        pass

    def handle_event(self):
        pass

    def draw(self):
            self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)
