import pygame

class bg:
    def __init__(self,screen):
        self.screen = screen
        self.bgimg = pygame.image.load("./src/assets/Background.png")
        self.bgimg = pygame.transform.scale(self.bgimg,(self.bgimg.get_width()*2,self.bgimg.get_height()*2))
        self.bgRect = (0,0,self.bgimg.get_width(),self.bgimg.get_height())
        pass
    def draw(self):
        self.screen.blit(self.bgimg,self.bgRect)
        pass