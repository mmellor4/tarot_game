import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the window (600x600)
window = pygame.display.set_mode((600, 600))

# Load the images for the animation

frame1 = pygame.image.load("../smiley/l0_smiley1.png")
frame2 = pygame.image.load("../smiley/l0_smiley2.png")
frame3 = pygame.image.load("../smiley/l0_smiley3.png")
frame4 = pygame.image.load("../smiley/l0_smiley4.png")
frame5 = pygame.image.load("../smiley/l0_smiley5.png")
frame6 = pygame.image.load("../smiley/l0_smiley6.png")

image_sprite = [
    pygame.transform.scale(frame1, (300, 300)),
    pygame.transform.scale(frame2, (300, 300)),
    pygame.transform.scale(frame3, (300, 300)),
    pygame.transform.scale(frame4, (300, 300)),
    pygame.transform.scale(frame5, (300, 300)),
    pygame.transform.scale(frame6, (300, 300))
]


# Clock to control frame rate
clock = pygame.time.Clock()

# Counter for image iteration
value = 0

# Variable to keep the game running
run = True

while run:
    # Event handling: Look for quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    # Set the framerate to 3fps
    clock.tick(5)

    # Reset 'value' when it reaches the end of the list
    if value >= len(image_sprite):
        value = 0

    # Get the current sprite image
    image = image_sprite[value]

    # Set the starting position
    x = 150
    if value == 0:
        y = 200
    else:
        y = 206

    # Fill the screen with black before drawing the new image
    window.fill((0, 0, 0))

    # Display the current sprite image
    window.blit(image, (x, y))

    # Update the display surface
    pygame.display.update()

    # Increase the value to switch to the next image
    value += 1

# Quit pygame
pygame.quit()
