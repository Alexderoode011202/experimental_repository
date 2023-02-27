import pygame
from pygame import Rect, Surface
import sys

pygame.init()

# screen initialization
WIDTH: int = 1000
HEIGTH: int = 700
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.mouse.set_cursor
# clock initiatilization
clock = pygame.time.Clock()

# (partial) map initialization


# Mouse adjustment
cursor_surf: Surface = pygame.image.load("pygame_shenanigans/diverse/crosshair.png")
cursor_surf = pygame.transform.scale_by(cursor_surf, 0.5)

# Player initialization
player: Surface = pygame.image.load("pygame_shenanigans/diverse/stickfigure.png")
player = pygame.transform.scale_by(player, 0.5)
player_flipped_surf = pygame.transform.flip(player, True, False)
player_flipped: bool = False
player_rect = player.get_rect(midbottom = ((WIDTH* 0.5, HEIGTH)))

# core
running: bool = True
while running:
    keyboard = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # player input
    if keyboard[pygame.K_d]:
        player_rect.centerx +=2.5
        if player_rect.right >= WIDTH:
            player_rect.right = WIDTH
    # walk left
    if keyboard[pygame.K_a]:
        player_rect.centerx -=2.5
        if player_rect.left <= 0:
            player_rect.left = 0


        

    # jump
    ...

    #flip checking
    if pygame.mouse.get_pos()[0] < player_rect.centerx:
        player_flipped = True
    else:
        player_flipped = False
        
    
    screen.fill("grey")
    # Add extra stuff below this line:

    cursor_rect = cursor_surf.get_rect(center = pygame.mouse.get_pos())
    screen.blit(cursor_surf, cursor_rect)
    if player_flipped:
        screen.blit(player, player_rect)
    else:
        screen.blit(player_flipped_surf, player_rect)

    pygame.display.update()
    clock.tick(60)