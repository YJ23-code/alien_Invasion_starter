"""
Program Name: Attacked by Rebels - Track 2
Author: Yasir 
Purpose: Create and control the X-wing laser projectiles.
Starter Code Links: Alien Invasion in class tutorial
Date: 11/22/2026
"""



import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represent a laser fired from the X-Wing."""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the laser image and starting position."""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the laser upward on the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        """Draw the laser on the game screen."""
        self.screen.blit(self.image, self.rect)