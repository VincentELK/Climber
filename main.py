import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player
def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Climber")
    running = True
    clock = pygame.time.Clock()
    fps = clock.get_fps()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    while running:
        
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # draw
        screen.fill((50,45,34))
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        

        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
