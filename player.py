from constants import WALL, GOAL, CELL_WIDTH, maze_structure
import pygame
import numpy as np
import numpy.typing as npt


class Directions:
    UP: npt.NDArray[np.int32] = np.array((0, -1))
    RIGHT: npt.NDArray[np.int32] = np.array((1, 0))
    LEFT: npt.NDArray[np.int32] = np.array((-1, 0))
    DOWN: npt.NDArray[np.int32] = np.array((0, 1))
    NONE: npt.NDArray[np.int32] = np.array((0, 0))


class Player:
    def __init__(self) -> None:
        self.pos: npt.NDArray[np.int32] = np.array([1, 1])
        self.image = pygame.Surface((CELL_WIDTH, CELL_WIDTH))
        self.image.set_colorkey("Black")
        radius = CELL_WIDTH / 2
        center_pos = (radius, radius)
        pygame.draw.circle(self.image, "Red", center_pos, radius)
        self.maze_structure_width = len(maze_structure)

    def move(self, direction: npt.NDArray[np.int32]):
        if (direction == Directions.NONE).all():
            return
        new_pos = self.pos + direction

        # Kinda not needed cause of borders
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
        return None

    def check_collision(self, pos):
        cell = maze_structure[pos[1]][pos[0]]
        return (cell != WALL, cell)

    def update(self, direction: npt.NDArray[np.int32]):
        reward = -2
        entered_cell = self.move(direction)
        if entered_cell != None:
            reward += 1
            if entered_cell == GOAL:
                self.pos = np.array([1, 1])
                reward += 1
        return reward

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.pos * CELL_WIDTH)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def get_direction(self):
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
        direction = self.get_direction()
        super().update(direction)


class AiPlayer(Player):
    learning_rate = 0.1
    discount = 0.95
    episodes = 2000

    def __init__(self):
        super().__init__()
        # Could be more efficient when disregarding borders
        observation_space_size = self.maze_structure_width * self.maze_structure_width
        action_space_size = 4
        self.q_table = np.zeros([observation_space_size, action_space_size])
        self.current_state = self.get_state()
        self.episode = 0

    def get_state(self):
        return self.pos[1] + self.pos[0] * self.maze_structure_width

    def get_direction(self, action):
        match action:
            case 0:
                return Directions.UP
            case 1:
                return Directions.RIGHT
            case 2:
                return Directions.DOWN
            case 3:
                return Directions.LEFT
        return Directions.NONE

    def update(self):
        current_q_values = self.q_table[self.current_state]
        action = np.argmax(current_q_values)
        current_q = current_q_values[action]
        direction = self.get_direction(action)
        reward = super().update(direction)
        new_state = self.get_state()
        if reward == 0:
            new_q = 0
            self.episode += 1
            print(self.episode)
        else:
            max_future_q = np.max(self.q_table[new_state])

            new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (
                reward + self.discount * max_future_q
            )
            self.q_table[self.current_state][action] = new_q
        self.current_state = new_state
