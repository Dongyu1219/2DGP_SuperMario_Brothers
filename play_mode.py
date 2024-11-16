from pico2d import *

from camera import Camera
from map import Map_1
from mario import Mario
import game_world
import game_framework
import title_mode
from enemy import Goomba
#import item_mode

camera = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
        #     game_framework.push_mode(item_mode)
        else:
            mario.handle_event(event)
            map.handle_events(event)
            camera.handle_events(event)

def init():
    global mario
    global map
    global goomba
    global camera

    camera = Camera()

    map = Map_1(camera)
    game_world.add_object(map, 0)

    goomba = Goomba()
    game_world.add_object(goomba, 1)

    mario = Mario()
    game_world.add_object(mario, 1)

def finish():
    game_world.clear()
    pass

def update():
    camera.update()
    game_world.update()


def draw():

    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.02)

def pause():
    pass

def resume():
    pass
