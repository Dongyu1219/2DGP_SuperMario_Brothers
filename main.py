from pico2d import *
from map import Map_1
from mario import Mario

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
    global mario, map
    global direction
    direction = 0
    global world

    running = True
    world = []

    map = Map_1()
    world.append(map)

    mario = Mario()
    world.append(mario)

def update_world():
    map.x += direction * 20
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
         o.draw()
    update_canvas()


open_canvas()
reset_world()

#게임 루프
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()
