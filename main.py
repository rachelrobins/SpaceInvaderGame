import pygame
import random

pygame.init()

clock_tick_rate=90
collided =False
window_width=600
window_height=900

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


screen=pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Space Invadors")

icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

running= True

clock = pygame.time.Clock()
bg = pygame.image.load("space_bg.jpg").convert()
bgX = 0
bgX2 = bg.get_height()


player_img=pygame.image.load("player.png")
player = pygame.transform.scale(player_img, (70, 100))
playerX = 225
playerY = 650
player_rect = pygame.Rect(225,650,80,120)

font = pygame.font.Font('freesansbold.ttf',59)
text = font.render('Game Over!!', True, white)

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (playerX+80, playerY+220)

asteroid = [pygame.image.load("asteroid.png"),pygame.image.load("asteroid.png"),pygame.image.load("asteroid.png")
            ,pygame.image.load("asteroid.png"),pygame.image.load("asteroid.png")]
#asteroid = pygame.image.load("asteroid.png")
#asteroid = pygame.transform.scale(asteroid, (100, 130))
#asteroid_posX = random.randint(0, 600)
#asteroid_posY=0

rects=[None] * 5

rects[0]=pygame.Rect(0,0,100,130)
rects[1]=pygame.Rect(0,0,100,130)
rects[2]=pygame.Rect(0,0,100,130)
rects[3]=pygame.Rect(0,0,100,130)
rects[4]=pygame.Rect(0,0,100,130)

asteroid_posX= [-100] * 5
asteroid_posY= [-100] * 5

asteroid_init = random.randint(2, 4)
asteroid_active= []
for i in range (0,5):
    asteroid[i] = pygame.transform.scale(asteroid[i], (100, 130))
for i in range (0,asteroid_init-1):
    asteroid_posX[i] = random.randint(0, 600)
    asteroid_posY[i] = 0
init = True
Game_Over= False


def redrawWindow():
    if Game_Over==False:
        screen.blit(bg, (0, bgX))  # draws our first bg image
        screen.blit(bg, (0, bgX2))  # draws the seconf bg image

        screen.blit(player, (playerX, playerY))
        player_rect.x = playerX
        player_rect.y = playerY
        if init == True:
            for i in range(0, asteroid_init - 1):
                screen.blit(asteroid[i], (asteroid_posX[i], asteroid_posY[i]))
                rects[i].x = asteroid_posX[i]
                rects[i].y = asteroid_posY[i]
        else:
            for i in asteroid_active:
                screen.blit(asteroid[i], (asteroid_posX[i], asteroid_posY[i]))
                rects[i].x = asteroid_posX[i]
                rects[i].y = asteroid_posY[i]

        pygame.display.update()  # updates the screen


    elif Game_Over==True:

        screen.blit(bg, [0, 0])
        screen.blit(text, textRect)

    pygame.display.update()


while running:
    redrawWindow()
    bgX -= 1.4
    bgX2 -= 1.4


    if bgX < bg.get_height() * -1:
        bgX = bg.get_height()

    if bgX2 < bg.get_height() * -1:
        bgX2 = bg.get_height()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in asteroid_active:
        if init == False:
            if (player_rect.colliderect(rects[i])):
                Game_Over = True




        if (asteroid_posY[i]>=750):
            asteroid_active.remove(i)
    for j in range(0, len(asteroid) - 1):
        if j not in asteroid_active:
            coin = random.randint(1,100)
            if (coin == 2):

                asteroid_active.append(j)
                asteroid_posX[j] = random.randint(0, 600)
                asteroid_posY[j] = 0



    if ((init == True) and (asteroid_posY[0]>=750)  ):
        init = False
        for i in range (0,len(asteroid)-1):
            coin = random.randint(1, 4)
            if(coin==2):

                asteroid_active.append(i)
                asteroid_posX[i] = random.randint(0, 600)
                asteroid_posY[i] = 0

    if init == True:
        for i in range (0,asteroid_init-1):
            asteroid_posY[i] += 7
    else:
        for i in asteroid_active:
            asteroid_posY[i] += 7


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (playerX-5)>0:
        playerX -= 7

    if keys[pygame.K_RIGHT] and (playerX+5)<465:
        playerX += 7

    if keys[pygame.K_UP] and (playerY-5)>-60:
        playerY -= 7

    if keys[pygame.K_DOWN] and (playerY-5)<690:
        playerY += 7

    #screen.blit(background_image, [0, 0])

    #pygame.display.flip()
    clock.tick(clock_tick_rate)