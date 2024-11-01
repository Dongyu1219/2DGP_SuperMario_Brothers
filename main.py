import opening
from pico2d import *

class Mario:
    def __init__(self):
            self.x, self.y = 0, 90
            self.frame = 0
            self.image = load_image('mario_image.png')
    def update(self):
        self.frame = (self.frame+1) %8
        pass
            # self.x += 5
    def draw(self):
            self.image.draw_now(400,30)

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
    #global world

    running = True
    #world = []

    mario = Mario()
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
    update_canvas()

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()
