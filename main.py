import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    print(SCREEN_HEIGHT, SCREEN_WIDTH)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((50,45,34))
        pygame.display.flip()
        
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
