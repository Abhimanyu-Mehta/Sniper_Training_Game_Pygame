import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background_img = pygame.image.load('shooting_range_background.png')
background = pygame.transform.scale(background_img, (800, 600))

pygame.display.set_caption('Sniper Training')

icon = pygame.image.load('target_icon.png')
pygame.display.set_icon(icon)

mixer.music.load('background.wav')
mixer.music.play(-1)

target = pygame.image.load('sniper_target.png')
targetx = 336
targety = 70
targetx_change = 0
targety_change = 0

gun_load = pygame.image.load('sniper.png')
gun = pygame.transform.rotate(gun_load, 45)
gunX = 336
guny = 490
gunx_change = 3
guny_change = 0

bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 490
bulletX_change = 0
bulletY_change = -6
bullet_state = "ready"


def print_target():
    screen.blit(target, (targetx, targety))


def print_gun():
    screen.blit(gun, (gunX, guny))


def print_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 25, y + 10))


def cheak_collision(targetX, targetY, bulletX, bulletY):
    distance = math.sqrt((math.pow(targetX - bulletX, 2) + (math.pow(targetY - bulletY, 2))))
    if distance <= 27:
        return True
    else:
        return False


score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
textX = 1000
textY = 1000


def print_score(x, y):
    score_print = score_font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(score_print, (x, y))


life = 3
life_font = pygame.font.Font('freesansbold.ttf', 32)
lifeX = 670
lifeY = 10


def print_life(x, y):
    life_print = life_font.render("Lives:" + str(life), True, (255, 255, 255))
    screen.blit(life_print, (x, y))


level = 1
level_font = pygame.font.Font('freesansbold.ttf', 32)
levelX = 10
levelY = 10


def print_level(x, y):
    level_print = level_font.render("Level:" + str(level), True, (255, 255, 255))
    screen.blit(level_print, (x, y))


game_over = pygame.font.Font('freesansbold.ttf', 64)
fontX = 200
fontY = 270


def print_game_over():
    game_over_ = game_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_, (fontX, fontY))


you_won = pygame.font.Font('freesansbold.ttf', 64)
you_won_fontX = 250
you_won_fontY = 270


def print_you_won():
    you_won_ = you_won.render("YOU WON", True, (255, 255, 255))
    screen.blit(you_won_, (fontX, fontY))


running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('shooting_sound.wav')
                    bullet_sound.play()
                    bulletX = gunX
                    print_bullet(bulletX, bulletY)

    if gunX >= 736:
        gunx_change = -3

    elif gunX <= 0:
        gunx_change = 3

    collision = cheak_collision(targetx, targety, bulletX, bulletY)

    if collision:
        bulletY = 490
        bullet_state = "ready"
        target_sound = mixer.Sound('target_hit.wav')
        target_sound.play()
        level += 1
        if level == 4:
            targety_change = 2
            targetx_change = 2
        if level == 3:
            targetx = random.choice([100, 150, 450, 500])
            targety_change = 10
            targetx_change = 0
        if level == 2:
            targetx = 336
            targetx_change = -4
            targety_change = 0
    elif targetx <= 0:
        targetx = 0
        targetx_change = 4
    elif targetx >= 736:
        targetx = 736
        targetx_change = -4
    elif targety >= 400:
        targety = 400
        targety_change = -10
    elif targety <= 0:
        targety = 0
        targety_change = 10
    elif life == 0:
        arrowY = 0
        print_game_over()

    elif bulletY <= 0:
        bulletY = 490
        bullet_state = "ready"
        life -= 1

    elif bullet_state is "fire":
        print_bullet(bulletX, bulletY)
        bulletY += bulletY_change
    elif level == 5:
        level = 0
    elif level == 0:
        levelX = 2000
        gunx_change = 0
        targety_change = 0
        targetx_change = 0
        print_you_won()

    print_life(lifeX, lifeY)
    print_target()
    print_score(textX, textY)
    gunX += gunx_change
    print_level(levelX, levelY)
    targetx += targetx_change
    targety += targety_change
    print_gun()
    pygame.display.update()
