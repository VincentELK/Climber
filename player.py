import pygame
from constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED
from rectshape import RectShape

class Player(RectShape):
    containers: tuple[pygame.sprite.Group, ...] = ()# create type of tuple for the container
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT )

        self.velocity = pygame.Vector2(0,0)
        self.speed = PLAYER_SPEED
        
    def move(self, dt, direction):
        self.position += direction * self.speed * dt 

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(dt, pygame.Vector2(-1,0))
        if keys[pygame.K_d]:
            self.move(dt, pygame.Vector2(1,0))
        if keys[pygame.K_w]:
            self.move(dt, pygame.Vector2(0,-1))
        if keys[pygame.K_s]:
            self.move(dt, pygame.Vector2(0,1))

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, 2)

    