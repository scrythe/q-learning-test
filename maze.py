import pygame
from constants import WALL, GOAL, CELL_WIDTH, image_size


class Maze:
    def __init__(self, maze_structure: list[list[int]]):
        self.maze_structure = maze_structure
        self.image = pygame.Surface((image_size, image_size))
        self.draw_maze_image()

    def draw_maze_image(self):
        wall = pygame.Surface((CELL_WIDTH, CELL_WIDTH))
        wall.fill("Black")
        path = wall.copy()
        path.fill("White")
        goal = wall.copy()
        goal.fill("Blue")

        current_cell_rect = wall.get_rect()

        for row in self.maze_structure:
            current_cell_rect.x = 0
            for cell in row:
                if cell == GOAL:
                    self.image.blit(goal, current_cell_rect)
                elif cell == WALL:
                    self.image.blit(wall, current_cell_rect)
                else:
                    self.image.blit(path, current_cell_rect)
                current_cell_rect.x += CELL_WIDTH
            current_cell_rect.y += CELL_WIDTH
