import game_framework
from pico2d import open_canvas, delay, close_canvas
import title_mode as start_mode

open_canvas()
game_framework.run(start_mode)
close_canvas()

