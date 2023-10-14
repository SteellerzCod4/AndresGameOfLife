import pygame
from grid import Grid
from cell import Cell
from random import choice


def game_scene(func):
    def wrapper(self, *arg, **kw):
        stop_game = False
        while not stop_game:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            self.screen.fill((0, 0, 0))
            stop_game = func(self, events, *arg, **kw)

            self.clock.tick(Game.FPS)
            pygame.display.update()
    return wrapper


class Game:
    WIDTH, HEIGHT = 800, 800
    FPS = 10
    CELLS_NUM = 50

    def __init__(self):
        self.__pygame_init()
        self.grid = Grid(self.CELLS_NUM, self.CELLS_NUM, self.screen)
        self.configurations = [self.start_config_2, self.start_config_2, self.start_config_3]
        start_config = choice(self.configurations)
        start_config()
        self.main()

    def __pygame_init(self):
        pygame.init()
        pygame.display.set_caption("Game of life by super Andres")
        # pygame.display.set_icon(pygame.image.load("img/icon.png"))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 36)

    def start_config_1(self):
        for i in range(self.grid.width):
            self.grid.cells[i][self.grid.height // 2] = Cell(True)
            self.grid.cells[self.grid.height // 2][i] = Cell(True)
            self.grid.cells[i][i] = Cell(True)

    def start_config_2(self):
        for i in range(self.grid.width):
            self.grid.cells[i][self.grid.height // 2] = Cell(True)

    def start_config_3(self):
        for i in range(self.grid.width):
            self.grid.cells[i][0] = Cell(True)
            self.grid.cells[i][4] = Cell(True)
            self.grid.cells[3][i] = Cell(True)

    def draw_glider(self, x_star, y_start):
        coordinates = ((x_star, y_start), (x_star + 1, y_start + 1), (x_star + 1, y_start + 2),
                       (x_star - 1, y_start + 2), (x_star, y_start + 2))
        for x, y in coordinates:
            self.grid.cells[x][y] = Cell(True)

    @game_scene
    def main(self, events):
        self.grid.draw()
        self.grid.update()


game = Game()
