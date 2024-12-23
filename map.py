from pico2d import load_image, load_music
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT
class Map_1:
    def __init__(self, camera):
        self.world_1 = load_image('resource/map/World-1.png')
        self.camera = camera
        self.bgm = load_music('sound/BGM1.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
    def update(self):
        pass

    def handle_events(self, event):
        pass

    def draw(self):
        global camera
        #2500
        self.world_1.clip_draw(int(self.camera.x * 320/800), 0, 320, 240, 400, 300, 800, 600)
        #self.world_1.clip_draw(int(self.camera.x), 0, 320, 240, 400, 300, 800, 600)
        pass

class Boss_Map:
    def __init__(self, camera):
        self.boss_world = load_image('resource/map/boss_map.png')
        self.camera = camera
        self.bgm = load_music('sound/boss_BGM.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
    def update(self):
        pass

    def handle_events(self, event):
        pass

    def draw(self):
        global camera
        #2500
        self.boss_world.clip_draw(int(self.camera.x * 320/800), 0, 320, 240, 400, 300, 800, 600)
        #self.world_1.clip_draw(int(self.camera.x), 0, 320, 240, 400, 300, 800, 600)
        pass

