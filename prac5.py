import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

for point in range(0, 500, 50): #range(start, stop, step)
    line1 = pygame.draw.line(background, (255, 0, 255), (0, 0), (500, point), 2)

for point in range(0, 500, 50):
    pygame.draw.line(background, (255, 0, 255), (0, 500), (point, 0), 2)

for point in range(0, 500, 50):
    pygame.draw.line(background, (255, 0, 255), (500, 0), (point, 500), 2)

for point in range(0, 500, 50):
    pygame.draw.line(background, (255, 0, 255), (500, 500), (0, point), 2)

running = True
FPS = 30
clock = pygame.time.Clock()

screen.blit(background, (0, 0))

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