import pygame
from pygame.time import Clock
from pygame import Surface, Rect
from typing import Tuple
from sys import exit
pygame.init()
width: int = 800
length: int = 450

screen = pygame.display.set_mode((width, length))
clock: Clock = pygame.time.Clock()

mouse_position: Tuple[int, int]

engineer: Surface = pygame.image.load("pygame_shenanigans/Smallineer.PNG.png")
engineer_rect: Rect = engineer.get_rect(midbottom = (width * 0.5, length))

tank: Surface = pygame.image.load("pygame_shenanigans/pz_3_without_background.png")
tank_rect: Rect = tank.get_rect(bottomright = (width, length))

running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 1. Using the rect's .collidepoint() method
        if engineer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            print("Collision")
    
    # Also is a neat way to check whether the mouse has clicked
    if pygame.mouse.get_pressed() == (False, False, True):
        print("Poggers!")
        
    screen.blit(engineer, engineer_rect)
    screen.blit(tank, tank_rect)
    pygame.display.update()
    clock.tick(60)