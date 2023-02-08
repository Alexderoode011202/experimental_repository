import pygame
from pygame import Surface
import time
import os
WIDTH, HEIGHT = (900, 500)
WIN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World!")
FPS: int = 40

def draw_window(num):
    global WIN
    global PZ_3_IMAGE
    WIN.blit(PZ_3_IMAGE)
    pygame.display.update()

def main() -> None:
    clock = pygame.time.Clock()
    run: bool = True
    rgb_val: int = 0
    PZ_3_IMAGE: Surface = pygame.image.load(os.path.join("pygame_shenanigans", "PZ_3.jpeg"))
    T_26_IMAGE: Surface = pygame.image.load(os.path.join("pygame_shenanigans", "T_26.jpg"))
    while(run == True):
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
                pygame.quit()
        WIN.fill((255,255,255))
        pygame.display.update()
    pygame.quit()

    
print(__name__)
if __name__ == "__main__":
    main()