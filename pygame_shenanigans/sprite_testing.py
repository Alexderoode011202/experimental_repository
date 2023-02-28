import pygame
from pygame import Surface
from pygame.sprite import Sprite
from sys import exit
from typing import Tuple, Union

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width: int, heigth: int, pos_x: int, pos_y: int, color: Tuple[int, int, int]):
        super().__init__()
        self.image: Surface = pygame.Surface((width, heigth))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def point_topleft(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer topleft"""
        self.rect = self.image.get_rect(topleft = coords)

    def point_midtop(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at midtop"""
        self.rect = self.image.get_rect(midtop = coords)

    def point_topright(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at topright"""
        self.rect = self.image.get_rect(topright = coords)

    def point_midleft(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at midleft"""
        self.rect = self.image.get_rect(midleft = coords)

    def point_center(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at center"""
        self.rect = self.image.get_rect(center = coords)

    def point_midright(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at midright"""
        self.rect = self.image.get_rect(midright = coords)

    def point_bottomleft(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at bottomleft"""
        self.rect = self.image.get_rect(bottomleft = coords)

    def point_midbottom(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at midbottom"""
        self.rect = self.image.get_rect(midmottom = coords)

    def point_bottomright(self, coords: Tuple[Union[float, int]]):
        """Sets the rect's pointer at bottomright"""
        self.rect = self.image.get_rect(bottomright = coords)

    def get_edge_coord(self, side: str) -> Union[float, int]:
        """Returns the coordinate of a specific edge of the Rect.
        :param side: takes either "top", "bottom", "left", "right" as input and 
        will raise a ValueError if the input is not one of those four.
        :returns: x- or y-coordinate of the edge"""

        if side == "top":
            return self.rect.top
        elif side == "left":
            return self.rect.left
        elif side == "right":
            return self.rect.right
        elif side == "bottom":
            return self.rect.bottom
        else:
            raise ValueError(f"{side} is not a proper argument.")
        
        
            
    
    

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGTH = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGTH))

test_obj: Sprite = Rectangle(600, 100, 100, 100, (255,255,255))
test_group = pygame.sprite.Group()
test_group.add(test_obj)

running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    test_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

