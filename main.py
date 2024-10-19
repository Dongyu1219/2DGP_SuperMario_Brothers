from pico2d import *

open_canvas()
running = True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            running = False
            break;

while running:
        handle_events()
        update_canvas()


close_canvas()