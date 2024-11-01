from pico2d import load_image

class Map_1:
    def __init__(self):
        self.x = 0
        self.world_1 = load_image('World-1.png')
    def update(self):
        if self.x < 0:
            self.x = 0
        elif self.x > 3508:
            self.x = 3508
        pass

    def draw(self):
        self.world_1.clip_draw(self.x, 0, 320, 240, 400, 300, 800, 600)
