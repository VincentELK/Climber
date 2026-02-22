import pygame
from rectshape import RectShape
from constants import * 
from ladder_parts import Part


class Ladder(RectShape):
    def __init__(self, x, y):
        super().__init__(x, y, LADDER_WIDTH, LADDER_HEIGHT)
        self.rect.center = (self.position.x, self.position.y)
        self.number_parts = 12
        self.parts = []

        for i in range(self.number_parts + 1):
            self.parts.append(Part(x, y + i * LADDER_HEIGHT, LADDER_WIDTH, LADDER_HEIGHT))

    def update(self, dt):
        pass

    def draw(self, screen):
        for part in self.parts:
            part.draw(screen)
        
        
            

    


        

