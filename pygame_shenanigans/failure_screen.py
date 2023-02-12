from pygame import *
import pygame
import sys


def failure_screen() -> None:
    

    WIDTH: int = 800
    LENGTH: int = 400
    __screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()

    __screen.fill((0,0,0))

    large_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 75)
    small_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 25)
    smaller_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 10)

    ending: Surface = large_font.render("You lost!", True, (255,0,0))
    ending_rect = ending.get_rect(midtop=(WIDTH*0.5, 50))


    extra: Surface = small_font.render("Cuz fuck you!", True, (255,0,0))
    extra_rect = extra.get_rect(midtop=(ending_rect.centerx, ending_rect.bottom))

    smaller: Surface = smaller_font.render("Nah, just kidding, you tried your best :)", True, (255,0,0))
    smaller_rect = smaller.get_rect(midtop=(extra_rect.centerx, extra_rect.bottom + 50))

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        __screen.blit(ending, ending_rect)
        __screen.blit(extra, extra_rect)
        __screen.blit(smaller, smaller_rect)
        pygame.display.update()
        clock.tick(60)
