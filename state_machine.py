from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_UP, SDLK_DOWN

class StateMachine:
    def __init__(self, obj):
        self.obj = obj
        self.event_que = []
    def start(self, state):
        self.cur_state = state
        self.cur_state.enter(self.obj, ('START', 0))
    def add_event(self, e):
        print(f'    DEBUG: New event {e} added to event Que')
        self.event_que.append(e)
    def set_transitions(self, transitions):
        self.set_transitions = transitions

    def update(self):
        self.cur_state.do(self.obj)
        if self.event_que:
            event = self.event_que.pop(0)
            self.handle_event(event)

    def handle_event(self, e):
        for event, next_state in self.set_transitions[self.cur_state].items():
            if event(e):
                print(f'Exit from {self.cur_state}')
                self.cur_state.exit(self.obj, e)
                self.cur_state = next_state
                print(f'Enter into {self.cur_state}')
                self.cur_state.enter(self.obj, e)
                return

        print(f'        Warning: Event [{e}] at State [{self.cur_state}] not handled')

    # def update(self):
    #     self.cur_state.do(self.obj)
    #     if self.event_que:
    #         e = self.event_que.pop(0)
    #         for check_event, next_state in self.set_transitions[self.cur_state].items():
    #             if check_event(e):
    #                 self.cur_state.exit(self.obj, e)
    #                 self.cur_state = next_state
    #                 self.cur_state.enter(self.obj, e)
    #                 #return
    #             print("     ERROR: ENTER EVENTS")       # 이 시점으로 왔다는 것은, event 에 따른 전환 못함.

    def draw(self):
        self.cur_state.draw(self.obj)



def start_event(e):
    return e[0] == 'START'
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def time_out(e):
    return e[0] == 'TIME_OUT'
def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
def jump_down(e):
    return e[0] == 'JUMP_DOWN'
