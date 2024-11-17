from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import ending_mode
import game_framework
from numbers import RUN_SPEED_PPS

class Camera:
    def __init__(self):
        self.x = 0
        self.direction = 0

    def update(self):
        self.x += self.direction *RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 0.0:
            self.x = 0.0
        elif self.x > 1180.0 :  # 맵의 오른쪽 경계에 도달
            self.x = 1180.0
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
