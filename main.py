import random, pygame, sys
from pygame.locals import *
import shelve
import menu
WINDOWL=800
WINDOWW=1400
FPS=50
FPSCLOCK=pygame.time.Clock()
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 2, 255)

def make_home_screen(DISPLAY):
    bkground=pygame.image.load('home_page1.png')
    bkground=pygame.transform.scale(bkground,(WINDOWW,WINDOWL))
    DISPLAY.blit(bkground,(0,0))
    pygame.display.update()
    pygame.time.wait(2000)
    

def main():
    pygame.init()
    DISPLAY=pygame.display.set_mode((0,0),FULLSCREEN)
    make_home_screen(DISPLAY)
    menu1=menu.menu()
    menu1.set_bg(DISPLAY)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN and event.key == K_F4):
                pygame.quit()
                sys.exit()
        DISPLAY.fill(RED)
        pygame.display.update()
if __name__ == '__main__':
    main()
