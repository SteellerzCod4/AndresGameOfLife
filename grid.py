import pygame
from cell import Cell


class Grid:
    def __init__(self, width, height, screen, diag_dir=True):
        self.width = width
        self.height = height

        self.cell_width = screen.get_width() / self.width
        self.cell_height = screen.get_height() / self.height
        self.cell_border = self.cell_width * 0.1

        self.diag_dir = diag_dir
        self.screen = screen
        self.cells = [[Cell(False) for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.width):
            self.cells[i][self.height // 2] = Cell(True)
        for i in range(self.width):
            self.cells[self.height // 2][i] = Cell(True)
        for i in range(self.width):
            self.cells[i][i] = Cell(True)
        # self.draw_glider(1, 7)

    def check_indexes(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_neighbours(self, x, y):
        directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}
        if self.diag_dir:
            directions.update(((-1, -1), (1, -1), (1, 1), (-1, 1)))

        neighbors = []
        for x_dir, y_dir in directions:
            n_x, n_y = x + x_dir, y + y_dir
            if self.check_indexes(n_x, n_y):
                neighbors.append(self.cells[n_x][n_y])

        return neighbors

    def draw_cell(self, x, y):
        pygame.draw.rect(self.screen, self.cells[y][x].color,
                         pygame.Rect(y * self.cell_height + self.cell_border,
                                     x * self.cell_width + self.cell_border,
                                     self.cell_height - self.cell_border,
                                     self.cell_width - self.cell_border))

    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                self.draw_cell(i, j)

    def count_alive_neighbours(self, x, y):
        neighbours = self.get_neighbours(x, y)
        counter = 0

        for neighbour in neighbours:
            if neighbour.previous_state:
                counter += 1

        return counter

    def update(self):
        for i in range(self.width):
            for j in range(self.height):
                amount = self.count_alive_neighbours(i, j)
                if self.cells[i][j].previous_state:
                    if amount < 2 or amount > 3:
                        self.cells[i][j].current_state = False
                else:
                    if amount == 3:
                        self.cells[i][j].current_state = True

        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].previous_state = self.cells[i][j].current_state

    def draw_glider(self, x_star, y_start):
        coordinates = ((x_star, y_start), (x_star + 1, y_start + 1), (x_star + 1, y_start + 2),
                       (x_star - 1, y_start + 2), (x_star, y_start + 2))
        for x, y in coordinates:
            self.cells[x][y] = Cell(True)
