from pico2d import *
import game_world
import game_framework
from game_world import world


class Ball:
    image = None
    fire_sound = None
    kill_sound = None

    def __init__(self, x=250, y=300, velocity=0.5, world_x = 300):
        if Ball.image is None:
            Ball.image = load_image('resource/mario/fire.png')
        self.x, self.y = x, y
        self.velocity_x = velocity  # x축 속도
        self.velocity_y = 10  # 초기 y축 속도
        self.gravity = -2.5  # 중력 효과
        self.bounce_count = 0  # 튕긴 횟수
        self.world_x = world_x
        #self.camera = camera

        if not Ball.fire_sound:
            Ball.fire_sound = load_wav('sound/fireball.wav')
            Ball.kill_sound = load_wav('sound/kill_mob.wav')
            Ball.fire_sound.set_volume(32)
            Ball.kill_sound.set_volume(32)


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb_draw())

    def update(self):
        # x축 이동
        self.x += self.velocity_x * game_framework.frame_time * 100
        #포물선
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # 바닥 충돌 처리
        if self.y <= 90:  # 바닥 위치
            self.y = 90
            self.velocity_y = -self.velocity_y
            self.bounce_count += 1

            # 3번 튕기면 제거
            if self.bounce_count >= 3:
                game_world.remove_object(self)

        # 화면 밖으로 나가면 제거
        if self.x < 0 or self.x > 1600:
            game_world.remove_object(self)

        print(self.world_x + self.x )

    def get_bb_draw(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_bb(self):

        return self.world_x + self.x -250 - 10, self.y - 10, self.world_x + self.x -250 + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'goomba:ball':
            Ball.kill_sound.play()
            game_world.remove_object(self)  # 공 삭제
            #game_world.remove_object(other)  # 적 삭제
