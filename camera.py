from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import ending_mode
import game_framework
from numbers import RUN_SPEED_PPS

class Camera:
    def __init__(self):
        self.x = 0
        #self.x = 2200
        self.direction = 0
        self.move = True

    def update(self):
        if self.move:
            self.x += self.direction * RUN_SPEED_PPS * game_framework.frame_time
            if self.x < 0.0:
                self.x = 0.0
            elif self.x > 1100 * 800/ 320:  # 맵의 오른쪽 경계에 도달
                self.x = 1100.0* 800/320
                game_framework.change_mode(ending_mode)

        #print(f"Camera X: {self.x}")
    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.direction = 1
            elif event.key == SDLK_LEFT:
                self.direction = -1
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_RIGHT, SDLK_LEFT):
                self.direction = 0

    def stop_movement(self):
        """카메라 이동을 멈춤"""
        self.move = False
        self.direction = 0

    def resume_movement(self):
        """카메라 이동을 재개"""
        self.move = True

    def draw(self):
        pass

    # def handle_collision(self, group, other):
    #     if group == 'mario:wall':
    #         #self.move = False
    #         #self.stop_movement()
