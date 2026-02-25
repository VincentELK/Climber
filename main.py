import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import player
import ladder
def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Climber")
    running = True
    clock = pygame.time.Clock()
    fps = clock.get_fps()
    dt = 0
    
    ladder.spawn()
    while running:
        
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        ladder.update(dt)
        
        # draw
        screen.fill((50,45,34))
        
        player.draw(screen)
        ladder.draw(screen)
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
