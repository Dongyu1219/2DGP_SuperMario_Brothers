from pico2d import load_image, draw_rectangle
import game_framework
import game_world
from numbers import ACTION_PER_TIME, FRAMES_PER_ACTION, RUN_SPEED_PPS


class Goomba:
    def __init__(self, camera):
        self.x, self.y = 2000, 105
        self.frame = 0
        self.direction = 1
        self.goomba = load_image('resource/enemy/ground_enemies.png')
        self.camera = camera

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        self.x += self.direction * RUN_SPEED_PPS * game_framework.frame_time *2

        if self.x >= 2500:  # 오른쪽 경계
            self.direction = -1  # 왼쪽으로 이동
        elif self.x <= 1800:  # 왼쪽 경계
            self.direction = 1  # 오른쪽으로 이동

    def draw(self):
        screen_x = self.x - self.camera.x
        self.goomba.clip_draw(int(self.frame)*17, 0, 17, 16, screen_x, self.y, 50, 50)
        print(f"Goomba: World X = {self.x}, Screen X = {screen_x}, Y = {self.y}")
        left, bottom, right, top = self.get_bb()
        screen_left = left - self.camera.x
        screen_right = right - self.camera.x
        draw_rectangle(screen_left, bottom, screen_right, top)
        #print(f"Goomba Screen X: {screen_x}")

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 30, self.y -30, self.x + 30, self.y +30

    def handle_collision(self, group, other):
        if group == 'mario:goomba':
            print("Mario and Goomba collided!")
            game_world.remove_object(self)

class Flower:
    def __init__(self, camera):
        self.x, self.y = 880, 225
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



