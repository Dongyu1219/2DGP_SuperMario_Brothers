from pico2d import load_image, get_events, clear_canvas, update_canvas
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_world
import mario
import play_mode

def init():
    global image
    image = load_image('resource/opening/game_over_image.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_world.clear()

            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    image.clip_draw(0, 0, 320, 267, 400, 300, 800, 600)
    update_canvas()

def update():
    pass