import pygame

class RectShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        if hasattr(self, "containers"):
            super().__init__(self.containers) 
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.Vector2(0,0)
        
    def draw(self, screen):
        pass
        
    def update(self, dt):
        pass