import pygame
from constants import *
from rectshape import RectShape

class Part(RectShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.rect.center = (self.position.x, self.position.y)
        

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, "black", self.rect, 3)