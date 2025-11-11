import pygame
import sys

pygame.init()

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Example")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):   # <-- fixed __init__
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(SURFACE_COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

sprite = Sprite(COLOR, 100, 100)
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
