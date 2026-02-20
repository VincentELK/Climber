import pygame
from constants import PLAYER_WIDTH, PLAYER_HEIGHT
from rectshape import RectShape

class Player(RectShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT )

        self.velocity = pygame.Vector2(0,0)
        def update(self, dt):
            self.position += self.velocity * dt
            self.rect.center = (self,self.position.x, self.position.y)
        def draw(self, screen):
            pygame.draw.rect(screen, "white", self.rect, 2)