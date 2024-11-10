from pico2d import *
import game_world
from map import Map_1
from mario import Mario

# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             game_framework.change_mode(title_mode)
#         elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
#             game_framework.push_mode(item_mode)
#         else:
#             boy.handle_event(event)
#

def init():
    global mario

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

def pause():
    pass

def resume():
    pass

