from sdl2 import SDL_QUIT

import game_framework
import title_mode
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events

def init():
    global image

    image = load_image('resource/opening/tuk_credit.png')

def finish():
    global image

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

