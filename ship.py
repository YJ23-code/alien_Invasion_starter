"""
Program Name: Attacked by Rebels - Track 2
Author: Yasir 
Purpose: Control the X-wing spaceship, movement, and positioning.
Starter Code Links: Alien Invasion in class tutorial
Date: 11/22/2026
"""





import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Represent the players x wing spaceship."""
    def __init__(self, ai_game):
        """Initialize the X wing image, position and movement"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(
            self.settings.ship_file
        ).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image, (80, 100)
        )
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the ship smoothly in all four directions."""
        if self.moving_right:
            self.x += 5

        if self.moving_left:
            self.x -= 5

        if self.moving_up:
            self.y -= 5

        if self.moving_down:
            self.y += 5

        # Keep the ship inside the screen.
        self.x = max(
            0,
            min(self.x, self.screen_rect.width - self.rect.width)
        )

        self.y = max(
            0,
            min(self.y, self.screen_rect.height - self.rect.height)
        )

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def blitme(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Reset the X-wing to the bottom center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False