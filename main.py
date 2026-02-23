import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player
from ladder import Ladder
from ladder_parts import Part
def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Climber")
    running = True
    clock = pygame.time.Clock()
    fps = clock.get_fps()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    parts = pygame.sprite.Group()
    Ladder.containers = (updatable, drawable)
    Part.containers = (parts, updatable, drawable )
    Player.containers = (updatable, drawable)
    
    ladder_x = SCREEN_WIDTH / 2
    
    ladder = Ladder(ladder_x, 0)
    
    player = Player(ladder_x, ladder.parts[-1].position.y)
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
