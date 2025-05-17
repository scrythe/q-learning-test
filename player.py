import pygame
from constants import CELL_WIDTH
import numpy as np


class Directions:
    UP = np.array((0, -1))
    RIGHT = np.array((1, 0))
    LEFT = np.array((-1, 0))
    DOWN = np.array((0, 1))
    NONE = np.array((0, 0))


class Player:
    def __init__(self, maze_structure: list[list[int]]):
        self.pos = np.array([1, 1])
        self.image = pygame.Surface((CELL_WIDTH, CELL_WIDTH))
        self.image.set_colorkey("Black")
        radius = CELL_WIDTH / 2
        center_pos = (radius, radius)
        pygame.draw.circle(self.image, "Red", center_pos, radius)
        self.maze_structure = maze_structure
        self.maze_structure_width = len(maze_structure)

    def move(self, direction: tuple[int, int]):
        new_pos = self.pos + direction

        if new_pos[0] < 0 or new_pos[1] < 0:
            return
        if (
            new_pos[0] >= self.maze_structure_width
            or new_pos[1] >= self.maze_structure_width
        ):
            return

        is_collision, cell = self.check_collision(new_pos)
        if is_collision:
            self.pos = new_pos
            return cell

    def check_collision(self, pos):
        cell = self.maze_structure[pos[1]][pos[0]]
        return (cell != 1, cell)

    def user_input(self):
        key = pygame.key.get_just_pressed()
        if key[pygame.K_w]:
            return Directions.UP
        if key[pygame.K_a]:
            return Directions.LEFT
        if key[pygame.K_s]:
            return Directions.DOWN
        if key[pygame.K_d]:
            return Directions.RIGHT
        return Directions.NONE

    def update(self):
        direction = self.user_input()
        entered_cell = self.move(direction)
        if entered_cell == 2:
            self.pos = np.array([1, 1])

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.pos * CELL_WIDTH)
