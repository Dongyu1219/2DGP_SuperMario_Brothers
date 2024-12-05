from pico2d import draw_rectangle, load_image, get_time

import game_world


class Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.image = load_image('resource/block/block.png')

    def get_bb(self):
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y + self.width

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height
        right = screen_x + self.width
        top = self.y + self.height
        return left, bottom, right, top

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x, self.y, 40, 40)
        #draw_rectangle(*self.get_bb_draw())


    def handle_collision(self, group, other):
        pass

    def update(self):
        pass

class Iteam_Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.original_y = y  # 블록의 초기 위치 저장
        self.camera = camera
        self.hit = True
        self.is_rising = False  # 블록이 위로 올라가는 상태
        self.rise_start_time = 0  # 블록이 올라가기 시작한 시간
        self.rise_duration = 0.5  # 블록이 올라가는 시간
        self.rise_height = 10  # 블록이 올라가는 높이
        self.images = [
            load_image('resource/block/item_block_1.png'),
            load_image('resource/block/item_block_2.png'),
            load_image('resource/block/item_block_3.png')
        ]
        self.image = load_image('resource/block/block.png')

        self.time = get_time()
        self.current_frame = 0
        self.frame_time = 0.1  # 프레임 교체 주기 (초 단위)
        self.last_frame_time = get_time()  # 프레임 변경 기준 시간
        self.timer = 0


    def get_bb(self):
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y + self.width

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height
        right = screen_x + self.width
        top = self.y + self.height
        return left, bottom, right, top

    def draw(self):
        screen_x = self.x - self.camera.x
        current_image = self.images[self.current_frame]
        if self.hit:
            current_image.draw(screen_x , self.y , 40, 40)
        else:   #히트됨.

            self.image.draw(screen_x, self.y, 40, 40)

        #draw_rectangle(*self.get_bb_draw())


    def handle_collision(self, group, other):
        pass
    def update(self):
        # 프레임 변경 처리
        current_time = get_time()
        if current_time - self.last_frame_time >= self.frame_time:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.last_frame_time = current_time

        # 상승 애니메이션 처리
        if self.is_rising:
            elapsed_time = current_time - self.rise_start_time
            if elapsed_time <= self.rise_duration:
                # 상승 중
                self.y = self.original_y + self.rise_height * (elapsed_time / self.rise_duration)
            else:
                # 상승 완료 후 원래 위치로
                self.y = self.original_y
                self.is_rising = False

class Break_Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.image = load_image('resource/block/break_block.png')

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y + self.width

    def get_bb_draw(self):
        #카메라 좌표를 고려해서 충돌박스 그리기
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height
        right = screen_x + self.width
        top = self.y + self.height
        return left, bottom, right, top

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x, self.y, 40, 40)
        #draw_rectangle(*self.get_bb_draw())


    def handle_collision(self, group, other):
        game_world.remove_object(self)
        pass

    def update(self):
        pass

class Pipe:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 45, 120
        self.camera = camera
        self.image = load_image('resource/block/pipe_house.png')

    def get_bb(self):
        return self.x - self.width//2 , self.y - self.width , self.x + self.width+15, self.y + self.height

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x
        left = screen_x - self.width//2
        bottom = self.y - self.height
        right = screen_x + self.width+15
        top = self.y  + self.height
        return left, bottom, right, top

    def draw(self):
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 90, 120)
        #draw_rectangle(*self.get_bb_draw())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass


class Wall:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 32, 63
        self.camera = camera

    def get_bb(self):
        return self.x, self.y, self.x + 30, self.y + 60

    def draw(self):
        screen_x = self.x - self.camera.x

        left = screen_x - self.width // 2
        bottom = self.y - self.height // 2
        right = screen_x + self.width // 2
        top = self.y + self.height // 2
        draw_rectangle(left, bottom, right, top)
            # draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass


