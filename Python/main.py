import pygame
import os
from random import random

from random import shuffle, randrange


this_path = os.getcwd()

pygame.init()


class Window:
    def __init__(self, win_width=800, win_height=600):
        # Размеры ркна
        self.win_width = win_width
        self.win_height = win_height

        # Название окна
        pygame.display.set_caption("Прятки")

        # Создание окна
        self.win = pygame.display.set_mode((win_width, win_height))

        # Счетчик кадров
        self.animCount = 0


class Player:
    def __init__(self, x=50, y=50, w=60, h=71, speed=5):
        # Скорость
        self.speed = speed

        # Координаты
        self.x = x
        self.y = y

        # Размеры
        self.w = w
        self.h = h

        # В какую сторону смотрит
        self.pos_left = False
        self.pos_right = False


window = Window(800, 600)


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


trump = Player()


def draw_window():
    global window
    window.win.fill((255, 153, 51))

    if window.animCount + 1 >= 30:
        window.animCount = 0

    if trump.pos_left:
        window.win.blit(walkLeft[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    elif trump.pos_right:
        window.win.blit(walkRight[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    else:
        window.win.blit(playerStand, (trump.x, trump.y))

    pygame.display.update()


run = True
while run:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and trump.x > trump.speed:
        trump.x -= trump.speed
        trump.pos_left = True
        trump.pos_right = False
    elif keys[pygame.K_RIGHT] and trump.x < window.win_width - trump.speed - trump.w:
        trump.x += trump.speed

        trump.pos_left = False
        trump.pos_right = True
    else:
        trump.pos_left = False
        trump.pos_right = False
        window.animCount = 0

    if keys[pygame.K_UP] and trump.y > trump.speed:
        trump.y -= trump.speed

    if keys[pygame.K_DOWN] and trump.y < window.win_height - trump.speed - trump.h:
        trump.y += trump.speed

    draw_window()

pygame.quit()
