from pico2d import load_image

from state_machine import StateMachine

class Idle:
    @staticmethod
    def enter(mario):
        print('Mario Idle Enter')
    @staticmethod
    def exit(boy):
        print('Boy Idle Exit')
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class Mario:
    def __init__(self):
            self.x, self.y = 100, 126
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
            self.state_machine = StateMachine(self)
    def update(self):
        self.frame = (self.frame+1) %4
        pass

    def handle_event(self):
        pass

    def draw(self):
            self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)
