# Computer Programming 1
# A scene that uses loops to make randomly generated stars.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)

# Drawing functions
def draw_ground():
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    
def draw_moon(x, y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])
    
def draw_stars():
    pass


# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    screen.fill(BLACK)
    draw_stars()
    draw_moon(575, 75)
    draw_ground()

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
