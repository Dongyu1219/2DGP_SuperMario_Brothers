from pico2d import *
from map import Map_1
from mario import Mario
import game_world

def handle_events():

    global direction
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                # input 이벤트를 mario 가 처리
                mario.handle_event(event)
                map.handle_events(event)


def init():
    global mario
    global map
    global running
    running = True

    map = Map_1()
    game_world.add_object(map, 0)

    mario = Mario()
    game_world.add_object(mario, 1)

def finish():
    #game_world.clear()
    pass

def update():
    game_world.update()

def draw():

    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas()
init()
while running:
    handle_events()
    update()
    draw()
    delay(0.01)
    finish()

def pause():
    pass

def resume():
    pass

