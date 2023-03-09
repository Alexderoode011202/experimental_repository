import pygame
from sys import exit
import math

# usual prep work
pygame.init()
WIDTH, HEIGTH = (1000, 750)
FPS: int = 60
screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()

# setting up the background image
bg = pygame.image.load("C:/Users/Alexd/Documents/GitHub/experimental_repository/pygame_shenanigans/diverse/bg.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH* 0.75, HEIGTH))
GROUND_LVL: int = 600

# setting up p1
p1 = pygame.image.load("C:/Users/Alexd/Documents/GitHub/experimental_repository/pygame_shenanigans/diverse/p1.png").convert_alpha()
p1 = pygame.transform.scale_by(p1, 0.20)
p1 = pygame.transform.flip(p1, True, False)
p1_rect = p1.get_rect(midbottom = (WIDTH*0.5,GROUND_LVL))

# calculating the amount of images needed to fill screen
tiles = math.ceil(screen.get_width()/bg.get_width()) + 1
scroll: int = 0


running: bool = True
while running:

    # event handles
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    print(f"MOUSE: {pygame.mouse.get_pos()}")
    # Background handling
    for tile in range(tiles):
        screen.blit(bg, (tile*bg.get_width() + scroll,0))
    
    scroll -= 5
    
    screen.blit(p1, p1_rect)

    # resetting of the score
    if abs(scroll) > bg.get_width():
        scroll = 0

    
    pygame.display.update()
    clock.tick(60)