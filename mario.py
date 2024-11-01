from pico2d import load_image

from state_machine import StateMachine

class Idle:
    @staticmethod
    def enter(mario):
        print('Mario Idle Enter')
        mario.frame = 0
    @staticmethod
    def exit(mario):
        print('Boy Idle Exit')
    @staticmethod
    def do(mario):
        mario.frame = (mario.frame + 1) % 4
    @staticmethod
    def draw(mario):
        mario.mario.clip_draw(mario.frame*35, 0, 34, 26, mario.x, mario.y, 100, 100)


class Mario:
    def __init__(self):
            self.x, self.y = 100, 126
            self.frame = 0
            self.mario = load_image('small_mario_runningsheet.png')
            self.state_machine = StateMachine(self)
            self.state_machine.start(Idle)
    def update(self):
        self.state_machine.update()
        #self.frame = (self.frame+1) %4
        pass

    def handle_event(self):
        pass

    def draw(self):
            self.state_machine.draw()
            #self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)
