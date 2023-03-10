import pygame
import sys

pygame.init()

width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("End of Game")

car_image = pygame.image.load("gameover.png")

x = -600
y = 0

speed = 200

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))

    x += speed / pygame.time.get_ticks()

    screen.blit(car_image, (x, y))

    if x > width - car_image.get_width():
        speed = 0

    pygame.display.flip()
