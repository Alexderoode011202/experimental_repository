import pygame
from pygame import Surface, Rect
from sys import exit
from typing import Tuple
pygame.init()
pygame.display.set_caption("Pootis Punk 2077")
# pygame.display.set_icon(pygame.image.load("experimental_repository/pygaming_shenanigans/tkinter_shennanigans/scout (1).ico"))
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
pz = pygame.image.load("pygame_shenanigans\pz_3_without_background.png")
pz_rect = pz.get_rect(midright = (800, 200))

test_figure = pygame.Surface((100, 200))
test_figure.fill((255,0,0))
test_rect = test_figure.get_rect(topleft = (0,0))

another_test_fig = pygame.Surface((100,200))
another_test_fig.fill((0,0,255))
another_test_rect = another_test_fig.get_rect(topleft = (0,test_rect.bottom))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Check for actual colission
    color: Tuple[int, int, int]
    if pz_rect.collidepoint(pygame.mouse.get_pos()):
        print("test 1")
        print(pygame.mouse.get_pos())
        x_axis = pygame.mouse.get_pos()[0] - pz_rect.left
        y_axis = pygame.mouse.get_pos()[1] - pz_rect.top


        try:
            color = pz.get_at((x_axis, y_axis))
        except IndexError:
            color = None
        
        print(color)
    
    if engineer_rect.collidepoint(pygame.mouse.get_pos()):
        print("test 1")
        print(pygame.mouse.get_pos())
        try:
            color = pz.get_at(pygame.mouse.get_pos())
        except IndexError:
            color = None

        print(color)

    if test_rect.collidepoint(pygame.mouse.get_pos()):
        print(pygame.mouse.get_pos())
        print(test_figure.get_at(pygame.mouse.get_pos()))


    if another_test_rect.collidepoint(pygame.mouse.get_pos()):
        print(pygame.mouse.get_rel())
        x_axis, y_axis = pygame.mouse.get_pos()
        x_axis = x_axis - another_test_rect.left
        y_axis = y_axis - another_test_rect.top

        

        print("TOUCH!")
        color = another_test_fig.get_at((x_axis, y_axis))
        print(color)
    
    
    third_surf = pygame.Surface((250, 250))
    third_surf.fill((255,255,255))

    




    pygame.draw.circle(engineer, (0,255,0), (engineer.get_width() * 0.5, engineer.get_height()*0.5), 50)

    screen.blit(some_test, some_test_rect)
    screen.blit(engineer, engineer_rect)
    screen.blit(test_figure, test_rect)
    screen.blit(another_test_fig, another_test_rect)
    screen.blit(pz, pz_rect)
    screen.blit(third_surf, (500, 300))
    pygame.display.update()
    clock.tick(60)