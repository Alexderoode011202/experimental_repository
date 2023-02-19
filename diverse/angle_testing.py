import math
from typing import Tuple
import pygame
degree = math.atan2(-1, -1) * 180/math.pi
if degree < 0:
    degree = 360 + degree
print(degree)

# 360-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi

def degree_to_grid(degree: float) -> Tuple[int, int]:
    x_axis: int= 0
    y_axis: int = 0
    degree = round(degree)
    if degree <=45:
        y_axis = 45
        x_axis = degree
    elif 45 < degree <= 90:
        x_axis = 45
        y_axis = 45 - (degree - 45)
    elif 90 < degree <=135:
        x_axis = 45
        try:
            y_axis = (degree - 90)*-1
        except ZeroDivisionError:
            y_axis = 0
    elif 135< degree <=180:
        y_axis = -45
        x_axis = degree - 135






    return (x_axis, y_axis)

pygame.init()
width, heigth = 900, 450
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()



degree = 0

running = True
while running:

    engineer = pygame.image.load(
        "C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame\
_shenanigans/SFH Classes/Allied_Medic_Head.png")
    engineer = pygame.transform.scale_by(engineer, 0.5)
    engineer_rect = engineer.get_rect(midtop = (width*0.5,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # degrees nonsense
    x_axis, y_axis = pygame.mouse.get_pos()
    y_axis = engineer_rect.centery - y_axis
    x_axis = x_axis - engineer_rect.centerx
    degree = math.atan2(y_axis, x_axis) * 180/math.pi

    # rotating the image
    engineer = pygame.transform.rotate(engineer, degree)

    screen.fill((0,0,0))
    screen.blit(engineer, engineer_rect)
    pygame.display.update()
    clock.tick(60)
