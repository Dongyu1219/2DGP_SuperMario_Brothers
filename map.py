from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT
class Map_1:
    def __init__(self, camera):
        self.world_1 = load_image('resource/map/World-1.png')
        self.camera = camera
    def update(self):
        pass

    def handle_events(self, event):
            pass

    def draw(self):
        #global camera
        self.world_1.clip_draw(int(self.camera.x * 320/800), 0, 320, 240, 400, 300, 800, 600)



