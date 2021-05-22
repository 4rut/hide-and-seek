import pygame
import os

this_path = os.getcwd()

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
