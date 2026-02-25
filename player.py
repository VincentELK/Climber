import pygame
from constants import *
import ladder
player_x = 100
player_y = 100

player_color = "blue"

player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT )

def player_spawn():
    pass
    

def update(dt):
    key = pygame.key.get_pressed()

    if key[pygame.K_w] and player_rect.y >= 0:
        player_rect.y -= PLAYER_SPEED * dt
    if key[pygame.K_s] and player_rect.y + PLAYER_HEIGHT < SCREEN_HEIGHT:
        player_rect.y += PLAYER_SPEED * dt

def draw(screen):
    pygame.draw.rect(screen, player_color, player_rect)