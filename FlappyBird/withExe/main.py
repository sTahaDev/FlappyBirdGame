import pygame
import player
import background
import engel
import random

gameover = False

#pencere ayarları
window_WIDTH = 288
window_HEIGHT = 512
screen = pygame.display.set_mode((window_WIDTH,window_HEIGHT))
pygame.display.set_caption("Flappy Bird")
Black = (1,1,1)

#Playeri Oluşturmak
MyPlayer = player.Player(screen)
arkaplan = background.bg(screen)
Myengel = engel.Engel(screen,random.randint(187,450))
#Zamanı Almak
clock = pygame.time.Clock()
#Engeller
engellist = []

skor = 0
green = (255, 255, 255)
blue = (0, 0, 128)
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text = font.render(f'Skor: {skor}', True, green)
textRect = (90,20,text.get_width(),text.get_height())


while gameover==False:
    #Fps i Sabitlemek
    clock.tick(60)
    #Mouse Pozisyonu
    Mouse_X,Mouse_Y = pygame.mouse.get_pos()
    #Programı Kapatma
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key = event.key
            mytype = event.type
            MyPlayer.inputs(key,mytype)
            pass
        
    #------------------------------
    screen.fill(Black)
    #--------------------------
    #Draw Fonksiyonu
    arkaplan.draw()
    MyPlayer.draw()
    
    if Myengel.engelX < 0-52 and len(engellist) < 1:
        engellist.append(engel.Engel(screen,random.randint(187,455)))
        
        skor += 1
        text = font.render(f'Skor: {skor}', True, green)
        
    else:
        Myengel.draw()
    for i in engellist:
        i.draw()
        if i.engelX < 0-52:
            skor += 1
            text = font.render(f'Skor: {skor}', True, green)
            engellist.remove(i)
            engellist.append(engel.Engel(screen,random.randint(187,455)))
            
        #Collision Dedection
        col = i.cRect.colliderect(MyPlayer.cRect)
        col2 = i.cRect2.colliderect(MyPlayer.cRect)
        
        
        
        if col or col2:
            gameover = True
            break
    col3 = Myengel.cRect.colliderect(MyPlayer.cRect)
    col4 = Myengel.cRect2.colliderect(MyPlayer.cRect)
    if col3 or col4:
        gameover = True
        break
    
    screen.blit(text, textRect)
    
    pygame.display.update()

#Game Over Ekranı
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    bg2 = pygame.image.load("./src/assets/Background.png")
    bg2 = pygame.transform.scale(bg2,(bg2.get_width()*2,bg2.get_height()*2))
    bg2R = bg2.get_rect()
    screen.blit(bg2,bg2R)
    gameoverImg = pygame.image.load("./src/assets/GameOver.png")
    gameoverImg = pygame.transform.scale(gameoverImg,(gameoverImg.get_width()*2,gameoverImg.get_height()*2))
    gameoverRec = (50,220,gameoverImg.get_width(),gameoverImg.get_height())
    screen.blit(gameoverImg,gameoverRec)
    
    pygame.display.update()
