import pygame

from player import Player
from window import Window
from grid import grid


def movement_logic(curr_window: Window, curr_player: Player, keys):
    if keys[pygame.K_LEFT] and curr_player.x > curr_player.speed:
        grid_check_x = curr_player.x // 40
        grid_check_y_1 = curr_player.y // 40
        grid_check_y_2 = (curr_player.y + curr_player.h - 10) // 40
        grid_check_y_3 = (curr_player.y + curr_player.h // 2) // 40

        if grid[grid_check_y_1][grid_check_x] and grid[grid_check_y_2][grid_check_x] and grid[grid_check_y_3][
            grid_check_x]:
            curr_player.x -= curr_player.speed
            curr_player.pos_left = True
            curr_player.pos_right = False
            curr_player.refresh_center_pos()

    elif keys[pygame.K_RIGHT] and curr_player.x < curr_window.win_width - curr_player.speed - curr_player.w:
        grid_check_x = (curr_player.x + curr_player.w) // 40
        grid_check_y_1 = curr_player.y // 40
        grid_check_y_2 = (curr_player.y + curr_player.h) // 40
        grid_check_y_3 = (curr_player.y + curr_player.h // 2) // 40

        if grid[grid_check_y_1][grid_check_x] and grid[grid_check_y_2][grid_check_x] and grid[grid_check_y_3][
            grid_check_x]:
            curr_player.x += curr_player.speed
            curr_player.pos_left = False
            curr_player.pos_right = True
            curr_player.refresh_center_pos()

    else:
        curr_player.pos_left = False
        curr_player.pos_right = False
        curr_window.animCount = 0

    if keys[pygame.K_UP] and curr_player.y > curr_player.speed:
        grid_check_x = (curr_player.x + curr_player.w // 2) // 40
        grid_check_y = curr_player.y // 40

        if grid[grid_check_y][grid_check_x]:
            curr_player.y -= curr_player.speed
            curr_player.refresh_center_pos()

    if keys[pygame.K_DOWN] and curr_player.y < curr_window.win_height - curr_player.speed - curr_player.h:
        grid_check_x = (curr_player.x + curr_player.w // 2) // 40

        grid_check_y = (curr_player.y + curr_player.h) // 40

        if grid[grid_check_y][grid_check_x]:
            curr_player.y += curr_player.speed
            curr_player.refresh_center_pos()
