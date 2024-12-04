from pico2d import *

from block import Pipe, Block, Iteam_Block, Break_Block, Wall
from camera import Camera
from item import Item
from map import Map_1
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
    global wall1, wall2, wall3, wall4
    global goomba
    global block, item_block
    global camera
    global map
    global mario
    global item
    global flower1, flower3, flower4
    global pipe_house1, pipe_house2, pipe_house3, pipe_house4

    game_world.clear()  # game_world에서 모든 객체 삭제

    camera = Camera()
    game_world.add_object(camera, 0)

    map = Map_1(camera)
    game_world.add_object(map, 0)

    goomba = Goomba(camera)
    game_world.add_object(goomba, 1)

    flower1 = Flower(885, 225, 6, camera)
    game_world.add_object(flower1, 1)

    pipe_house1 = Pipe(865, 80, camera)
    game_world.add_object(pipe_house1, 2)

    mario = Mario(camera)
    game_world.add_object(mario, 2)

    item_block = Iteam_Block(1100, 220, camera)
    game_world.add_object(item_block, 2)

    item = Item(1100, 220, camera)
    game_world.add_object(item, 1)

    # flower2 = Flower(2200, 225, camera)
    # game_world.add_object(flower2, 1)
    pipe_house2 = Pipe(2180, 80, camera)
    game_world.add_object(pipe_house2, 2)

    break_block_positions = [2150, 2190, 2230]
    break_blocks = []  # 생성된 객체를 저장할 리스트
    for poss in break_block_positions:
        block = Break_Block(poss, 400, camera)
        game_world.add_object(block, 2)
        break_blocks.append(block)
    for block in break_blocks:
        game_world.add_collision_pair('mario:block', mario, block)

    flower3 = Flower(2450, 225, 6, camera)
    game_world.add_object(flower3, 1)
    pipe_house3 = Pipe(2430, 80, camera)
    game_world.add_object(pipe_house3, 2)

    flower4 = Flower(2700, 225, 2, camera)
    game_world.add_object(flower4, 1)
    pipe_house4 = Pipe(2680, 80, camera)
    game_world.add_object(pipe_house4, 2)

    #충돌처리
    game_world.add_collision_pair('mario:goomba', mario, None)
    game_world.add_collision_pair('mario:goomba', None, goomba)

    pipe_houses = [pipe_house1, pipe_house2, pipe_house3, pipe_house4]
    for pipe_house in pipe_houses:
        game_world.add_collision_pair('mario:pipe_house', mario, pipe_house)

    flowers = [flower1, flower3, flower4]
    for flower in flowers:
        game_world.add_collision_pair('mario:goomba', mario, flower)

    game_world.add_collision_pair('mario:item', mario, item)
    game_world.add_collision_pair('mario:item_block', mario, item_block)


def finish():
    game_world.clear()
    pass

def update():
    #camera.update()
    game_world.update()
    game_world.handle_collisions()
    if game_world.collide(mario, goomba):
        pass
        #print("COLLISION mario:goomba")
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
