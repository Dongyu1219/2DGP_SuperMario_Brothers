import pico2d
import logo_mode
import play_mode

pico2d.open_canvas()

#play_mode.init()
logo_mode.init()
while logo_mode.running:
    logo_mode.handle_events()
    logo_mode.update()
    logo_mode.draw()
    pico2d.delay(0.01)

logo_mode.finish()

pico2d.close_canvas()