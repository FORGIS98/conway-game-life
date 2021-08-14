import pygame
import time

import grid as grd
import neighbor as nb

SCR_SIZE = (720, 720)
SCR_COLOR = (50, 50, 50)
TXT_COLOR = (255, 255, 255)

# tmp values
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


def button(screen):
    small_font = pygame.font.SysFont('Corbel', 35)
    text = small_font.render('Start', True, TXT_COLOR)
    w, h = SCR_SIZE
    screen.blit(text, (w/2 - 50, h - 50))
    return (w/2 - 50, h - 50)


def main():
    screen, scr_size, scr_color = create_screen()

    grid = grd.Grid(screen, scr_size)
    neighbor = nb.Neighbor()

    pre_start = True
    play_game = True
    grid.draw_board()

    pygame.display.update()
    pygame.Surface.fill(screen, scr_color)

    while pre_start:
        pygame.Surface.fill(screen, scr_color)
        grid.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pre_start = False  # End program
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_x, pos_y = grid.get_real_pos(pos_x, pos_y)
                # Select (or deselect) a position
                grid.select(pos_x, pos_y)

        time.sleep(0.5)  # to be deleted

        mouse = pygame.mouse.get_pos()
        print(mouse)

        (w_start, h_start) = button(screen)
        print(w_start, h_start)

        if (w_start <= mouse[0] <= w_start + 140 and h_start <= mouse[0] <= h_start + 40):
            pygame.draw.rect(screen, BUTTON_LIGHT, [w_start, h_start, 140, 40])
        else:
            pygame.draw.rect(screen, (255, 0, 0), [w_start, h_start, 140, 40])

        button(screen)

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
