import numpy as np


class Neighbor:
    def __init__(self):
        pass

    def play(self, population_state):
        len_pop = len(population_state)
        new_population_state = np.zeros((len_pop, len_pop))

        for x in range(len_pop - 1):
            for y in range(len_pop - 1):
                if(self.__inside(population_state, x, y)):
                    total_neighbor = self.__total_neighbor(
                        x, y, population_state)
                    # For a space that is populated
                    if(population_state[x][y]):
                        # Each cell with one or no neighbors dies, as if by solitude
                        # Each cell with four or more neighbors dies, as if by overpopulation
                        if(total_neighbor <= 1 or total_neighbor >= 4):
                            new_population_state[x][y] = 0.0
                        else:  # Each cell with two or three neighbors survives
                            new_population_state[x][y] = 1.0

                    elif(total_neighbor == 3):  # For a space that is empty or unpopulated
                        # Each cell with three neighbors becomes populated
                        new_population_state[x][y] = 1.0

        return new_population_state

    def __inside(self, population_state, x, y):
        if(x <= 0 or y <= 0):
            return False
        elif(x >= len(population_state) or y >= len(population_state)):
            return False
        return True

    def __total_neighbor(self, x, y, population_state):
        if(y > 0 and x > 0):
            return sum([
                population_state[x-1][y-1],
                population_state[x-1][y],
                population_state[x-1][y+1],
                population_state[x][y-1],
                population_state[x][y+1],
                population_state[x+1][y-1],
                population_state[x+1][y],
                population_state[x+1][y+1]
            ])
        else:
            return 0

        # return sum(population_state[i][j] for i in range(max(0, x-1), min(len(population_state), x+2)) for j in range(max(0, y-1), min(len(population_state[0]), y+2)))
