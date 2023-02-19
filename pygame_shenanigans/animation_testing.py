import pygame
from pygame import Surface, Rect
from typing import List, Tuple
import math
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

class Soldier:
    def __init__(self, health: int = 100, ammo: int = 100, stand_anim: List[Surface] = None, head: Surface = None, arms: Surface = None, start_coordinates: Tuple[int, int] = (0,0)):

        self.health = health
        self.ammo = ammo
        self.coordinates = start_coordinates
        self.x_speed: float = 0
        self.y_speed: float = 0
        self.running: bool = False
        self.in_air: bool = False
        self.inverse: bool = False

        self.walking_anim: List[Surface]
        self.head: Surface
        self.head_rect: Rect
        self.arms: Surface
        self.arms_rect: Rect
        self.current_frame: Surface
        self.current_rect: Rect
        self.standard_frame: Surface


        # Here we import the animation for walking
        if stand_anim is None:
            self.walking_anim = [pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#0.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#1.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#2.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#3.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#4.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#5.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#7.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#8.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#9.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#10.png")
                            ]

        else:
            self.walking_anim = stand_anim

        # Here we import the head
        if head is None:
            self.head = pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Head.png")
        else:
            self.head = head

        # Here we import the arms
        if arms is None:
            self.arms = pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Arms.png")
        else:
            self.arms = arms

        # Make first frame the standard frame
        self.standard_frame = self.walking_anim[0]
        self.current_frame = self.walking_anim[0]
        self.current_rect = self.current_frame.get_rect()

        # Add the rectangles for the arms and head
        self.head_rect = self.head.get_rect()
        self.arms_rect = self.arms.get_rect()

    def make_walk(self, opposite: bool = False, backwards: bool = False):
        """ is used to make the soldier go through the walking animation"""
        pass

    def get_frame(self) -> Surface:
        """
        Gets the frame
        """
        return self.current_frame

    def get_rect(self) -> Rect:
        return self.current_rect

    def update_frame(self, mouse_coords: tuple) -> None:
        """Here we take care of updating the information for the frame, like selecting the right frame when moving,
        and making sure the head and arms face in the right direction"""
        # 1.Update animation
        if running:
            try:
                self.current_frame = self.walking_anim[self.walking_anim.index(self.current_frame) + 1]
            except IndexError:
                self.current_frame = self.walking_anim[0]
        # 2.update head
        angle = math.atan2()
        # 3.update arms
        pass

    def invert_frame(self) -> None:
        """Inverts the frame in order to let the character turn around"""
        # use the inversion method
        self.current_frame = pygame.transform.flip(self.current_frame, True, False)
        if self.inverse:
            self.inverse = False
        else:
            self.inverse = True

    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    def set_coordinates(self, place: str, x_axis: float, y_axis: float) -> None:
        """Gives the user a new way to set the coordinates for the current rect"""
        self.current_rect = self.current_frame.get_rect(place = (x_axis, y_axis))

    def get_inversion(self) -> bool:
        return self.inverse



anim_list: List[Surface] = [pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#0.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#1.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#2.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#3.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#4.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#5.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#7.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#8.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#9.png"),
                            pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/SFH Classes/Allied_Medic_Animation_R#10.png")
                            ]

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
    soldier_head_rect = soldier_head.get_rect(midleft=(soldier_rect.centerx-13, soldier_rect.top - 25))

    screen.fill((0,0,0))
    screen.blit(soldier, soldier_rect)
    screen.blit(soldier_head, soldier_head_rect)

    pygame.display.update()
    clock.tick(10)