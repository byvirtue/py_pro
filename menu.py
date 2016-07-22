import random, pygame, sys
from pygame.locals import *
import shelve
class menu:
    option_width=700
    option_height=100
    def _init_(self):
        pass
    def get_option_number(self,mousex,mousey,tag):
        for i in range(0,4):
            self.img_width=tag[i].get_width()
            self.img_height=tag[i].get_height()
            if(mousex>=menu.option_width and mousex<=(menu.option_width+self.img_width) and mousey>=(menu.option_height*(i+1)) and mousey<=((menu.option_height*(i+1)+ self.img_height))):
               return (i+1)   
            

    def set_bg(self,DISPLAY):
        self.option_selected=0
        
        while(True):
            DISPLAY.fill((255,255,255))
            self.tag=[]
            self.bkground=pygame.image.load('menu_bg.gif')
            self.tag.append(pygame.image.load('menu_tag1.png'))
            self.tag.append(pygame.image.load('menu_tag2.png'))
            self.tag.append(pygame.image.load('menu_tag3.png'))
            self.tag.append(pygame.image.load('menu_tag4.png'))
            for i in range(0,4):
                DISPLAY.blit(self.tag[i],(menu.option_width,menu.option_height*(i+1)))
            DISPLAY.blit(self.bkground,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif (event.type == KEYDOWN and event.key == K_F4):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    self.mousex, self.mousey = event.pos
                    self.option_selected=self.get_option_number(self.mousex,self.mousey,self.tag)
                    return self.option_selected
        
    
