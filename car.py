import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 150

CAR_SPEED = 5


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("car.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"

    def update(self):
        if self.direction == "right":
            self.rect.x += CAR_SPEED
            if self.rect.right > SCREEN_WIDTH:
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "left"
        else:
            self.rect.x -= CAR_SPEED
            if self.rect.left < 0:
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = "right"


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprites_list = pygame.sprite.Group()
car = Car(0, 30)
all_sprites_list.add(car)

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.update()

    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
