import pygame
from grid import Grid


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
    FPS = 1
    CELLS_NUM = 90

    def __init__(self):
        self.__pygame_init()
        self.grid = Grid(self.CELLS_NUM, self.CELLS_NUM, self.screen)
        self.main()

    def __pygame_init(self):
        pygame.init()
        pygame.display.set_caption("Game of life")
        # pygame.display.set_icon(pygame.image.load("img/icon.png"))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 36)

    @game_scene
    def main(self, events):
        self.grid.draw()
        self.grid.update()


game = Game()