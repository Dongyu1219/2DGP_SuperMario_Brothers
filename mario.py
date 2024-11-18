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
        #print(f"Mario: X = {self.x},  Wolrd.x = {self.world_x } , Y = {self.y}")
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
            pass
            # o_left, o_bottom, o_right, o_top = other.get_bb()
            #
            # overlap_top = top - o_top
            # overlap_bottom = o_bottom - bottom
            # overlap_left = o_left - left
            # overlap_right = right - o_right
            #
            # # 가장 작은 겹치는 방향으로 위치 고정
            # if min(overlap_top, overlap_bottom, overlap_left, overlap_right) == overlap_top:
            #     self.y = o_top + 20
            #     self.jump_speed = 0  # 점프 멈춤
            # elif min(overlap_top, overlap_bottom, overlap_left, overlap_right) == overlap_bottom:
            #     self.y = o_bottom - 20
            # elif min(overlap_top, overlap_bottom, overlap_left, overlap_right) == overlap_left:
            #     self.world_x = o_left - 20
            # elif min(overlap_top, overlap_bottom, overlap_left, overlap_right) == overlap_right:
            #     self.world_x = o_right + 20
                
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
            mario.jump_start_y = mario.y
            mario.jump_speed = 20
            pass

    @staticmethod
    def exit(mario, e):
        #print('Mario Jump Exit')
        pass

    @staticmethod
    def do(mario):
        mario.y += mario.jump_speed
        mario.jump_speed -=1
        if mario.y <= mario.jump_start_y:
            mario.y = mario.jump_start_y
            mario.state_machine.add_event(('JUMP_DOWN', 0))

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


