import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,192,203)
screen.fill(white)
for point in range(0,256,10): 
    pygame.draw.line(screen, (0,point,point), (0,0), (320, point*2), 1)
    pygame.draw.line(screen, (0,point,point), (0,480), (320, point*2), 1)
    pygame.draw.line(screen, (0,point,point), (640, 0), (320,point*2), 1)
    pygame.draw.line(screen, (0,point,point), (640, 480), (320,point*2), 1)
   
clock = pygame.time.Clock()

running = True

FPS= 30 
playtime = 0.0

while running:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    text = "FPS {0}".format(FPS) +" Playtime : {0:.2f}" .format(playtime)   
    pygame.display.set_caption(text)   
    pygame.display.flip()

pygame.display.update()