import pygame
import os

this_path = os.getcwd()

pygame.init()

win_width = 800
win_height = 600

clock = pygame.time.Clock()

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Прятки")

walkRight = [pygame.image.load(this_path + r'\animations\player\pygame_right_1.png'),
             pygame.image.load(this_path + r'\animations\player\pygame_right_3.png'),
             pygame.image.load(this_path + r'\animations\player\pygame_right_4.png'),
             pygame.image.load(this_path + r'\animations\player\pygame_right_2.png'),
             pygame.image.load(this_path + r'\animations\player\pygame_right_5.png'),
             pygame.image.load(this_path + r'\animations\player\pygame_right_6.png')]

walkLeft = [pygame.image.load(this_path + r'\animations\player\pygame_left_1.png'),
            pygame.image.load(this_path + r'\animations\player\pygame_left_2.png'),
            pygame.image.load(this_path + r'\animations\player\pygame_left_3.png'),
            pygame.image.load(this_path + r'\animations\player\pygame_left_4.png'),
            pygame.image.load(this_path + r'\animations\player\pygame_left_5.png'),
            pygame.image.load(this_path + r'\animations\player\pygame_left_6.png')]

playerStand = pygame.image.load(this_path + r'\animations\player\pygame_idle.png')


speed = 5
pos_x = 50
pos_y = 50
width = 60
height = 71

left = False
right = False
animCount = 0


def draw():
    global animCount
    win.fill((255, 153, 51))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (pos_x, pos_y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (pos_x, pos_y))
        animCount += 1
    else:
        win.blit(playerStand, (pos_x, pos_y))

    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pos_x > speed:
        pos_x -= speed

        left = True
        right = False

    elif keys[pygame.K_RIGHT] and pos_x < win_width - speed - width:
        pos_x += speed

        left = False
        right = True

    else:
        left = False
        right = 0
        animCount = 0

    if keys[pygame.K_UP] and pos_y > speed:
        pos_y -= speed

    if keys[pygame.K_DOWN] and pos_y < win_height - speed - height:
        pos_y += speed

    draw()

pygame.quit()
