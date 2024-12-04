import game_framework
import start02
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time

def init():
    global image
    global logo_start_time
    global running

    image = load_image('resource/opening/nintendo1.png')
    running = True
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global running
    global logo_start_time
    if get_time()-logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(start02)

def draw():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()

def handle_events():
    events = get_events()

