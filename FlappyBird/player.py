import pygame
class Player:
    def __init__(self,screen):
        #Velocity ler
        self.playerVelY = 3
        self.playerVelX = 5
        #Player Pos
        self.playerX = 50
        self.playerY = 150
        #Player Img yüklemek
        self.playerImg = pygame.image.load("./src/assets/Bird_01.png")
        #Player i scale etmek
        self.playerImg = pygame.transform.scale(self.playerImg,(self.playerImg.get_width()*3,self.playerImg.get_height()*3))
        #Player Rect oluşturmak
        self.playerRect = (self.playerX,self.playerY,self.playerImg.get_width(),self.playerImg.get_height())
        self.screen = screen
        #Tuşlar
        self.keys = "null"
        #Teklik Uçma
        self.oneFly = False
        #Pygame Rect
        self.cRect = self.playerImg.get_rect()
        #pygame.Rect(self.playerX,self.playerY,self.playerImg.get_width(),self.playerImg.get_height())
        pass
    def draw(self):  
        self.cRect = pygame.Rect(self.playerX,self.playerY,self.playerImg.get_width(),self.playerImg.get_height())
        self.playerRect = (self.playerX,self.playerY,self.playerImg.get_width(),self.playerImg.get_height())
        #player i çizdirmek
        self.screen.blit(self.playerImg,self.playerRect)
        #Yer Çekimi
        self.yerCekimi()
        pass
    def yerCekimi(self):
        self.playerY += self.playerVelY
            
        pass 
    def inputs(self,mykey,mytype):
        if mytype == pygame.KEYDOWN:
            if mykey == pygame.K_SPACE and self.oneFly == False:
                self.playerY -= 50
                self.oneFly = True
        if mytype == pygame.KEYUP:
            if mykey == pygame.K_SPACE:
                self.oneFly = False
            
        pass
