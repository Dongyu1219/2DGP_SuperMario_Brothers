from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

class Map_1:
    def __init__(self):
        self.x = 0
        self.direction = 0
        self.world_1 = load_image('World-1.png')
    def update(self):
        self.x += self.direction *5
        if self.x < 0:
            self.x = 0
        elif self.x > 3508:
            self.x = 3508
        pass

    def handle_events(self, event):
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.direction += 1
                    pass
                elif event.key == SDLK_LEFT:
                    self.direction -= 1
                    pass
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.direction -= 1
                elif event.key == SDLK_LEFT:
                    self.direction += 1

    def draw(self):
        self.world_1.clip_draw(self.x, 0, 320, 240, 400, 300, 800, 600)

