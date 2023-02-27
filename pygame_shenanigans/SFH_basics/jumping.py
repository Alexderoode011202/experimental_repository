"""Here we create custom classes in which we can create full fledged operators, 
which are able to be used by AI as well. Here you can decide:
1.How fast they can walk
2.How they jump
3.Set their HP
4.Set the damage and rate of fire of their weapon
5.set magazine size
6.set bullet speed
7...."""

import pygame
from pygame import Rect, Surface
from typing import Optional, Tuple
class Soldier:
    def __init__(self, path: str, HP: int, damage: int, speed: float, magazine_size: int, reload_time: float, bullet_speed: float) -> None:
        self.surf: Surface = pygame.image.load(path)
        self.damage: int = damage
        self.speed: float = speed
        self.reload_time: float = reload_time
        self.magazine_size: int = magazine_size
        self.magazine: int = magazine_size
        self.bullet_speed: int = bullet_speed
        self.rect : Optional[Rect] = None

    def set_rect(self, pointer: str, pointer_coord: Tuple[int, int]) -> None:
        """sets a rectangle of the surface and keeps it in memory.
        :param pointer: decides where the pointer is meant to be on the surface. takes string values like: midbottom, topleft, etc.
        :pointer_coord: gives the location of where the pointer is meant to be on the screen
        :returns: None"""
        self.rect = self.surf.get_rect(pointer = pointer_coord)
        return None
    
    def get_rect(self) -> Optional[Rect]:
        """Returns the rectangle the object has"""
        return self.rect
    
    def get_flipped(self, x_axis: bool, y_axis: bool) -> Surface:
        """returns a flipped version of the Surface"""
        return pygame.transform.flip(self.surf, x_axis, y_axis)
    
    def fire(self) -> Optional[Tuple[Surface, Rect]]:
        """Lets the soldier fire. However, a projectile being fired is not guaranteed 
        because the soldier can only fire under certain conditions, like the magazine not being empty."""
        if self.magazine == 0:
            return None
        else:
            self.magazine -=1
            