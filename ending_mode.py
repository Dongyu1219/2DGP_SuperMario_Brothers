from pico2d import load_image, get_events, clear_canvas, update_canvas
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE
import play_mode
from mario import Mario
from numbers import M_FRAMES_PER_ACTION, ACTION_PER_TIME


def init():
    global end_image
    global mario_image
    global mario_sit
    global mairo_jump
    global frame
    global x
    global y
    frame, x, y = 0, 0, 0
    end_image = load_image('resource/map/World-1.png')
    mario_image = Mario().image
    mario_sit = Mario().sit_image
    mario_jump = Mario().jump_image
def finish():
    global end_image
    del end_image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    end_image.clip_draw(1180, 0, 320, 240, 400, 300, 800, 600)
    mario_image.clip_draw(35*int(frame), 0, 34, 26, 100+x, 126, 100, 100)
    update_canvas()

def update():
    global frame
    frame = (frame + M_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % M_FRAMES_PER_ACTION
    pass