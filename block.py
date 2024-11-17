from pico2d import draw_rectangle


class Block:
    def __init__(self, x, y, width, height, camera):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.camera = camera

    def get_bb(self):
        # 세계 좌표 기준의 충돌 박스
        return self.x, self.y, self.x + self.width, self.y + self.height

    def draw(self):
        # 화면 좌표로 변환 후 그리기
        screen_x = self.x - self.camera.x
        draw_rectangle(screen_x, self.y, screen_x + self.width, self.y + self.height)
        self.image.draw(screen_x + self.width // 2, self.y + self.height // 2)
