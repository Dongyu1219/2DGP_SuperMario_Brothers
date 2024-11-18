from pico2d import load_image, get_time, draw_rectangle
from numbers import ACTION_PER_TIME, M_FRAMES_PER_ACTION, RUN_SPEED_PPS
import game_framework
from state_machine import *
from map import *

class Mario:
    def __init__(self, camera):
            self.x, self.y = 100, 126
            self.world_x = 0
            self.frame = 0
            self.direction = 0
            self.camera = camera

            self.velocity_y = 0  # 중력을 반영한 수직 속도
            self.is_grounded = False  # 블록 위에 있는 상태

            self.image = load_image('resource/mario/small_mario_runningsheet.png')
            self.sit_image = load_image('resource/mario/small_mario_sit_image.png')
            self.jump_image = load_image('resource/mario/small_mario_jump_image.png')
            self.state_machine = StateMachine(self)
            self.state_machine.start(Idle)
            self.state_machine.set_transitions(
                {
                    Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, up_down : Jump, jump_down : Idle},
                    Run: {right_down: Run, left_down: Idle, right_up: Idle, left_up: Idle, time_out: Idle, up_down : Jump},
                    Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle},
                    Jump : {jump_down : Idle, right_down: Jump, left_down: Jump, right_up: Jump, left_up: Jump}
                }
            )


    def update(self):
        self.state_machine.update()
        self.world_x = self.x + self.camera.x
        print(f"Mario: X = {self.x},  Wolrd.x = {self.world_x } , Y = {self.y}")
        #낙하처리
        if not self.is_grounded:
            self.velocity_y -= 1  # 중력 가속도
        self.y += self.velocity_y
        # 바닥에 닿으면 멈춤
        if self.y <= 126:
            self.y = 126
            self.velocity_y = 0
            self.is_grounded = True
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
            draw_rectangle(*self.get_bb_draw())

    def get_bb(self):
        # fill here
        # 네 개의 값, x1, y1, x2, y2
        return self.world_x-20, self.y-50, self.world_x + 20, self.y + 20

    def get_bb_draw(self):
        # fill here
        # 네 개의 값, x1, y1, x2, y2
        return self.x-20, self.y-50, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        left, bottom, right, top = self.get_bb()  # 마리오의 충돌 박스
        if group == 'mario:pipe':
            o_left, o_bottom, o_right, o_top = other.get_bb()

            # 충돌 방향 판별
            if bottom < o_top < top:  # 아래에서 블록 위로 충돌
                self.y = o_top
                self.velocity_y = 0
                self.is_grounded = True
            elif top > o_bottom > bottom:  # 위에서 블록 아래로 충돌
                self.y = o_bottom - (top - bottom)
                self.velocity_y = -1  # 반발력

            # 수평 충돌 처리
            if right > o_left > left:  # 오른쪽 블록과 충돌
                self.world_x = o_left - (right - left)
            elif left < o_right < right:  # 왼쪽 블록과 충돌
                self.world_x = o_right + (right - left)
                
        if group == 'mario:goomba':
            print("collision")
            game_framework.quit()


class Idle:
    @staticmethod
    def enter(mario,e):
        #print('Mario Idle Enter')
        mario.wait_time = get_time()
    @staticmethod
    def exit(mario, e):
        #print('Boy Idle Exit')
        pass
    @staticmethod
    def do(mario):
        if get_time() - mario.wait_time >2:
            mario.state_machine.add_event(('TIME_OUT', 0))
    @staticmethod
    def draw(mario):
        if mario.direction >= 0 :
            mario.image.clip_draw(0, 0, 34, 26, mario.x, mario.y, 100, 100)
        else:
            mario.image.clip_composite_draw(0, 0, 34, 26, 0, 'h', mario.x, mario.y, 100, 100)

class Run:
    @staticmethod
    def enter(mario, e):
        #print('Mario Run Enter')
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            mario.direction = 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN

            mario.direction = -1

    @staticmethod
    def exit(mario, e):
        #print('Mario Sleep Exit')
        pass

    @staticmethod
    def do(mario):
        #
        if mario.x< 200:
            mario.x += mario.direction * RUN_SPEED_PPS//2 * game_framework.frame_time
        mario.frame = (mario.frame + M_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % M_FRAMES_PER_ACTION
        pass

    def draw(mario):
        if mario.direction ==1 :
            mario.image.clip_draw(int(mario.frame)*35, 0, 34, 26, mario.x, mario.y, 100, 100)
        else:
            mario.image.clip_composite_draw(int(mario.frame) * 35, 0, 34, 26, 0, 'h', mario.x, mario.y, 100, 100)
        pass

class Jump:
    @staticmethod
    def enter(mario, e):
        #print('Mario Jump Enter')
        if up_down(e):
            mario.velocity_y = 25
            mario.is_grounded = False

    @staticmethod
    def exit(mario, e):
        #print('Mario Jump Exit')
        pass

    @staticmethod
    def do(mario):
        if mario.is_grounded:
            mario.state_machine.add_event(('JUMP_DOWN', 0))  # 바닥에 닿으면 Idle 상태로 복귀

    def draw(mario):
        if mario.direction ==1 :
            mario.jump_image.draw(mario.x, mario.y, 100, 100)
        else:
            mario.jump_image.composite_draw(0, 'h', mario.x, mario.y, 100, 100)
        pass


class Sleep:
    @staticmethod
    def enter(mario,e):
        #print('Mario Sleep Enter')
        pass
    @staticmethod
    def exit(mario, e):
        #print('Mario Sleep Exit')
        pass
    @staticmethod
    def do(mario):
        pass
    def draw(mario):
        mario.sit_image.draw(mario.x, mario.y, 100, 100)
        pass


