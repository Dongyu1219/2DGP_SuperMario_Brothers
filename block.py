from pico2d import draw_rectangle, load_image, get_time


class Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.image = load_image('resource/block/block.png')  # 블록 이미지 경로

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
        draw_rectangle(*self.get_bb_draw())
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass

class Iteam_Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.images = [
            load_image('resource/block/item_block_1.png'),
            load_image('resource/block/item_block_2.png'),
            load_image('resource/block/item_block_3.png')
        ]
        self.time = get_time()

        self.current_frame = 0
        self.frame_time = 70.0
        self.timer = 0

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
        current_image = self.images[self.current_frame]
        current_image.draw(screen_x , self.y , 40, 40)
        #self.image.draw(screen_x , self.y , 40, 40)
        draw_rectangle(*self.get_bb_draw())
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        self.timer += get_time()
        if self.timer >= self.frame_time:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.images)
        pass


class Pipe:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 45, 120
        self.camera = camera
        self.image = load_image('resource/block/pipe_house.png')  # 블록 이미지 경로

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x - self.width//2 , self.y - self.width , self.x + self.width+15, self.y + self.height

    def get_bb_draw(self):
        screen_x = self.x - self.camera.x
        left = screen_x - self.width//2
        bottom = self.y - self.height
        right = screen_x + self.width+15
        top = self.y  + self.height
        return left, bottom, right, top

    def draw(self):
        # 화면 좌표로 변환 후 그리기
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 90, 120)
        draw_rectangle(*self.get_bb_draw())
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass


class Wall:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 32, 63
        self.camera = camera
        #self.image = load_image('resource/block/pipe_house.png')

    def get_bb(self):
            # 세계 좌표 기준의 충돌 박스
        return self.x, self.y, self.x + 30, self.y + 60

    def draw(self):
            # 화면 좌표로 변환 후 그리기
        screen_x = self.x - self.camera.x

        left = screen_x - self.width // 2 - 10
        bottom = self.y - self.height // 2
        right = screen_x + 80 - self.width // 2
        top = self.y + 120 - self.height // 2
        draw_rectangle(left, bottom, right, top)
            # draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

        def update(self):
            pass


