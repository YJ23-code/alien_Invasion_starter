import pygame
from pathlib import Path


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(
            self.settings.ship_file
        )
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)


    def update(self):
        if self.moving_right:
            self.x += 1
        if self.moving_left:
            self.x -= 1

        self.rect.x = int(self.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)