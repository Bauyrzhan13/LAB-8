import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

ballsurface = pygame.Surface((150, 150))
ballsurface.fill((255, 255, 255))  
pygame.draw.circle(ballsurface, (255,192,203), (75, 75), 75)
#pygame.draw.circle(Surface, color, pos, radius, width=0)
running = True
FPS = 30
clock = pygame.time.Clock()

screen.blit(background, (0, 0))
screen.blit(ballsurface, (200, 200))

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    pygame.display.flip()

pygame.quit()