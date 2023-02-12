import pygame
from sys import exit

pygame.init()
pygame.display.set_caption("Call of Duty 2023 Premium Edition")

WIDTH: int = 780
LENGTH: int = 400
screen = pygame.display.set_mode((WIDTH, LENGTH))
screen.fill(color=(0,0,255))
clock = pygame.time.Clock()
boring_font = pygame.font.Font("pygame_shenanigans/pixel_font.ttf", 20)

test_surface = pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/ground.png")
air_surface = pygame.image.load("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/pygame_shenanigans/Air.jpg")
text_surface = boring_font.render("What am I doing?", True, "black")
pz3_surface = pygame.image.load("pygame_shenanigans/pz_3_without_background.png")
pz3_x: int = 429
pz3_y: int = 249
running: bool = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    # Background
    screen.blit(test_surface, (0, LENGTH-test_surface.get_height()))
    screen.blit(air_surface, (0, LENGTH-test_surface.get_height()-air_surface.get_height()))
    
    # text
    screen.blit(source=text_surface, dest=(WIDTH*0.5, LENGTH*0.5))

    # tank
    pz3_x -=2
    if pz3_x <= 0:
        pz3_x = WIDTH

    screen.blit(pz3_surface, (pz3_x, pz3_y))


    pygame.display.update()
    clock.tick(60)

    
