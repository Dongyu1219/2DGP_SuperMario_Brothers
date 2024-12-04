import random
from pico2d import *
import time
from block import Iteam_Block, Block
from camera2 import Camera
from item import Item, Fire_Item
from map import Boss_Map
from mario import Mario
import game_world
import game_framework
import title_mode
from boss import Lava, Koopa, Killer, Boss_Goomba
from princess import Peach

#import item_mode

last_killer_spawn_time = 0
killer_spawn_interval = 4
last_goomba_spawn_time = 0
goomba_spawn_interval = 3

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
    global koopa
    global peach

    camera = Camera()
    game_world.add_object(camera, 0)

    map = Boss_Map(camera)
    game_world.add_object(map, 0)

    mario = Mario(camera)
    game_world.add_object(mario, 2)

    item_block = Iteam_Block(1100, 220, camera)
    game_world.add_object(item_block, 2)
    item = Fire_Item(1100, 220, camera)
    game_world.add_object(item, 1)

    lava_positions = [1700, 1800, 1950, 2100, 2250, 2300]  # 용암 위치 리스트
    lavas = []  # 생성된 Lava 객체를 저장할 리스트
    for pos in lava_positions:
        lava = Lava(pos, camera)
        game_world.add_object(lava, 1)
        lavas.append(lava)
    for lava in lavas:
        game_world.add_collision_pair('mario:goomba', mario, lava)

    block_positions = [1700, 1800, 1950, 2200]
    blocks = []  # 생성된 Lava 객체를 저장할 리스트
    for poss in block_positions:
        block = Block(poss, 100,  camera)
        game_world.add_object(block, 2)
        blocks.append(block)
    for block in blocks:
        game_world.add_collision_pair('mario:block', mario, block)

    koopa = Koopa(3000, 155 ,camera)
    game_world.add_object(koopa, 2)

    peach = Peach(3000, 60, camera)
    game_world.add_object(peach, 1)

    game_world.add_collision_pair('mario:goomba', mario, koopa)
    game_world.add_collision_pair('goomba:ball', koopa, None)

    game_world.add_collision_pair('mario:fire_item', mario, item)
    game_world.add_collision_pair('mario:item_block', mario, item_block)


def finish():
    game_world.clear()
    pass

def update():
    #camera.update()
    global camera
    game_world.update()
    game_world.handle_collisions()
    spawn_killer()
    #print(camera.x)
    if camera.x > 2000:
        spawn_goomba()

def draw():

    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.02)

def pause():
    pass

def resume():
    pass

def spawn_killer():
    global last_killer_spawn_time
    current_time = time.time()
    if current_time - last_killer_spawn_time >= killer_spawn_interval:
        random_y = random.randint(150, 400)
        killer = Killer(3500, random_y, camera)
        game_world.add_object(killer, 2)
        game_world.add_collision_pair('mario:goomba', None, killer)
        game_world.add_collision_pair('goomba:ball', killer, None)
        print(f"Killer spawned at x=3000, y={random_y}")
        last_killer_spawn_time = current_time

def spawn_goomba():
    global last_goomba_spawn_time
    current_time = time.time()
    if current_time - last_goomba_spawn_time >= goomba_spawn_interval:
        boss_goomba = Boss_Goomba(3200, 110, camera)
        game_world.add_object(boss_goomba, 1)
        game_world.add_collision_pair('mario:goomba', None, boss_goomba)
        game_world.add_collision_pair('goomba:ball', boss_goomba, None)
        print(f"Killer spawned at x=3000, y={155}")
        last_goomba_spawn_time = current_time