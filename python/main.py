import pygame
import time

import grid as grd
import neighbor as nb

SCR_SIZE = (720, 720)
SCR_COLOR = (50, 50, 50)
TXT_COLOR = (255, 255, 255)

BUTTON_LIGHT = (0, 255, 0)
BUTTON_DARK = (255, 0, 0)


def create_screen():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    # Size of the screen
    screen = pygame.display.set_mode(SCR_SIZE)
    # Fills the screen with almost a black background
    pygame.Surface.fill(screen, SCR_COLOR)
    return screen, SCR_SIZE, SCR_COLOR


def main():
    screen, scr_size, scr_color = create_screen()

    grid = grd.Grid(screen, scr_size)
    neighbor = nb.Neighbor()

    pre_start = True
    play_game = True

    pygame.display.update()
    pygame.Surface.fill(screen, scr_color)

    while pre_start:
        pygame.Surface.fill(screen, scr_color)
        grid.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pre_start = False  # End cell selection
                play_game = False  # End game
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                if(grid.inside_cells(pos_x, pos_y)):
                    pos_x, pos_y = grid.get_real_pos(pos_x, pos_y)
                    # Select (or deselect) a position
                    grid.select(pos_x, pos_y)

                if(grid.click_start(pos_x, pos_y)):
                    pre_start = False

                if(grid.click_clean(pos_x, pos_y)):
                    grid.clear_population()
                    grid.clear(screen, scr_color)

        mouse = pygame.mouse.get_pos()
        grid.check_button(mouse, screen)
        grid.button(screen, "START", "CLEAR")

        grid.populate()
        pygame.display.update()

    start_stop = "STOP"
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                if(grid.click_start(pos_x, pos_y)):
                    start_stop = "START" if start_stop == "STOP" else "STOP"
                if(grid.click_clean(pos_x, pos_y)):
                    play_game = False  # End game

        if start_stop == "STOP":
            grid.population_state = neighbor.play(grid.population_state)

            grid.clear(screen, scr_color)
            grid.check_button(mouse, screen)
            grid.button(screen, start_stop, "QUIT")

            grid.populate()

            pygame.display.update()
            time.sleep(0.25)

        mouse = pygame.mouse.get_pos()

        grid.check_button(mouse, screen)
        grid.button(screen, start_stop, "QUIT")

        pygame.display.update()


if __name__ == "__main__":
    main()
