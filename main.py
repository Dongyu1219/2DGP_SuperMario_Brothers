import opening
from pico2d import *

open_canvas()
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            running = False
            break


close_canvas()
