from pico2d import load_image, draw_rectangle

import game_framework
import game_world
from numbers import ACTION_PER_TIME, M_FRAMES_PER_ACTION, FRAMES_PER_ACTION


class Koopa:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.frame = 0
        self.direction = 1
        self.image = load_image('resource/enemy/koopa_running.png')
        self.camera = camera

    def update(self):
        self.frame = (self.frame + M_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % M_FRAMES_PER_ACTION

        #self.x += self.direction * RUN_SPEED_PPS * game_framework.frame_time *2

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.clip_draw(int(self.frame)*34, 0, 32, 32, screen_x, self.y, 150, 150)
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

class Lava:
    def __init__(self, x, camera):
        self.x = x
        self.y = 35
        self.width, self.height = 80, 30
        self.frame = 0
        self.direction = 1
        self.goomba = load_image('resource/map/lave.png')
        self.camera = camera

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    def draw(self):
        screen_x = self.x - self.camera.x
        self.goomba.clip_draw(int(self.frame)*10, 0, 60, 32, screen_x, self.y, 180, 70)
        draw_rectangle(*self.get_bb_draw())

    def handle_event(self, event):
        pass

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y + 50

    def get_bb_draw(self):
        #카메라 좌표를 고려해서 충돌박스 그리기
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height
        right = screen_x + self.width
        top = self.y + 50
        return left, bottom, right, top


    def handle_collision(self, group, other):
        game_world.remove_object(self)
        pass