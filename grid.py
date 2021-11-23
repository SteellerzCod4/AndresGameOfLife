import pygame
from cell import Cell


class Grid:
    def __init__(self, width, height, screen, diag_dir=False):
        self.width = width
        self.height = height

        self.cell_width = screen.get_width() // self.width
        self.cell_height = screen.get_height() // self.height
        self.cell_border = int(self.cell_width * 0.03)

        self.diag_dir = diag_dir
        self.screen = screen
        self.cells = [[Cell(False)] * self.width for _ in range(self.height)]

    def check_indexes(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_neighbours(self, x, y):
        directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}
        if self.diag_dir:
            directions.update(((-1, -1), (1, -1), (1, 1), (-1, 1)))

        neighbors = []
        for x_dir, y_dir in directions:
            if self.check_indexes(x, y):
                neighbor = x + x_dir, y + y_dir
                neighbors.append(neighbor)

        return neighbors

    def draw_cell(self, x, y):
        pygame.draw.rect(self.screen, self.cells[x][y].color,
                         pygame.Rect(x * self.cell_width + self.cell_border,
                                     y * self.cell_height + self.cell_border,
                                     self.cell_width - 2 * self.cell_border,
                                     self.cell_height - 2 * self.cell_border))

    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                self.draw_cell(i, j)
