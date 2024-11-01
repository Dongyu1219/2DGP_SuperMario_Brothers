# import pygame
# from pico2d import *
#
# screen_size = 260
# open_canvas()
# opening = load_image('opening_image.png')
#
# def draw_opening_page():
#
#     opening.draw(screen_size, screen_size)
#     update_canvas()
#     delay(3)
#     close_canvas()
#
# draw_opening_page()
from pico2d import load_image


class Opening:
    def __init__(self):
        self.opening = load_image('opening_image.png')
        self.screen_size = 260
        pass
    def draw(self):
        self.opening.draw_now(260, 260, self.screen_size, self.screen_size)
    def update(self):
        pass
