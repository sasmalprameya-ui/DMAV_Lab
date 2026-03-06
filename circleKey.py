import pygame
import sys

# Initialize pygame
pygame.init()

# Screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle with Key Interaction")

# Circle properties
x = 300
y = 200
radius = 30
speed = 5

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Game loop
while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key interaction
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw circle
    pygame.draw.circle(screen, blue, (x, y), radius)

    pygame.display.update()