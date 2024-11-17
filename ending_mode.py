from pico2d import load_image, get_events, clear_canvas, update_canvas
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE
import play_mode
from mario import Mario
from numbers import M_FRAMES_PER_ACTION, ACTION_PER_TIME


def init():
    global end_image, mario_image, mario_sit, mario_jump
    global frame, end_mode
    global x, y
    frame, x, y = 0, 0, 0
    end_mode = 1
    end_image = load_image('resource/map/World-1.png')
    mario_image = Mario().image
    mario_sit = Mario().sit_image
    mario_jump = Mario().jump_image
def finish():
    global end_image
    del end_image

def update():
    global frame, x, y, end_mode
    frame = (frame + M_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % M_FRAMES_PER_ACTION
    if x < 40:
        x += 0.1
    elif x < 180:
        end_mode = 2
        x += 0.8
        y += 1
    elif x < 240:
        end_mode = 3
        y -= 0.2
        if y < 90:
            end_mode = 4
        if y <= 0:
            y = 0
            end_mode = 1
            x = 240
    elif x >= 240 and x < 440:
        x += 0.3
    elif x > 440:
        end_mode = 5

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
    if end_mode==1:
        mario_image.clip_draw(35*int(frame), 0, 34, 26, 100+x, 126, 100, 100)
    elif end_mode ==2:
        mario_jump.draw(100+x, 126+y, 100, 100)
    elif end_mode == 3:
        mario_sit.draw(100+x, 126+y, 100, 100)
    elif end_mode == 4:
        mario_sit.clip_composite_draw(0, 0, 34, 26, 0, 'h', 130+x, 126+y, 100, 100)
    update_canvas()

