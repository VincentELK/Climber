import pygame
import player
import random
from constants import *
ladder_x = 0
ladder_y = 0
ladder_rect = pygame.Rect(ladder_x, ladder_y, LADDER_WIDTH, LADDER_HEIGHT)

ladders_list = []
max_ladders = 10
def spawn():
    random.seed()
    
    
    for i in range(3, random.randint(4, max_ladders)):
        ladder_x = random.randint(0, SCREEN_WIDTH - LADDER_WIDTH)
        ladder_y = random.randint(0, SCREEN_HEIGHT - LADDER_HEIGHT)
        ladder_rect = pygame.Rect(ladder_x, ladder_y, LADDER_WIDTH, LADDER_HEIGHT)
        ladders_list.append(ladder_rect)


def update(dt):
    pass

def draw(screen):
    for i in range(len(ladders_list)):
        pygame.draw.rect(screen, "red", ladders_list[i], 2)