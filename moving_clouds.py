# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

# Make picture objects



# Drawing functions
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_sun():
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

def draw_ground():
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

# Game loop
running = True

while running:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   


    # Game logic

             
    # Drawing code
    screen.fill(BLUE)
    draw_sun()
    
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)
        
    draw_ground()
    

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
