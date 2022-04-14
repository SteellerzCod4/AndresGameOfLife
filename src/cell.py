import pygame


class Cell:
    EMPTY = False
    ALIVE = True
    EMPTY_COLOR = pygame.Color("#000001")
    ALIVE_COLOR = pygame.Color("#00BF32")

    def __init__(self, state):
        self.previous_state = state
        self.current_state = state

    @property
    def color(self):
        if self.current_state:
            return self.ALIVE_COLOR
        else:
            return self.EMPTY_COLOR
