import pygame
import os
import random

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

# анимации ходьбы
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

# создание игрока
trump = Player(speed=5)

# создание лабиринта
grid = [[1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]]


# прорисовка окна
def draw_window():
    global window

    # заливка фона
    window.win.fill((255, 153, 51))

    # прорисока лабиринта по сетке grid
    for i in range(20):
        for j in range(15):
            if not grid[j][i]:
                pygame.draw.rect(window.win, (255, 255, 255), (i * 40, j * 40, 40, 40))

    # проверка синхронизации анимаций с кадрами
    if window.animCount + 1 >= 30:
        window.animCount = 0

    # поворот модельки игрока
    if trump.pos_left:
        window.win.blit(walkLeft[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    elif trump.pos_right:
        window.win.blit(walkRight[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    else:
        window.win.blit(playerStand, (trump.x, trump.y))

    print(window.win.get_at((trump.x, trump.y)))

    # смена кадра
    pygame.display.update()


# работа окна
run = True
while run:
    # настройка тикрейта
    pygame.time.Clock().tick(30)

    # проверка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # проверка передвижения игрока
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

    #print('1. x: ', trump.x, '\ty:', trump.y)

    if keys[pygame.K_DOWN] and trump.y < window.win_height - trump.speed - trump.h:
        if window.win.get_at((trump.x + (trump.w // 2), trump.y - trump.speed + trump.h)) != pygame.Color(255, 153, 51):
            trump.y += trump.speed

    #print('2. x: ', trump.x, '\ty:', trump.y)

    draw_window()

pygame.quit()
