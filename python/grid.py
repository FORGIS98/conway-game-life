import pygame
import numpy as np

SCR_SIZE = (720, 720)
SCR_COLOR = (50, 50, 50)
TXT_COLOR = (255, 255, 255)

BUTTON_LIGHT = (150, 150, 150)
BUTTON_DARK = (100, 100, 100)


class Grid:
    def __init__(self, screen, scr_size):
        self.screen = screen
        self.max_x, self.max_y = scr_size

        # We give space for Start and Delete buttons
        self.max_x -= 50

        self.start_x, self.start_y = (10, 10)
        self.grid_color = (150, 150, 150)

        # In reality this is not the space btw squares right now
        self.space_btw_squares = 10

        # Amount of lines
        self.draw_lines = max(self.max_x, self.max_y)
        self.draw_lines = self.draw_lines // 10
        self.population_state = np.zeros((self.draw_lines, self.draw_lines))

    def draw_board(self):
        for jump in range(1, (self.draw_lines - 5)):
            # Horizontal lines
            pygame.draw.line(self.screen,
                             self.grid_color,
                             (10, 10 * jump),
                             ((self.max_y - 10), 10 * jump))

        for jump in range(1, self.draw_lines):
            # Vertical lines
            pygame.draw.line(self.screen,
                             self.grid_color,
                             (10 * jump, 10),
                             (10 * jump, (self.max_x - 10)))

    def get_real_pos(self, pos_x, pos_y):
        new_x = (pos_x - self.start_x) // self.space_btw_squares
        new_y = (pos_y - self.start_y) // self.space_btw_squares

        if new_x < 50 or new_y < 50:
            return new_x, new_y
        return None

    def select(self, pos_x, pos_y):
        inside = pos_x >= 0 and pos_y >= 0 and pos_x < len(
            self.population_state) and pos_x < len(self.population_state)
        if(inside):
            self.population_state[pos_x][pos_y] = 0.0 if self.population_state[pos_x][pos_y] else 1.0

    # returns true if user clicks inside a cell
    def inside_cells(self, _pos_x, pos_y):
        return (self.max_y - 50) >= pos_y

    def populate(self):
        self.draw_board()

        for x in range(len(self.population_state)):
            for y in range(len(self.population_state[x])):
                if(self.population_state[x][y]):
                    rect = pygame.Rect((x+1)*10, (y+1)*10, 10, 10)
                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 255),
                        rect
                    )

    def clear(self, screen, scr_color):
        screen.fill(scr_color)

    def clear_population(self):
        self.population_state = np.zeros((self.draw_lines, self.draw_lines))

    def click_start(self, pos_x, pos_y):
        return (pos_x >= 10 and pos_x <= (720/2)+10) and (pos_y >= 680 and pos_y <= 720)

    def click_clean(self, pos_x, pos_y):
        return (pos_x >= ((720/2) + 10) and pos_x <= 720) and (pos_y >= 680 and pos_y <= 720)

    def button(self, screen, txt_left, txt_right):
        small_font = pygame.font.SysFont('Corbel', 35)
        text = small_font.render(txt_left, True, TXT_COLOR)
        screen.blit(text, (10, 680))

        text = small_font.render(txt_right, True, TXT_COLOR)
        screen.blit(text, ((720/2) + 10, 680))

        return (10, 680)

    def check_button(self, mouse, screen):
        (pos_x, pos_y) = mouse
        # Check if mouse is on top of START button
        if((pos_x >= 10 and pos_x <= (720/2)+10) and (pos_y >= 680 and pos_y <= 720)):
            pygame.draw.rect(screen, BUTTON_LIGHT, [
                             10, 680, (720/2) + 10, 720])
        else:
            pygame.draw.rect(screen, BUTTON_DARK, [10, 680, (720/2) + 10, 720])
        # Check if mouse is on top of CLEAR button
        if((pos_x >= ((720/2) + 10) and pos_x <= 720) and (pos_y >= 680 and pos_y <= 720)):
            pygame.draw.rect(screen, BUTTON_LIGHT, [
                             (720/2) + 10, 680, 720, 720])
        else:
            pygame.draw.rect(screen, BUTTON_DARK, [
                             (720/2) + 10, 680, 720, 720])
