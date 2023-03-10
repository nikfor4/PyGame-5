import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BOMB_SIZE = 50


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bomb.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_exploded = False

    def explode(self):
        if not self.is_exploded:
            self.is_exploded = True
            self.image = pygame.image.load("boom.png").convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()

bombs = []

for i in range(20):
    x = random.randrange(BOMB_SIZE, SCREEN_WIDTH - BOMB_SIZE)
    y = random.randrange(BOMB_SIZE, SCREEN_HEIGHT - BOMB_SIZE)
    bomb = Bomb(x, y)
    all_sprites.add(bomb)
    bombs.append(bomb)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            for bomb in bombs:
                if bomb.rect.collidepoint(event.pos):
                    bomb.explode()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
