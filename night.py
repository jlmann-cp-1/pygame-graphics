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

''' Make stars '''
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, YELLOW, s)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
