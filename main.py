import pygame
import random
import sys

pygame.init()

clock_tick_rate = 70
collided = False
window_width = 600
window_height = 900

alien_sizeX = 90
alien_sizeY = 110

fire_sizeX = 20
fire_sizeY = 20

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Space Invadors")

icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

running = True

clock = pygame.time.Clock()
bg = pygame.image.load("space_bg.jpg").convert()
bgX = 0
bgX2 = bg.get_height()

player_img = pygame.image.load("player.png")
player = pygame.transform.scale(player_img, (70, 100))
playerX = 225
playerY = 650
player_rect = pygame.Rect(225, 650, 80, 120)

font = pygame.font.Font('freesansbold.ttf', 59)
text = font.render('Game Over!!', True, white)

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (playerX + 80, playerY + 220)

asteroid = [pygame.image.load("asteroid.png"), pygame.image.load("asteroid.png"), pygame.image.load("asteroid.png")
    , pygame.image.load("asteroid.png"), pygame.image.load("asteroid.png")]

rects = [None] * 5

rects[0] = pygame.Rect(0, 0, 100, 130)
rects[1] = pygame.Rect(0, 0, 100, 130)
rects[2] = pygame.Rect(0, 0, 100, 130)
rects[3] = pygame.Rect(0, 0, 100, 130)
rects[4] = pygame.Rect(0, 0, 100, 130)

asteroid_posX = [-100] * 5
asteroid_posY = [-100] * 5

asteroid_init = random.randint(2, 4)
asteroid_active = []
for i in range(0, 5):
    asteroid[i] = pygame.transform.scale(asteroid[i], (100, 130))
for i in range(0, asteroid_init - 1):
    asteroid_posX[i] = random.randint(0, 600)
    asteroid_posY[i] = 0

alien = [pygame.image.load("alien.png"), pygame.image.load("alien.png"), pygame.image.load("alien.png")
    , pygame.image.load("alien.png"), pygame.image.load("alien.png")]
shot_alien = [False] * 5
active_alien = 0
for i in range(0, 5):
    alien[i] = pygame.transform.scale(alien[i], (alien_sizeX, alien_sizeY))

alien_rect = [None] * 5

alien_rect[0] = pygame.Rect(0, 0, alien_sizeX, alien_sizeY)
alien_rect[1] = pygame.Rect(0, 0, alien_sizeX, alien_sizeY)
alien_rect[2] = pygame.Rect(0, 0, alien_sizeX, alien_sizeY)
alien_rect[3] = pygame.Rect(0, 0, alien_sizeX, alien_sizeY)
alien_rect[4] = pygame.Rect(0, 0, alien_sizeX, alien_sizeY)

fire_ball = [pygame.image.load("fire.png"), pygame.image.load("fire.png"), pygame.image.load("fire.png")
    , pygame.image.load("fire.png"), pygame.image.load("fire.png"), pygame.image.load("fire.png"),
             pygame.image.load("fire.png"), pygame.image.load("fire.png")
    , pygame.image.load("fire.png"), pygame.image.load("fire.png")]

for i in range(0, 10):
    fire_ball[i] = pygame.transform.scale(fire_ball[i], (fire_sizeX, fire_sizeY))

fire_rect = [None] * 10
for i in range(0, 10):
    fire_rect[i] = pygame.Rect(0, 0, fire_sizeX, fire_sizeY)

fire_sound = pygame.mixer.Sound("fire_audio.wav")
init = True
alien_fall = False
Game_Over = False
counter = 0
shoot = False
last_ball_shot = 0;
balls_in_the_air = 0
exploded = [False] * 10


def shoot_on():
    pygame.mixer.Sound.play(fire_sound)
    pygame.mixer.music.stop()


def redrawWindow():
    if Game_Over == False:
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
        if (alien_fall == True):
            screen.blit(alien[active_alien], (alien_rect[active_alien].x, alien_rect[active_alien].y))

        if (shoot == True):
            screen.blit(fire_ball[0], (fire_rect[0].x, fire_rect[0].y))
        pygame.display.update()  # updates the screen


    elif Game_Over == True:

        screen.blit(bg, [0, 0])
        screen.blit(text, textRect)

    pygame.display.update()
    
def control():
    global  playerX
    global  playerY
    global balls_in_the_air
    global last_ball_shot
    
    if keys[pygame.K_LEFT] and (playerX - 5) > 0:
        playerX = playerX - 11

    if keys[pygame.K_RIGHT] and (playerX + 5) < 465:
        playerX += 11

    if keys[pygame.K_UP] and (playerY - 5) > -60:
        playerY -= 11

    if keys[pygame.K_DOWN] and (playerY - 5) < 780:
        playerY += 11

    if keys[pygame.K_SPACE]:
        shoot = True
        shoot_on()
        balls_in_the_air = balls_in_the_air + 1
        fire_rect[last_ball_shot].x = player_rect.x + 25
        fire_rect[last_ball_shot].y = player_rect.y - 20
        last_ball_shot = (last_ball_shot + 1) % 10

    if keys[pygame.K_a]:
        Game_Over = False
        screen.blit(bg, [0, 0])
        playerX = 225
        playerY = 650
        screen.blit(player, (225, 650))
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

        if (asteroid_posY[i] >= 750):
            asteroid_active.remove(i)
    for j in range(0, len(asteroid) - 1):
        if j not in asteroid_active:
            coin = random.randint(1, 100)
            if (coin == 2):
                asteroid_active.append(j)
                asteroid_posX[j] = random.randint(0, 600)
                asteroid_posY[j] = 0

    if ((init == True) and (asteroid_posY[0] >= 750)):
        init = False
        for i in range(0, len(asteroid) - 1):
            coin = random.randint(1, 4)
            if (coin == 2):
                asteroid_active.append(i)
                asteroid_posX[i] = random.randint(0, 600)
                asteroid_posY[i] = 0

    if init == True:
        for i in range(0, asteroid_init - 1):
            asteroid_posY[i] += 5
    else:
        for i in asteroid_active:
            asteroid_posY[i] += 5

    if (alien_fall == True):
        alien_rect[active_alien].y += 5
    if (alien_rect[active_alien].y > 750):
        alien_fall = False
        active_alien = (active_alien + 1) % 5

    if (len(asteroid_active) > 2 and alien_fall == False):
        alien_fall = True
        alien_rect[active_alien].x = random.randint(100, 400)
        alien_rect[active_alien].y = 0

    if (shoot == True):
        fire_rect[0].y -= 10
        if (fire_rect[0].colliderect(alien_rect[active_alien])):
            alien_rect[active_alien].y = 1000
            shot_alien[active_alien] = True

    keys = pygame.key.get_pressed()
    control()

    # screen.blit(background_image, [0, 0])

    # pygame.display.flip()
    counter += 1
    clock.tick(clock_tick_rate)
