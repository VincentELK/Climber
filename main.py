import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

def main():
    pygame.init()
    print(f"Starting Climber with pygame version: {pygame.version.ver}")
    print(SCREEN_HEIGHT, SCREEN_WIDTH)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Climber")
    running = True
    clock = pygame.time.Clock()
    fps = clock.get_fps()
    dt = 0
    player_color = "blue"
    
    player_rect = pygame.Rect(100,100,50,50)
    speed = 5
    
    while running:
        
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            player_rect.x += speed 
        if key[pygame.K_LEFT]:
            player_rect.x -= speed 
        if key[pygame.K_UP]:
            player_rect.y -= speed 
        if key[pygame.K_DOWN]:
            player_rect.y += speed
        if key[pygame.K_SPACE]:
            player_color = "red"


        if player_rect.x < 0:
            player_rect.x = 0
        if player_rect.x > SCREEN_WIDTH - player_rect.width:
            player_rect.x = SCREEN_WIDTH - player_rect.width
        
        if player_rect.y < 0:
            player_rect.y = 0
        if player_rect.y > SCREEN_HEIGHT - player_rect.height:
            player_rect.y = SCREEN_HEIGHT - player_rect.height

        # draw
        screen.fill((50,45,34))
        pygame.draw.rect(screen, player_color, player_rect)
        pygame.display.flip()
        
        




if __name__ == "__main__":
    main()
