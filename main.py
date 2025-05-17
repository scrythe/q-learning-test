import pygame
import numpy as np
from constants import image_size, maze_structure, FPS
from maze import Maze
from player import HumanPlayer, AiPlayer


pygame.init()
screen = pygame.display.set_mode((image_size, image_size))

maze = Maze(maze_structure)
player = AiPlayer()
clock = pygame.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update()

    if player.episode % 50 == 0:
        screen.blit(maze.image)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
