import pygame

# Generated with maze_generator from it_learns_maze
maze_structure = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

CELL_WIDTH = 40

image_size = len(maze_structure) * CELL_WIDTH

pygame.init()
screen = pygame.display.set_mode((image_size, image_size))


class Maze:
    def __init__(self, maze_structure: list[list[int]]):
        self.maze_structure = maze_structure
        self.image = pygame.Surface((image_size, image_size))
        self.create_maze()

    def create_maze(self):
        wall = pygame.Surface((CELL_WIDTH, CELL_WIDTH))
        wall.fill("Black")
        path = wall.copy()
        path.fill("White")
        goal = wall.copy()
        goal.fill("Blue")

        collision_rects = []
        current_cell_rect = wall.get_rect()

        for row in self.maze_structure:
            current_cell_rect.x = 0
            for cell in row:
                if cell == 2:
                    self.image.blit(goal, current_cell_rect)
                    collision_rects.append(current_cell_rect.copy())
                elif cell == 1:
                    self.image.blit(wall, current_cell_rect)
                    collision_rects.append(current_cell_rect.copy())
                else:
                    self.image.blit(path, current_cell_rect)
                current_cell_rect.x += CELL_WIDTH
            current_cell_rect.y += CELL_WIDTH


maze = Maze(maze_structure)

screen.blit(maze.image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
