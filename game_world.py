world = [ [], [] ]
#world[0] : 백그라운드 개체들 (맨 아래에 그려야 할 객체들)
#world[1] : 포어그라운드 객체들 ( 위에 그려야할 객체들)

def add_object(o, depth):
    world[depth].append(o)


def render():
    for layer in world:
        for o in layer:
            o.draw()


def update():
    for layer in world:
        for o in layer:
            o.update()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return          #지우는 미션은 달성. 안하면 layer 만큼 반복함
    print('ERROR : DO NOT EXIST')