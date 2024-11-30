from pico2d import *

from block import Iteam_Block
from camera2 import Camera
from item import Item
from map import Map_1, Boss_Map
from mario import Mario
import game_world
import game_framework
import title_mode
from enemy import Goomba, Flower
#import item_mode
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
    global block, item_block
    global camera
    global map
    global mario
    global item

    camera = Camera()
    game_world.add_object(camera, 0)

    map = Boss_Map(camera)
    game_world.add_object(map, 0)

    mario = Mario(camera)
    game_world.add_object(mario, 2)

    item_block = Iteam_Block(1100, 220, camera)
    game_world.add_object(item_block, 2)

    item = Item(1100, 220, camera)
    game_world.add_object(item, 1)

    game_world.add_collision_pair('mario:item', mario, item)
    game_world.add_collision_pair('mario:item_block', mario, item_block)

def finish():
    game_world.clear()
    pass

def update():
    #camera.update()
    game_world.update()
    game_world.handle_collisions()

def draw():

    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.02)

def pause():
    pass

def resume():
    pass
