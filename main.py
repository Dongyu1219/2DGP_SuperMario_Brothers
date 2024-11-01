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
            self.x, self.y = 50, 90
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
    def update(self):
        self.frame = (self.frame+1) %4
        self.x += direction *10
        pass
            # self.x += 5
    def draw(self):
            self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, 132, 100, 100)

class World_1:
    def __init__(self):
        self.x, self.y
    pass

def handle_events():
    global running
    global direction

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction+=1
                pass
            elif event.key == SDLK_LEFT:
                direction-=1
                pass
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direction -=1
            elif event.key == SDLK_LEFT:
                direction +=1


def reset_world():
    global running
    global mario, direction
    direction = 0
    #global world

    running = True
    #world = []

    mario = Mario()
    #world.append(mario)


def update_world():
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
