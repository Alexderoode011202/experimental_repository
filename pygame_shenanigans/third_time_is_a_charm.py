import pygame
from sys import exit
from failure_screen import failure_screen

pygame.init()
pygame.display.set_caption("Call of Duty 2023 Premium Edition")

WIDTH: int = 780
LENGTH: int = 400
screen = pygame.display.set_mode((WIDTH, LENGTH))
screen.fill(color=(0,0,255))
clock = pygame.time.Clock()
boring_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 20)
smaller_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 10)
test_surface = pygame.image.load("pygame_shenanigans/ground.png").convert()
test_rect = test_surface.get_rect(midbottom = (WIDTH*0.5, LENGTH))

air_surface = pygame.image.load("pygame_shenanigans/Air.jpg").convert()
air_rect = air_surface.get_rect(midbottom=(WIDTH*0.5,LENGTH - test_surface.get_height()))

text_surface = boring_font.render("What am I doing?", True, "black")
text_rect = text_surface.get_rect(midtop=(WIDTH*0.5, 0))

smaller_text = smaller_font.render("I have no idea!!", False, (0,0,0))
smaller_text_rect = smaller_text.get_rect(midtop=(WIDTH * 0.5, text_rect.bottom))


pz3_surface = pygame.image.load("pygame_shenanigans/pz_3_without_background.png").convert_alpha()
pz3_rect = pz3_surface.get_rect(bottomright=(WIDTH*0.7, LENGTH))

# object for directions

running: bool = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            pygame.init()
            failure_screen()
            
            exit()

    # Background
    screen.blit(test_surface, test_rect)
    screen.blit(air_surface, air_rect)
    
    # text
    screen.blit(text_surface, text_rect)
    screen.blit(smaller_text, smaller_text_rect)

    # tank
    pz3_rect.left -=10
    if pz3_rect.right <= 0:
        pz3_rect.left = WIDTH


    screen.blit(pz3_surface, pz3_rect)


    pygame.display.update()
    clock.tick(60)

    
