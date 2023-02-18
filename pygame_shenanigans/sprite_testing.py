import pygame
from pygame import Surface
from typing import List
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, heigth, pos_x, pos_y, color):
        super().__init__()
        self.surf = pygame.Surface(size=(width, heigth))
        self.surf.fill(color)
        self.surf_ret = self.surf.get_rect()

pygame.init()
WIDTH = 1000
HEIGTH = 500
screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()

running: bool = True

anim_list: List[Surface] = [pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#0.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#1.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#2.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#3.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#4.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#5.png")

                            ]
# C:\Users\Alexd\OneDrive\Documenten\GitHub\experimental_repository\pygame_shenanigans\SFH Classes\Allied_Medic_Animation_R#3.png

soldier = anim_list[0]
soldier_rect = soldier.get_rect(midbottom=(WIDTH*0.5, HEIGTH))
soldier_head = pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Head.png")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # get to next frame
    try: soldier = anim_list[anim_list.index(soldier) - 1]
    except IndexError:
        soldier = anim_list[len(anim_list)-1]
    soldier_rect = soldier.get_rect(midbottom=(WIDTH*0.5,HEIGTH))

    #soldier head
    soldier_head_rect = soldier_head.get_rect(midleft=(soldier_rect.centerx-5, soldier_rect.top - 25))

    screen.fill((0,0,0))
    screen.blit(soldier, soldier_rect)
    screen.blit(soldier_head, soldier_head_rect)
    pygame.display.update()
    clock.tick(10)