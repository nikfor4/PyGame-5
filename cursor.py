import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

cursor_img = pygame.image.load("cursor.png")

pygame.mouse.set_cursor(*pygame.cursors.arrow)

while True:
    pygame.mouse.set_visible(False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    if pygame.mouse.get_focused():
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, (mouse_pos[0], mouse_pos[1]))

    pygame.display.flip()
