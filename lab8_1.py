import pygame


pygame.init()

gameOver = True
FPS = 30
width = 720
height = 720
dy=20
dx=20
screen = pygame.display.set_mode((width,height))

x = 200
y = 200
pygame.draw.circle(screen, (255,0,0), (x,y), 25, 25)

clock=pygame.time.Clock()

while gameOver:
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x,y), 25, 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and x>=20: 
        x -= 20
    
    if pressed[pygame.K_RIGHT] and x<=width-20: 
        x += 20
        
    if pressed[pygame.K_UP] and y>=20: 
        y -= 20
    
    if pressed[pygame.K_DOWN] and y<=height-20: 
        y += 20
    
    pygame.display.flip()
    clock.tick(FPS)       