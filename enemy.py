from pico2d import load_image, delay
import random
import math
import game_framework
import game_world


# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

class Goomba:
    def __init__(self):
        self.x, self.y = 400, 150
        self.frame = 0
        self.goomba = load_image('resource/enemy/ground_enemies.png')

    def update(self):
        #self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.frame = (self.frame + 1) % 2
        pass


    def draw(self):
        self.goomba.clip_draw(self.frame*17, 0, 17, 16, self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass


