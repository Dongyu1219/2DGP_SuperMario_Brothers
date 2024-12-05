from asyncio import Runner
#this is main
from pico2d import load_image, get_time, draw_rectangle, delay, load_wav

import game_over
import game_world
import logo_mode
from ball import Ball
from numbers import ACTION_PER_TIME, M_FRAMES_PER_ACTION, RUN_SPEED_PPS
import game_framework
from state_machine import *

from map import *

class Mario:
    fireball_sound = None
    up_sound = None
    down_sound = None
    block_hit_sound = None
    jump_sound = None
    death_sound = None

    def __init__(self, camera):
            self.x = 100
            self.y = 126
            self.world_x = 0
            self.frame = 0
            self.direction = 0
            self.die = True
            self.camera = camera
            self.tall = 0
            self.big_Mode = False
            self.fire_mode = False

            self.velocity_y = 0
            self.is_grounded = False
            self.is_jumping = False
            self.meet_peach = False  # 공주와 만났는지 상태를 저장하는 플래그

            self.image = load_image('resource/mario/small_mario_runningsheet.png')
            self.sit_image = load_image('resource/mario/small_mario_sit_image.png')
            self.jump_image = load_image('resource/mario/small_mario_jump_image.png')
            self.die_image = load_image('resource/mario/small_mario_die_image.png')
            self.fire_mode_image = load_image('resource/mario/small_mario_fire_runningsheet.png')
            self.fire_mode_jump_image = load_image('resource/mario/small_mario_fire_jump_image.png')
            self.state_machine = StateMachine(self)
            self.state_machine.start(Idle)
            self.state_machine.set_transitions(
                {
                    Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, up_down : Jump, jump_down : Idle, left_stop : Idle, right_stop: Idle, die: Die, space_down: Idle},
                    Run: {right_down: Run, left_down: Idle, right_up: Idle, left_up: Idle, time_out: Idle, up_down : Jump, right_stop : Right_Stop, left_stop : Left_Stop, die: Die, space_down: Run},
                    Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle, die: Die},
                    Jump : {jump_down : Idle, right_down: Jump, left_down: Jump, right_up: Jump, left_up: Jump, die: Die, space_down: Jump},
                    Left_Stop : {right_down: Run, left_down: Left_Stop, left_up: Left_Stop, right_up: Run, up_down : Jump, jump_down : Idle},
                    Right_Stop : {right_down: Right_Stop, left_down: Run, left_up: Run, right_up: Right_Stop, up_down : Jump, jump_down : Idle},
                    Die : {die : Die}
                }
            )

            if not Mario.fireball_sound:
                Mario.fireball_sound = load_wav('sound/fireball.wav')
                Mario.fireball_sound.set_volume(32)

                Mario.up_sound = load_wav('sound/power_up.wav')
                Mario.up_sound.set_volume(32)
                Mario.down_sound = load_wav('sound/power_down.wav')
                Mario.down_sound.set_volume(32)

                Mario.block_hit_sound = load_wav('sound/block_hit.wav')
                Mario.block_hit_sound.set_volume(32)

                Mario.jump_sound = load_wav('sound/jump.wav')
                Mario.jump_sound.set_volume(32)

                Mario.death_sound = load_wav('sound/death.wav')
                Mario.death_sound.set_volume(32)

    def update(self):
        self.state_machine.update()
        self.world_x = self.x + self.camera.x
        if self.meet_peach:  # 공주와 만난 경우
            game_framework.change_mode(logo_mode)
            return  # 상태 전환 후 더 이상 처리하지 않음
        #print(f"Mario: X = {self.x},  Wolrd.x = {self.world_x } , Y = {self.y}")                                   #위치 디버깅
        if not self.is_grounded:
            self.velocity_y -= 1
        self.y += self.velocity_y
        if self.world_x > 1300 and self.world_x < 1380:
            self.is_grounded = False

        elif self.y <= 126 and self.die:
            self.y = 126
            self.velocity_y = 0
            self.is_grounded = True
        else:
            self.is_grounded = False

    def handle_event(self, event):
        self.state_machine.add_event(
            ('INPUT', event)
        )
        pass

    def draw(self):
            self.state_machine.draw()
            #self.mario.clip_draw(self.frame*35, 0, 34, 26, self.x, self.y, 100, 100)
            #draw_rectangle(*self.get_bb_draw())

    def fire_ball(self):
        if self.fire_mode:
            ball = Ball(self.x, self.y, self.direction * 10, self.world_x)
            game_world.add_object(ball, 2)
            Mario.fireball_sound.play()
            game_world.add_collision_pair('goomba:ball', None, ball)


    def get_bb(self):
        return self.world_x-20, self.y-50, self.world_x + 20, self.y + 20

    def get_bb_draw(self):
        return self.x-20, self.y-45, self.x + 20, self.y + 20 + self.tall//2

    def handle_collision(self, group, other):
        left, bottom, right, top = self.get_bb()  # 마리오의 충돌 박스
        o_left, o_bottom, o_right, o_top = other.get_bb()
        #o_left, o_bottom, o_right, o_top = other.get_bb_draw()

        if group == 'mario:block':
            # 충돌 방향 판별
            if bottom < o_top < top:  # 아래에서 블록 위로 충돌
                self.y = o_top +45
                self.velocity_y = 0
                self.is_grounded = True
            elif top > o_bottom > bottom:  # 위에서 블록 아래로 충돌
                self.y = o_bottom - (top - bottom)
                Mario.block_hit_sound.play()
                self.velocity_y = -1  # 반발력
            # 수평 충돌 처리
            if right > o_left > left:  # 오른쪽 블록과 충돌
                self.world_x = o_left - (right - left)
            elif left < o_right < right:  # 왼쪽 블록과 충돌
                self.world_x = o_right + (right - left)

        if group == 'mario:item_block':
            if bottom < o_top < top:
                self.y = o_top +45
                self.velocity_y = 0
                self.is_grounded = True
            elif top > o_bottom > bottom:  # 위에서 블록 아래로 충돌
                self.y = o_bottom - (top - bottom)
                self.velocity_y = -1
                Mario.block_hit_sound.play()
                other.hit = False
                other.is_rising = True
                other.rise_start_time = get_time()  # 충돌 시점 시간 기록
            # 수평 충돌 처리
            if right > o_left > left:  # 오른쪽 블록과 충돌
                self.world_x = o_left - (right - left)
            elif left < o_right < right:  # 왼쪽 블록과 충돌
                self.world_x = o_right + (right - left)

        if group == 'mario:item':
            if top > o_bottom > bottom:  # 위에서 블록 아래로 충돌
                other.creating = 1
            if other.hit > 1:
                print(f'other.hit')
                #delay(1.0)
                Mario.up_sound.play()
                self.tall = 60
                self.big_Mode = True

        if group == 'mario:fire_item':
            if top > o_bottom > bottom:  # 위에서 블록 아래로 충돌
                other.creating = 1
            if other.hit > 1:
                print(f'other.hit')
                #delay(1.0)
                Mario.up_sound.play()
                self.fire_mode = True

        if group == 'mario:pipe_house':
            # 벽 위로 올라갈 때
            if bottom < o_top+40 < top and right > o_left-10 and left < o_right+10 and self.die :
                if self.velocity_y <= 0:
                    self.y = o_top+40
                    self.velocity_y = 0
                    self.is_grounded = True
                return

            # 벽의 왼쪽과 충돌
            if right > o_left+1  > left and self.die:
                self.world_x = o_left+10 - (right - left)
                self.x = self.world_x - self.camera.x
                self.state_machine.add_event(('RIGHT_STOP', 0))
                print("Right collision with wall")


            # 벽의 오른쪽과 충돌
            if left < o_right-1 < right and self.die:
                self.world_x = o_right-10 + (right - left)
                self.x = self.world_x - self.camera.x
                self.state_machine.add_event(('LEFT_STOP', 0))
                print("Left collision with wall")

        if group == 'mario:wall':
            # 벽 위로 올라갈 때
            if bottom < o_top+40 < top and right > o_left-10 and left < o_right+10 and self.die :
                if self.velocity_y <= 0:
                    self.y = o_top+40
                    self.velocity_y = 0
                    self.is_grounded = True
                return

            # 벽의 왼쪽과 충돌
            if right > o_left+10  > left and self.die:
                self.world_x = o_left+10 - (right - left)
                self.x = self.world_x - self.camera.x
                self.state_machine.add_event(('RIGHT_STOP', 0))
                print("Right collision with wall")


            # 벽의 오른쪽과 충돌
            if left < o_right-10 < right and self.die:
                self.world_x = o_right-10 + (right - left)  # 위치 보정
                self.x = self.world_x - self.camera.x  # 로컬 좌표도 업데이트
                self.state_machine.add_event(('LEFT_STOP', 0))
                print("Left collision with wall")

        if group == 'mario:goomba':
            print("collision")
            if (self.big_Mode == False):
                self.state_machine.add_event(('DIE', 0))
            else:
                Mario.down_sound.play()
                self.big_Mode = False
                self.tall = 0
            #game_framework.quit()

        if group == 'mario:peach':
            print("prince collide ")
            self.meet_peach = True

class Die:
    @staticmethod
    def enter(mario, e):
        #print('Mario Die Enter')
        Mario.death_sound.play()
        mario.velocity_y = 10  # 초기 수직 속도
        mario.die = False
        mario.die_start_time = get_time()  # 죽기 시작한 시간 기록
        pass

    @staticmethod
    def exit(mario, e):
        #print('Mario Sleep Exit')
        pass

    @staticmethod
    def do(mario):
        mario.y += mario.velocity_y
        mario.velocity_y -= 0.3


        if get_time() - mario.die_start_time >= 2.0:
            game_framework.change_mode(game_over)
        pass

    def draw(mario):
        mario.die_image.draw(mario.x, mario.y, 100, 100)
        pass


class Idle:
    @staticmethod
    def enter(mario,e):
        #print('Mario Idle Enter')
        mario.wait_time = get_time()
    @staticmethod
    def exit(mario, e):
        #print('Boy Idle Exit')
        if space_down(e):
            mario.fire_ball()
        pass
    @staticmethod
    def do(mario):
        if get_time() - mario.wait_time >5:
            mario.state_machine.add_event(('TIME_OUT', 0))
    @staticmethod
    def draw(mario):
        if (mario.fire_mode):
            if mario.direction >= 0:
                mario.fire_mode_image.clip_draw(0, 0, 34, 26, mario.x, mario.y , 100, 100)
            else:
                mario.fire_mode_image.clip_composite_draw(0, 0, 34, 26, 0, 'h', mario.x, mario.y, 100,
                                                100)
        else :
            if mario.direction >= 0 :
                mario.image.clip_draw(0, 0, 34, 26, mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)
            else:
                mario.image.clip_composite_draw(0, 0, 34, 26, 0, 'h', mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)


class Left_Stop:
    @staticmethod
    def enter(mario,e):
        mario.direction = -1
        mario.camera.stop_movement()
        #print('Mario Left_Stop Enter')
        pass
    @staticmethod
    def exit(mario, e):
        mario.camera.resume_movement()
        #print('Mario Stop Exit')
    @staticmethod
    def do(mario):
        pass
    def draw(mario):
        mario.image.clip_composite_draw(0, 0, 34, 26, 0, 'h', mario.x, mario.y, 100, 100)

class Right_Stop:
    @staticmethod
    def enter(mario,e):
        mario.direction = 0
        mario.camera.stop_movement()
        #print('Mario Right_Stop Enter')
        pass
    @staticmethod
    def exit(mario, e):
        mario.camera.resume_movement()
        #print('Mario Stop Exit')
    @staticmethod
    def do(mario):
        pass
    def draw(mario):
        mario.image.clip_draw(0, 0, 34, 26, mario.x, mario.y, 100, 100)


class Run:
    @staticmethod
    def enter(mario, e):
        #print('Mario Run Enter')
        mario.camera.resume_movement()
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            mario.direction = 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN

            mario.direction = -1

    @staticmethod
    def exit(mario, e):
        if space_down(e):
            mario.fire_ball()
        pass

    @staticmethod
    def do(mario):
        if mario.x < 250:
            mario.x += mario.direction * RUN_SPEED_PPS // 2 * game_framework.frame_time
        mario.frame = (mario.frame + M_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % M_FRAMES_PER_ACTION
        pass

    def draw(mario):
        if (mario.fire_mode):
            if mario.direction == 1:
                mario.fire_mode_image.clip_draw(int(mario.frame) * 35, 0, 34, 26, mario.x, mario.y + mario.tall // 3, 100,
                                      100 + mario.tall)
            else:
                mario.fire_mode_image.clip_composite_draw(int(mario.frame) * 35, 0, 34, 26, 0, 'h', mario.x,
                                                mario.y + mario.tall // 3, 100, 100 + mario.tall)
        else:
            if mario.direction ==1 :
                mario.image.clip_draw(int(mario.frame)*35, 0, 34, 26, mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)
            else:
                mario.image.clip_composite_draw(int(mario.frame) * 35, 0, 34, 26, 0, 'h', mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)



class Jump:
    @staticmethod
    def enter(mario, e):
        if not mario.is_jumping:
            Mario.jump_sound.play()
            mario.is_jumping = True
        #print('Mario Jump Enter')
        if up_down(e) and mario.big_Mode == False:
            mario.velocity_y = 20
            mario.is_grounded = False
        elif up_down(e) and mario.big_Mode:
            mario.velocity_y = 22
            mario.is_grounded = False

    @staticmethod
    def exit(mario, e):
        if space_down(e):
            mario.fire_ball()
        pass

    @staticmethod
    def do(mario):
        if mario.is_grounded:
            mario.is_jumping = False
            mario.state_machine.add_event(('JUMP_DOWN', 0))

    def draw(mario):
        if(mario.fire_mode):
            if mario.direction ==1 :
                mario.fire_mode_jump_image.draw(mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)
            else:
                mario.fire_mode_jump_image.composite_draw(0, 'h', mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)
        else:
            if mario.direction ==1 :
                mario.jump_image.draw(mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)
            else:
                mario.jump_image.composite_draw(0, 'h', mario.x, mario.y+mario.tall//3, 100, 100+mario.tall)

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


