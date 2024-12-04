from pico2d import load_image

class Peach:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 45, 120
        self.camera = camera
        self.image = load_image('resource/mario/peach.png')

    def get_bb(self):
        pass

    def get_bb_draw(self):
        pass

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 60, 80)
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass