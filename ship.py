import pygame


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
        """Move the ship and keep it inside the screen."""

        if self.moving_right:
            self.x += 5

        if self.moving_left:
            self.x -= 5

        # Prevent the ship from leaving the screen.
        self.x = max(
            0,
            min(self.x, self.screen_rect.width - self.rect.width)
        )

        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)