from pico2d import *

class Opening:
    def __init__(self):
        self.opening = load_image('opening_image.png')
        self.screen_size = 260
        pass
    def draw(self):
        self.opening.draw_now(260, 260, self.screen_size, self.screen_size)
    def update(self):
        pass

class Mario:
    def __init__(self):
            self.x, self.y = 0, 90
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
    def update(self):
        self.frame = (self.frame+1) %4
        pass
            # self.x += 5
    def draw(self):
            self.mario.clip_draw(self.frame*35, 0, 34, 26, 200, 132, 100, 100)

class World_1:
    def __init__(self):
        self.x, self.y
    pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            break

def reset_world():
    global running
    global mario
    global opening
    #global world

    running = True
    #world = []

    mario = Mario()
    opening = Opening()
    #world.append(mario)


def update_world():
    # for o in world:
    #     o.update()
    mario.update()
    pass

def render_world():
    clear_canvas()
    # for o in world:
    #     o.draw()
    mario.draw()
    opening.draw()
    update_canvas()

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)

close_canvas()
