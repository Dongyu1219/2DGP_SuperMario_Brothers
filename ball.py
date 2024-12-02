from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=0.5):
        if Ball.image is None:
            Ball.image = load_image('resource/mario/fire.png')
        self.x, self.y = x, y
        self.velocity_x = velocity  # x축 속도
        self.velocity_y = 10  # 초기 y축 속도
        self.gravity = -2.5  # 중력 효과
        self.bounce_count = 0  # 튕긴 횟수

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # x축 이동
        self.x += self.velocity_x * game_framework.frame_time * 100

        # y축 포물선 운동
        self.velocity_y += self.gravity  # 중력 작용
        self.y += self.velocity_y

        # 바닥 충돌 처리
        if self.y <= 90:  # 바닥 위치
            self.y = 90
            self.velocity_y = -self.velocity_y   # 반사 및 속도 감소
            self.bounce_count += 1

            # 3번 튕기면 제거
            if self.bounce_count >= 3:
                game_world.remove_object(self)

        # 화면 밖으로 나가면 제거
        if self.x < 0 or self.x > 1600:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'goomba:ball':
            game_world.remove_object(self)  # 공 삭제
            game_world.remove_object(other)  # 적 삭제
