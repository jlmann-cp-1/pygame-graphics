# Imports
import pygame


# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Grid"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

def draw_grid(width, height, scale):
    '''
    Draws a grid that can overlay your picture.
    This should make it easier to figure out coordinates
    when drawing pictures.
    '''
    for x in range(0, width, scale):
        pygame.draw.line(screen, GRAY, [x, 0], [x, height], 1)
    for y in range(0, height, scale):
        pygame.draw.line(screen, GRAY, [0, y], [width, y], 1)

        
# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    # Drawing code
    screen.fill(WHITE)

    draw_grid(800, 600, 20) # make this the last line in your drawing code

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
