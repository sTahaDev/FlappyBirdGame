import pygame
import random

class Engel:
    def __init__(self,screen,newY):
        print(newY)
        self.screen = screen
        self.engelX = 288
        self.engelY = newY
        self.engelimg = pygame.image.load("./src/assets/Pipe.png")
        self.engelimg = pygame.transform.scale(self.engelimg,(self.engelimg.get_width()*2,self.engelimg.get_height()*2))
        self.engelRect = (self.engelX,self.engelY,self.engelimg.get_width(),self.engelimg.get_height())
        #engel 2
        self.engelX2 = 288
        self.engelY2 = newY - 450
        self.engelimg2 = pygame.image.load("./src/assets/Pipe.png")
        self.engelimg2 = pygame.transform.scale(self.engelimg2,(self.engelimg2.get_width()*2,self.engelimg2.get_height()*2))
        self.engelimg2 = pygame.transform.rotate(self.engelimg2,180)
        self.engelRect2 = (self.engelX2,self.engelY2,self.engelimg2.get_width(),self.engelimg2.get_height())
        #Pygame Rect
        self.cRect = self.engelimg.get_rect()
        self.cRect2 = self.engelimg2.get_rect()
        #self.cRect = pygame.Rect(self.engelX,self.engelY,self.engelimg.get_width(),self.engelimg.get_height())
        #self.cRect2 = pygame.Rect(self.engelX2,self.engelY2,self.engelimg2.get_width(),self.engelimg2.get_height())
        
        pass
    def draw(self):
        self.cRect = pygame.Rect(self.engelX,self.engelY,self.engelimg.get_width(),self.engelimg.get_height())
        self.cRect2 = pygame.Rect(self.engelX2,self.engelY2,self.engelimg2.get_width(),self.engelimg2.get_height())
        self.engelRect = (self.engelX,self.engelY,self.engelimg.get_width(),self.engelimg.get_height())
        self.engelRect2 = (self.engelX2,self.engelY2,self.engelimg2.get_width(),self.engelimg2.get_height())
        self.screen.blit(self.engelimg,self.engelRect)
        self.screen.blit(self.engelimg2,self.engelRect2)
        self.engelX -= 3
        self.engelX2 -=3
        pass