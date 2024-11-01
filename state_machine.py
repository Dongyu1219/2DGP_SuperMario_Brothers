from sdl2 import SDL_KEYDOWN, SDLK_SPACE

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def time_out(e):
    return e[0] == 'TIME_OUT'


class StateMachine:
    def __init__(self, o):
        self.o = o
        self.event_que = []
    def start(self, state):
        self.cur_state = state
        self.cur_state.enter(self.o, ('START', 0))
    def add_event(self, e):
        self.event_que.append(e)
    def set_transitions(self, transitions):
        self.transtions = transitions
    def update(self):
        self.cur_state.do(self.o)
        if self.event_que:
            event = self.event_que.pop(0)
            self.handle_event(event)
    def draw(self):
        self.cur_state.draw(self.o)
    def handle_event(self,e ):
        for event, next_state in self.transtions[self.cur_state].items():
            if event(e):
                self.cur_state.exit(self.o, e)
                self.cur_state = next_state
                self.cur_state.enter(self.o, e)
                return

