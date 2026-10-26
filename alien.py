import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game, x, y):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(x)

    def update(self):
        """Move the alien horizontally."""
        if self.check_edges():
            self.settings.fleet_direction *= -1

        self.x += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self):
        """Return True if the alien is at either edge of the screen."""
        return (
            self.rect.right >= self.screen_rect.right
            or self.rect.left <= self.screen_rect.left
        )