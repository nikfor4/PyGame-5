import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

hero_image = pygame.image.load("hero.png")

hero_x = 0
hero_y = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                hero_x -= 10
            elif event.key == pygame.K_RIGHT:
                hero_x += 10
            elif event.key == pygame.K_UP:
                hero_y -= 10
            elif event.key == pygame.K_DOWN:
                hero_y += 10

    screen.fill((255, 255, 255))

    screen.blit(hero_image, (hero_x, hero_y))

    pygame.display.flip()

pygame.quit()
