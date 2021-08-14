import pygame
import numpy as np

class Grid:
    def __init__(self, screen, scr_size):
        self.screen = screen
        self.max_x, self.max_y = scr_size
        self.start_x, self.start_y = (10, 10)
        self.grid_color = (150, 150, 150)
        # In reality this is not the space btw squares right now
        self.space_btw_squares = 10

        # Amount of lines
        self.draw_lines = min(self.max_x, self.max_y)
        self.draw_lines = self.draw_lines // 10
        self.population_state = np.zeros((self.draw_lines, self.draw_lines))

    def draw_board(self):

        for jump in range(1, self.draw_lines):
            # Horizontal lines
            pygame.draw.line(self.screen,
                    self.grid_color,
                    (10, 10 * jump),
                    ((self.max_y - 10), 10 * jump))

            # Vertical lines
            pygame.draw.line(self.screen,
                    self.grid_color,
                    (10 * jump, 10),
                    (10 * jump , (self.max_x - 10)))

    def get_real_pos(self, pos_x, pos_y):
        new_x = (pos_x - self.start_x) // self.space_btw_squares
        new_y = (pos_y - self.start_y) // self.space_btw_squares

        if new_x < 50 or new_y < 50:
            return new_x, new_y
        return None

    def select(self, pos_x, pos_y):
        inside = pos_x >= 0 and pos_y >= 0 and pos_x < len(self.population_state) and pos_x < len(self.population_state)
        if(inside):
            self.population_state[pos_x][pos_y] = 0.0 if self.population_state[pos_x][pos_y] else 1.0

    def populate(self):
        self.draw_board()

        for x in range(len(self.population_state)):
            for y in range(len(self.population_state[x])):
                if(self.population_state[x][y]):
                    rect = pygame.Rect((x+1)*10, (y+1)*10, 10, 10)
                    pygame.draw.rect(
                            self.screen,
                            (255,255,255),
                            rect
                            )

    def clear(self, screen, scr_color):
        screen.fill(scr_color)
