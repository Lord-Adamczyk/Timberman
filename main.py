from static import *
def on_key_down(key):
    if(key==keys.F):
        if(czyFullscreen()):
            screen.surface=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
        else:
            screen.surface=pygame.display.set_mode((FULLSCREEN_WIDTH,FULLSCREEN_HEIGHT),pygame.FULLSCREEN)
        zmienFullscreen()
def draw():
    screen.fill((0,0,0))
    tlo.draw()
pgzrun.go()