import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    print(SCREEN_HEIGHT, SCREEN_WIDTH)


if __name__ == "__main__":
    main()
