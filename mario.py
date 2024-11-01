from pico2d import load_image


class Mario:
    def __init__(self):
            self.x, self.y = 100, 90
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
    def update(self):
        self.frame = (self.frame+1) %4
        #self.x += direction *10
        pass
            # self.x += 5
    def draw(self):
            self.mario.clip_draw(self.frame*35, 0, 34, 26, 100, 126, 100, 100)
