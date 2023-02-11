from pygame.event import Event
from pygame import Surface
from typing import List
import pygame
import time
pygame.init()

# First we instantiate a screen
WIDTH: int = 700
LENGTH: int = 400
Screen = pygame.display.set_mode((WIDTH, LENGTH))

# how to add title
pygame.display.set_caption("some dog shit game")

# How to add icon
icon = pygame.image.load("C:/Users/Alexd/Documents/GitHub/experimental_repository/tkinter_shennanigans/scout (1).ico")
pygame.display.set_icon(icon)

# how to make a certain color background
# Directly below we create the colors in advance which follow the RGB protocol
WHITE: tuple = (255, 255, 255)
RED: tuple = (255, 0, 0)
BLUE: tuple = (0, 255, 0)
GREEN: tuple = (0, 0, 255)
BLACK: tuple = (0, 0, 0)

Screen.fill(RED)
pygame.display.update()

# standard game loop
running: bool = True

# plane image

plane_img = pygame.image.load("C:/Users/Alexd/Documents/GitHub/experimental_repository/pygame_shenanigans/airplane.png")
plane_x: int = 100
plane_y: int = 200

tank_img = pygame.image.load("C:/Users/Alexd/Documents/GitHub/experimental_repository/pygame_shenanigans/T_26.jpg")
tank_x: int = round(WIDTH * 0.75)
tank_y: int = round(LENGTH * 0.8)

# use the Screen's .blit(img, coord_tuple) method in order to get an image at a certain location on the screen!
Screen.blit(plane_img, (plane_x, plane_y))
Screen.blit(tank_img, (tank_x, tank_y))
pygame.display.update()


def move_object(image: Surface, x_dif: int = 0, y_dif: int = 0):
    """
    Does not work due to Surface's .get_heigth() and .get_width() methods show the wrong information
    """
    global Screen
    current_y: int = image.get_height()
    current_x: int = image.get_width()
    print(f"({current_x}, {current_y}")
    Screen.blit(image, (current_x + x_dif, current_y + y_dif))
    pygame.display.update()
    return None


while running:
    # pygame.display.update()
    events: List[Event] = pygame.event.get()
    print(events)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        print(pygame.key.get_pressed())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("lower!")
                tank_x += 5

            elif event.key == pygame.K_a:
                tank_x -= 5

            elif event.key == pygame.K_w:
                tank_y -= 5

            elif event.key == pygame.K_s:
                tank_y += 5

    # Empty screen
    Screen.fill((255,0,0))
    pygame.display.update()

    # update with new values
    Screen.blit(tank_img, (tank_x, tank_y))
    pygame.display.update()
    pass
