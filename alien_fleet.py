import pygame
from alien import Alien

class AlienFleet:
    """A class to manage a fleet of aliens"""

    def __init__(self, game):
        """Initialize the alien fleet"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.aliens = pygame.sprite.Group()

    def create_fleet(self):
        """Create a single row of aliens."""
        self.aliens.empty()   

        alien_width = self.settings.alien_w
        available_space_x = self.settings.screen_w
        number_aliens_x = available_space_x // (2* alien_width)
        for alien_number in range(number_aliens_x):
            x = alien_width + 2 * alien_width * alien_number
            y = self.settings.alien_h

            alien = Alien(self.game, x, y)
            self.aliens.add(alien)

    def check_fleet_edges(self):
      """Reverse direction if any alien reaches a screen edge."""
      for alien in self.aliens.sprites():
        if alien.check_edges():
            self.settings.fleet_direction *= -1
            break

    def update_fleet(self):
     """Check the fleet edges and update all aliens."""
     self.check_fleet_edges()
     self.aliens.update()