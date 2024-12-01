from pico2d import load_image, draw_rectangle

import game_world


class Item:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.image = load_image('resource/mario/item.png')
        self.creating = 0
        self.hit = 0

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
        draw_rectangle(*self.get_bb_draw())
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'mario:item':
            self.hit += 1
            if self.hit > 3:
                game_world.remove_object(self)
                print('deleted')
            pass

    def update(self):
        if self.y <= 260:
            self.y += self.creating
        pass


class Fire_Item:
    def __init__(self, x, y, camera):
        self.x, self.y = x, y
        self.width, self.height = 20, 20
        self.camera = camera
        self.image = load_image('resource/mario/fire_item.png')
        self.creating = 0
        self.hit = 0

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
        draw_rectangle(*self.get_bb_draw())
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'mario:fire_item':
            self.hit += 1
            if self.hit > 3:
                game_world.remove_object(self)
                print('deleted')
            pass

    def update(self):
        if self.y <= 260:
            self.y += self.creating
        pass