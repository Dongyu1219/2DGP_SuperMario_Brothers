from pico2d import load_image, draw_rectangle

import game_framework
import logo_mode


class Peach:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 45, 120
        self.camera = camera
        self.image = load_image('resource/mario/peach.png')

    def get_bb(self):
        return self.x - self.width, self.y - self.height//3, self.x + self.width, self.y + self.height
        pass

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height//3
        right = screen_x + self.width
        top = self.y +  self.height
        return left, bottom, right, top
        pass

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 60, 80)
        #draw_rectangle(*self.get_bb_draw())

    def handle_collision(self, group, other):
        if group == 'mario:peach':
            pass
        pass

    def update(self):
        pass