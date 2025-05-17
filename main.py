import pygame
from constants import image_size, maze_structure, FPS
from maze import Maze
from player import Player


pygame.init()
screen = pygame.display.set_mode((image_size, image_size))

maze = Maze(maze_structure)
player = Player(maze_structure)
clock = pygame.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update()

    screen.blit(maze.image)
    player.draw(screen)
    pygame.display.update()

    clock.tick(FPS)
