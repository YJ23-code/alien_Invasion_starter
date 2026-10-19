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

    def blitme(self):
        self.screen.blit(self.image, self.rect)