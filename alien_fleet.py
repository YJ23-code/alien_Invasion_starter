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
        alien_height = self.settings.alien_h
        available_space_y = self.settings.screen_h - (3 * alien_height) - self.settings.ship_h
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
         for alien_number in range(number_aliens_x):
           x = alien_width + 2 * alien_width * alien_number
           y = alien_height + 2 * alien_height * row_number

           alien = Alien(self.game, x, y)
           self.aliens.add(alien)

    def check_fleet_edges(self):
     """Drop the fleet and reverse direction at screen edges."""
     for alien in self.aliens.sprites():
        if alien.check_edges():
            self.change_fleet_direction()
            break

    def change_fleet_direction(self):
     """Move the fleet downward and reverse its direction."""
     for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed

     self.settings.fleet_direction *= -1    

    def update_fleet(self):
     """Check the fleet edges and update all aliens."""
     self.check_fleet_edges()
     self.aliens.update()

    def check_aliens_bottom(self):
        """Check if any alien has reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                return True

        return False