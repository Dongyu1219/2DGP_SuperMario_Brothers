from pico2d import *
from map import Map_1
from mario import Mario
import game_world

def handle_events():
    global running
    global direction

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


def reset_world():
    global running
    global mario, map
    global direction
    direction = 0

    running = True

    map = Map_1()
    game_world.add_object(map, 0)

    mario = Mario()
    game_world.add_object(mario, 1)

def update_world():
    # map.update()
    # for o in world:
    #     o.update()
    game_world.update()
    pass

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()

#게임 루프
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.02)

close_canvas()
