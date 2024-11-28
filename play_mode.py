from pico2d import *

from block import Pipe, Block, Iteam_Block, Break_Block
from camera import Camera
from map import Map_1
from mario import Mario
import game_world
import game_framework
import title_mode
from enemy import Goomba, Flower

#import item_mode

#camera = None

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
    global pipe_house1, pipe_house2, pipe_house3
    global goomba
    global flower1, flower2, flower3
    global block, block2, item_block
    global break_block0, break_block1, break_block2
    global camera

    camera = Camera()
    game_world.add_object(camera, 0)

    map = Map_1(camera)
    game_world.add_object(map, 0)

    goomba = Goomba(camera)
    game_world.add_object(goomba, 1)

    flower1 = Flower(885, 225, camera)
    game_world.add_object(flower1, 1)

    pipe_house1 = Pipe(865, 80, camera)
    game_world.add_object(pipe_house1, 2)

    mario = Mario(camera)
    game_world.add_object(mario, 1)

    block = Block(1060, 220, camera)
    game_world.add_object(block, 2)

    item_block = Iteam_Block(1100, 220, camera)
    game_world.add_object(item_block, 2)

    block2 = Block(1140, 220, camera)
    game_world.add_object(block2, 2)

    flower2 = Flower(2200, 225, camera)
    game_world.add_object(flower2, 1)
    pipe_house2 = Pipe(2180, 80, camera)
    game_world.add_object(pipe_house2, 2)

    for i in range(3):
        break_block = Break_Block(2150 + i * 40, 400, camera)
        game_world.add_object(break_block, 2)

    flower3 = Flower(2400, 225, camera)
    game_world.add_object(flower3, 1)
    pipe_house3 = Pipe(2380, 80, camera)
    game_world.add_object(pipe_house3, 2)

    game_world.add_collision_pair('mario:goomba', mario, None)
    game_world.add_collision_pair('mario:goomba', None, goomba)

    game_world.add_collision_pair('mario:goomba', None, flower1)
    game_world.add_collision_pair('mario:goomba', None, flower2)
    game_world.add_collision_pair('mario:goomba', None, flower3)
    game_world.add_collision_pair('mario:wall', mario, pipe_house1)
    game_world.add_collision_pair('mario:wall', mario, pipe_house2)
    game_world.add_collision_pair('mario:wall', mario, pipe_house3)

    game_world.add_collision_pair('mario:block', mario, block)
    game_world.add_collision_pair('mario:item_block', mario, item_block)
    game_world.add_collision_pair('mario:block', mario, block2)
    game_world.add_collision_pair('mario:block', mario, break_block1)
    game_world.add_collision_pair('mario:block', mario, break_block2)
    game_world.add_collision_pair('mario:block', mario, break_block0)

def finish():
    game_world.clear()
    pass

def update():
    #camera.update()
    game_world.update()
    game_world.handle_collisions()
    if game_world.collide(mario, goomba):
        print("COLLISION mario:goomba")
    if game_world.collide(mario, block):
        print("BLOCK COLLIDE")
    if game_world.collide(mario, pipe_house1):
        pass
        #print("WALL COLLIDE")
        #camera.stop_movement()

def draw():

    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.02)

def pause():
    pass

def resume():
    pass
