from pico2d import draw_rectangle, load_image


class Pipe:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 32, 63
        self.camera = camera
        self.image = load_image('resource/block/pipe_house.png')  # 블록 이미지 경로

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x, self.y, self.x + 30, self.y + 60


    def draw(self):
        # 화면 좌표로 변환 후 그리기
        screen_x = self.x - self.camera.x
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2, 90, 120)

        left = screen_x - self.width // 2 - 10
        bottom = self.y - self.height // 2
        right = screen_x + 80 - self.width // 2
        top = self.y + 120 - self.height // 2
        draw_rectangle(left, bottom, right, top)
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


class Block:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        # self.image = load_image('resource/block/pipe_house.png')

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y + self.width

    def draw(self):
        # 화면 좌표로 변환 후 그리기
        screen_x = self.x - self.camera.x

        left = screen_x - self.width
        bottom = self.y - self.height
        right = screen_x  + self.width
        top = self.y +  + self.height
        draw_rectangle(left, bottom, right, top)
        # draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass