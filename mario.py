from pico2d import load_image, get_time

from state_machine import *

class Mario:
    def __init__(self):
            self.x, self.y = 100, 126
            self.frame = 0
            self.direction = 0
            self.image = load_image('small_mario_runningsheet.png')
            self.sit_image = load_image('small_mario_sit_image.png')
            self.jump_image = load_image('small_mario_jump_image.png')
            self.state_machine = StateMachine(self)
            self.state_machine.start(Idle)
            self.state_machine.set_transitions(
                {
                    Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, up_down : Jump},
                    Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, time_out: Idle, up_down : Jump},
                    Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle},
                    Jump : {right_down: Run, left_down: Run, left_up: Run, right_up: Run}
                }
            )
    def update(self):
        self.state_machine.update()
        #self.frame = (self.frame+1) %4
        pass

    def handle_event(self, event):
        #튜플을 이용해서 이벤트 상태 나타내기
        self.state_machine.add_event(
            ('INPUT', event)
        )
        pass

    def draw(self):
            self.state_machine.draw()
            #self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)


class Idle:
    @staticmethod
    def enter(mario,e):
        print('Mario Idle Enter')
        mario.wait_time = get_time()
    @staticmethod
    def exit(mario, e):
        print('Boy Idle Exit')
    @staticmethod
    def do(mario):
        if get_time() - mario.wait_time >2:
            mario.state_machine.add_event(('TIME_OUT', 0))
    @staticmethod
    def draw(mario):
        mario.image.clip_draw(0, 0, 34, 26, mario.x, mario.y, 100, 100)

class Run:
    @staticmethod
    def enter(mario, e):
        print('Mario Run Enter')
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pass
            #mario.direction = 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pass
            #mario.direction = -1

    @staticmethod
    def exit(mario, e):
        print('Mario Sleep Exit')
        pass

    @staticmethod
    def do(mario):
        mario.x += mario.direction*5
        mario.frame = (mario.frame+1)%4
        pass

    def draw(mario):
        mario.image.clip_draw(mario.frame*35, 0, 34, 26, mario.x, mario.y, 100, 100)
        pass

class Jump:
    @staticmethod
    def enter(mario, e):
        print('Mario Jump Enter')
        if up_down(e):
            mario.jump_start_y = mario.y
            mario.jump_speed = 15
            pass

    @staticmethod
    def exit(mario, e):
        print('Mario Jump Exit')
        pass

    @staticmethod
    def do(mario):
        mario.y += mario.jump_speed
        mario.jump_speed -=1
        if mario.y <= mario.jump_start_y:
            mario.y = mario.jump_start_y
            mario.state_machine.add_event(('up_up', Idle))  # 점프 종료 후 Idle 상태로 전환
        pass

    def draw(mario):
        mario.jump_image.draw(mario.x, mario.y, 100, 100)
        pass

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


