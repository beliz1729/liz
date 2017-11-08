import pygame
from pygame.locals import *
import random
from copy import deepcopy


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

        self.cgrid = self.cell_list()

        # Скорость протекания игры
        self.speed = speed

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
            self.draw_cell_list(self.cgrid)
            self.update_cell_list(self.cgrid)
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.cgrid = []
        if randomize:
            self.cell_list = [[random.randrange(0,2) for x in range(self.width // self.cell_size)] for y in range(self.height // self.cell_size)]
        return self.cell_list

    def draw_cell_list(self, rects):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
    	"""
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if rects[i][j]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (
                        x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (
                        x, y, a, b))

    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки

    	:param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
    	:return: Одномерный список ячеек, смежных к ячейке cell
    	"""
        neighbours = []
        row, col = cell
        n = self.cell_height - 1
        m = self.cell_width - 1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if not (0 <= i <= n and 0 <= j <= m) or (i == row and j == col):
                    continue
                neighbours.append(self.cgrid[i][j])
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.

    	Обновление всех ячеек происходит одновременно. Функция возвращает
    	новое игровое поле.

    	:param cell_list: Игровое поле, представленное в виде матрицы
    	:return: Обновленное игровое поле
    	"""
        new_cgrid = deepcopy(self.cgrid)
        for i in range(self.cell_height):
            for j in range(0, self.cell_width):
                count = sum(self.get_neighbours((i, j)))
                if self.cgrid[i][j]:
                    if count < 2 or count > 3:
                        new_cgrid[i][j] = 0
                else:
                    if count == 3:
                        new_cgrid[i][j] = 1
        self.cgrid = new_cgrid
        return self.cgrid

if __name__ == '__main__':
    game = GameOfLife(500, 500, 20)
    game.run()