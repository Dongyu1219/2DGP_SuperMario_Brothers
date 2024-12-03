from pico2d import load_image

class peaach:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 45, 120
        self.camera = camera
        self.image = load_image('resource/mario/peach.png')

    def get_bb(self):
        return self.x - self.width//2 , self.y - self.width , self.x + self.width+15, self.y + self.height

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x
        left = screen_x - self.width//2
        bottom = self.y - self.height
        right = screen_x + self.width+15
        top = self.y  + self.height
        return left, bottom, right, top

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 90, 120)
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass