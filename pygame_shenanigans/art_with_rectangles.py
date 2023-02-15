import pygame
from pygame import Surface, Rect
from sys import exit
pygame.init()

width, heigth = (800, 400)
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

pixel_font = pygame.font.Font("pygame_shenanigans/pixel_font2.ttf", 30)
some_test: Surface = pixel_font.render("Heya there!", True, (255,0,0))
some_test_rect: Rect = some_test.get_rect(midtop= (width*0.5, 0))

engineer: Surface = pygame.image.load("pygame_shenanigans/smallineer.PNG.png")
eng_wid = engineer.get_width()
eng_heig = engineer.get_height()
engineer_rect = engineer.get_rect(midbottom = (width*0.5, heigth))

# This is fucking stupid
pygame.draw.polygon(engineer, "red", ((eng_wid * 0.5, 0), (0, eng_heig*0.2), (eng_wid, eng_heig*0.2), (eng_wid * 0.2,eng_heig), (eng_wid * 0.8, 0.2*eng_heig)))
# So here we are going to draw with rectangles
# 1. choose on what surface to draw
# 2. choose what color the shape has to be
# 3. choose the rectangle to determine the size and placement with rectangles

pygame.draw.rect(screen, "pink", screen.get_rect(topleft=(0,0)))
pygame.draw.line(screen, "red", (0,0), (width, heigth), 3)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(some_test, some_test_rect)
    screen.blit(engineer, engineer_rect)
    pygame.display.update()
    clock.tick(60)