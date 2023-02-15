import pygame
from failure_screen import failure_screen
from pygame import Surface, Rect
from direction_tracker import DirectionTracker


pygame.init()

WIDTH: int = 800
LENGTH: int = 500
screen = pygame.display.set_mode((WIDTH, LENGTH))
clock = pygame.time.Clock()



# Player 1
p1_bat: Surface = pygame.surface.Surface((20, 100))
p1_bat.fill((255,255,255))
p1_rect: Rect = p1_bat.get_rect(center=(WIDTH/16, LENGTH*0.5))

# Player 2
p2_bat: Surface = pygame.surface.Surface((20, 100))
p2_bat.fill((255, 0, 0))
p2_rect: Rect = p2_bat.get_rect(center=(WIDTH/16*15, LENGTH*0.5))

# ball
ball: Surface = pygame.image.load("pygame_shenanigans/pong/ball.png")
ball_rect = ball.get_rect(center=(WIDTH*0.5, LENGTH*0.5))
dt = DirectionTracker()
speed = 1.8

running: bool = True
while running:
    keys_pressed = pygame.key.get_pressed()

    # making moving more fluid
    if keys_pressed[pygame.K_w]:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        
        # player actions
        """
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1_rect.top -=30
                
            if event.key == pygame.K_s:
                p1_rect.top +=30
                """
    print(f"{ball_rect.top} and {ball_rect.bottom}")
    print(dt.get_direction())
    # collision rules:
    if ball_rect.top < 0:
        print("TOP REACHED")
        ball_rect.centery += 5
        dt.invert_vertical()

    elif ball_rect.bottom > LENGTH:
        # ball_rect.bottom - 5
        print("BOTTOM REACHED")
        dt.invert_vertical()
        

    if ball_rect.right == WIDTH:
        # ball_rect.right = -5
        dt.invert_horizontal()

    # --stops game--
    if ball_rect.centerx <= 0:
        pygame.quit()
        pygame.init()
        failure_screen()
        
    
    # Collision P1
    if ball_rect.colliderect(p1_rect):
        ball_rect.left + 5
        speed = speed * 1.1
        dt.invert_horizontal()

    # Collision P2
    if p2_rect.colliderect(ball_rect):
        speed = speed*1.1
        dt.invert_horizontal()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        if pressed[pygame.K_SPACE]:
            p1_rect.centery -= 15
        else:
            p1_rect.centery -= 7.5
    if pressed[pygame.K_s]:
        if pressed[pygame.K_SPACE]:
            p1_rect.centery += 15
        else:    
            p1_rect.centery += 7.5



    #ball logic
    ball_rect.centerx = ball_rect.centerx + dt.get_grid_movement()[0] * speed
    ball_rect.centery = ball_rect.centery + dt.get_grid_movement()[1] * speed


    screen.fill((0,0,0))
    screen.blit(p1_bat, p1_rect)
    p2_rect.centery = ball_rect.centery
    screen.blit(p2_bat, p2_rect)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(30)