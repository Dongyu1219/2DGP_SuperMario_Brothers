from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

from state_machine import *


class Idle:
    @staticmethod
    def enter(mario,e):
        print('Mario Idle Enter')
        mario.frame = 0
        mario.wait_time = get_time()
    @staticmethod
    def exit(mario, e):
        print('Boy Idle Exit')
    @staticmethod
    def do(mario):
        mario.frame = (mario.frame + 1) % 4
        if get_time() - mario.wait_time >2:
            mario.state_machine.add_event(('TIME_OUT', 0))
    @staticmethod
    def draw(mario):
        mario.image.clip_draw(mario.frame*35, 0, 34, 26, mario.x, mario.y, 100, 100)

class Sleep:
    @staticmethod
    def enter(mario,e):
        print('Mario Sleep Enter')
    @staticmethod
    def exit(mario, e):
        print('Mario Sleep Exit')
        pass
    @staticmethod
    def do(mario):
        pass
    def draw(mario):
        mario.sit_image.draw(mario.x, mario.y, 100, 100)
        pass


class Mario:
    def __init__(self):
            self.x, self.y = 100, 126
            self.frame = 0
            self.image = load_image('small_mario_runningsheet.png')
            self.sit_image = load_image('small_mario_sit_image.png')
            self.state_machine = StateMachine(self)
            self.state_machine.start(Idle)
            self.state_machine.set_transitions(
                {
                    Idle: {time_out : Sleep},
                    Sleep : {space_down: Idle}
                }
            )
    def update(self):
        self.state_machine.update()
        #self.frame = (self.frame+1) %4
        pass

    def handle_event(self, event):
        #튜플을 이용해서 이벤트 상태 나타내기
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
            self.state_machine.draw()
            #self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)
