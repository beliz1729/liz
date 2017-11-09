import pygame
from pygame.locals import *
import random
from copy import deepcopy


class Cell:

    def __init__(self, row, col, state=0):
        self.row = row
        self.col = col
        self.life = state

    def is_alive(self):
        return self.life


class CellList:

    def __init__(self, nrows, ncols, randomize=True):
        self.nrows = nrows
        self.ncols = ncols
        self.random = randomize
        if randomize:
            self.cell_list = [[Cell(i, j, random.randrange(0,2)) for j in range(self.ncols)] for i in range(self.nrows)]
        else:
            self.cell_list = [[Cell(i, j) for j in range(self.ncols)] for i in range(self.nrows)]

    def get_neighbours(self, cell):
        neighbours = []
        positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0),
                     (1, -1), (1, 1)]
        for r, c in positions:
            if 0 <= cell[0] + r < self.nrows and 0 <= cell[1] + c < self.ncols:
                try:
                    neighbours.append(self.cell_list[cell[0] + r][cell[1] + c].is_alive())
                except:
                    continue
        return neighbours

    def update(self):
        new_grid = deepcopy(self.cell_list)
        for i in range(len(self.cell_list)):
            for j in range(len(self.cell_list[i])):
                num_neighbours = sum(c for c in self.get_neighbours((i, j)))
                if self.cell_list[i][j]:
                    if not (2 <= num_neighbours <= 3):
                        new_grid[i][j] = int(False)
                else:
                    if num_neighbours == 3:
                        new_grid[i][j] = int(True)
        self.cell_list = new_grid
        return new_grid

    @classmethod
    def from_file(cls, filename):
        cgrid = []
        with open(filename) as f:
            cgrid = [[Cell(i, j, int(value)) for j, value in enumerate(line) if value in '01'] for i, line in enumerate(f)]
        clist_class = cls(len(cgrid), len(cgrid[0]), False)
        clist_class.clist = cgrid
        return clist_class

    def __iter__(self):
        self.i_num = 0
        self.j_num = 0
        return self

    def __next__(self):
        if self.i_num == self.nrows:
            raise StopIteration

        cell = self.cell_list[self.i_num][self.j_num]
        self.j_num += 1
        if self.j_num == self.ncols:
            self.j_num = 0
            self.i_num += 1
        return cell


class GameOfLife:
    def __init__(self, width=500, height=500, cell_size=5, speed=20):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        self.clist = CellList(self.cell_height, self.cell_width, True) 
        self.grid = self.clist.cell_list

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list()
            self.clist.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_cell_list(self):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if self.grid[i][j].is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'), (
                        x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (
                        x, y, a, b))


if __name__ == '__main__':
    game = GameOfLife(500, 500, 20)
    game.run()