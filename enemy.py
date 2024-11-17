from pico2d import load_image
import game_framework
from numbers import ACTION_PER_TIME, FRAMES_PER_ACTION


class Goomba:
    def __init__(self, camera):
        self.x, self.y = 1000, 105
        self.frame = 0
        self.goomba = load_image('resource/enemy/ground_enemies.png')
        self.camera = camera

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        pass


    def draw(self):
        screen_x = self.x - self.camera.x
        self.goomba.clip_draw(int(self.frame)*17, 0, 17, 16, screen_x, self.y, 50, 50)
        #print(f"Goomba Screen X: {screen_x}")

    def handle_event(self, event):
        pass

class Flower:
    def __init__(self, camera):
        self.x, self.y = 800, 150
        self.frame = 0
        self.goomba = load_image('resource/enemy/flower_enemies.png')
        self.camera = camera

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        pass

    def draw(self):
        screen_x = self.x - self.camera.x
        self.goomba.clip_draw(int(self.frame)*17, 0, 17, 24, screen_x, self.y, 50, 50)
        #print(f"Flower Screen X: {screen_x}")

    def handle_event(self, event):
        pass



