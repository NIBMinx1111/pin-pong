from pygame import *

back = (200, 255, 255)
win_wid = 500
win_hei = 500
window = display.set_mode((win_wid, win_hei))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)