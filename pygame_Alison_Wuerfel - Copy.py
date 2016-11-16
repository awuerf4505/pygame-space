# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (1000, 550)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60



# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
DARK_BLUE=(1, 20, 25)
MERCURY = (112, 112, 117)
VENUS = (173, 103, 18)    
EARTH = (43, 68, 196)
MARS = (255, 33, 0)
JUPITER = (217, 150, 61)
SPOT = (175, 41, 0)
SPOTTWO = (99, 23, 0)
SPOTTHREE = (204, 63, 20)
SATURN = (252, 119, 53)
SATURNRINGSONE = (198, 66, 0)
SATURNRINGSTWO = (173, 117, 90)
SATURNRINGSTHREE =(244, 173, 66)
URANUS = (102, 189, 232)
URANUSLOOP = (234, 255, 255)
NEPTUNE = (89, 125, 217)
NEPTUNELOOP = (220, 247, 255)
GREY = (112, 112, 112)


stars = []
for n in range(3500):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 550)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

    
# Game loop
done = False




        
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''

    

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
    pygame.draw.ellipse(screen, ORANGE, [0, 148, 277, 278])
    pygame.draw.ellipse(screen, MERCURY, [290, 265, 12, 13])
    pygame.draw.ellipse(screen, VENUS, [310, 258, 25, 26])
    pygame.draw.ellipse(screen, EARTH, [337, 258, 28, 29])
    pygame.draw.rect(screen, GREEN, [344, 262, 10, 11])
    pygame.draw.rect(screen, GREEN, [341, 269, 10, 11])
    pygame.draw.rect(screen, GREEN, [359, 262, 3, 4])
    pygame.draw.rect(screen, GREEN, [362, 272, 3, 4])
    pygame.draw.ellipse(screen, MARS, [370, 262, 20, 21])
    pygame.draw.ellipse(screen, JUPITER, [400, 195, 150, 151])
    pygame.draw.ellipse(screen, SPOTTHREE, [445, 280, 45, 25])
    pygame.draw.ellipse(screen, SPOT, [450, 285, 35, 15])
    pygame.draw.ellipse(screen, SPOTTWO, [455, 290, 15, 7])
    pygame.draw.ellipse(screen, SATURN, [577, 200, 135, 134])
    pygame.draw.ellipse(screen, SATURNRINGSONE, [562, 250, 170, 6])
    pygame.draw.ellipse(screen, SATURNRINGSTWO, [556, 258, 180, 6])
    pygame.draw.ellipse(screen, SATURNRINGSTHREE, [556, 266, 185, 6])
    pygame.draw.ellipse(screen, SATURNRINGSTWO, [556, 274, 180, 6])
    pygame.draw.ellipse(screen, SATURNRINGSONE, [562, 282, 170, 6])
    pygame.draw.ellipse(screen, URANUS, [755, 250, 34, 35])
    pygame.draw.ellipse(screen, URANUSLOOP, [772, 248, 2, 40])
    pygame.draw.ellipse(screen, NEPTUNE, [796, 250, 34, 35])
    pygame.draw.ellipse(screen, NEPTUNELOOP, [793, 262, 40, 2])
    pygame.draw.ellipse(screen, NEPTUNELOOP, [793, 265, 40, 2])
    pygame.draw.ellipse(screen, NEPTUNELOOP, [793, 268, 40, 2])
    pygame.draw.polygon(screen, WHITE, [[ 607,189 ], [622, 182] , [607 ,175]] , 1)
    pygame.draw.rect(screen, WHITE, [577, 175, 30, 15])
    pygame.draw.polygon(screen, WHITE, [[ 577,175 ], [577, 165] , [585 ,175]] , 1)
    pygame.draw.polygon(screen, BLUE, [[ 902 ,95 ], [925, 300] , [883 ,300]])
    pygame.draw.ellipse(screen, GREEN, [891, 89, 25, 26])
    pygame.draw.rect(screen, WHITE, [888, 100, 32, 15])
    pygame.draw.rect(screen, GREY, [902, 222, 8, 9])




 


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
