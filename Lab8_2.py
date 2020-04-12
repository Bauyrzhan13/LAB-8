import pygame

pygame.init()

screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
screenrect = screen.get_rect()
background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((255,255,255))     # Fill the background white color (red,green,blue)
background2 = background.copy()   
ballsurface = pygame.Surface((50,50))     
ballsurface.set_colorkey((0,0,0)) 
pygame.draw.circle(ballsurface, (0,0,255), (25,25),25)
ballrect = ballsurface.get_rect()


ballx, bally = 550,240             
dx,dy  = 60, 50  
 
screen.blit(background, (0,0))     
screen.blit(ballsurface, (ballx, bally))

class Ball:

    def __init__(self ,ballx , bally, dx ,dy):
        self.ballx = ballx
        self.bally = bally
        self.dx = dx
        self.dy = dy
    
    def draw_it(self):
        screen.blit(ballsurface, (round(self.ballx,0), round(self.bally,0 )))
    def movement(self):
        self.ballx += self.dx * seconds 
        self.bally += self.dy * seconds
        if self.ballx < 0:
            self.ballx = 0
            self.dx *= -1 
        elif self.ballx + ballrect.width > screenrect.width:
            self.ballx = screenrect.width - ballrect.width
            self.dx *= -1
        if self.bally < 0:
            self.bally = 0
            self.dy *= -1
        elif self.bally + ballrect.height > screenrect.height:
            self.bally = screenrect.height - ballrect.height
            self.dy *= -1
def blitscreen():
    screen.blit(background,(0,0))

running = True
clock = pygame.time.Clock()       
FPS = 60                      
playtime = 0
ball = Ball(ballx , bally ,dx ,dy)
while running:
    pygame.display.set_caption("Text")
    milliseconds = clock.tick(FPS)  
    seconds = milliseconds / 1000.0 
    playtime += seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  
    blitscreen()
    ball.movement()
    ball.draw_it()
    pygame.display.flip()
    

pygame.quit()