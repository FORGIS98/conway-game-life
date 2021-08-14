import pygame
import time

import grid as grd
import neighbor as nb

def create_screen():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    # Size of the screen
    scr_size = (500, 500)
    screen = pygame.display.set_mode(scr_size)
    # Fills the screen with almost a black background
    scr_color = (50, 50, 50)
    pygame.Surface.fill(screen, scr_color)
    return screen, scr_size, scr_color

def main():
    screen, scr_size, scr_color = create_screen()

    grid = grd.Grid(screen, scr_size)
    neighbor = nb.Neighbor()

    pre_start = True
    play_game = True
    grid.draw_board()

    pygame.display.update()
    pygame.Surface.fill(screen, scr_color)

    tmp_squares = 35 # to be deleted

    while pre_start and tmp_squares >= 0:
        pygame.Surface.fill(screen, scr_color)
        grid.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pre_start = False # End program
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_x, pos_y = grid.get_real_pos(pos_x, pos_y)
                # Select (or deselect) a position
                grid.select(pos_x, pos_y)

        time.sleep(0.5) # to be deleted
        tmp_squares -= 1

        grid.populate()
        pygame.display.update()

    while play_game:
        grid.population_state = neighbor.play(grid.population_state)
        grid.clear(screen, scr_color)
        grid.populate()
        pygame.display.update()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
