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
        """Create a V-shaped formation of TIE fighters."""
        self.aliens.empty()

        center_x = self.settings.screen_w // 2
        start_y = 60
        spacing_x = 90
        spacing_y = 65

        # Create the center TIE fighter.
        alien = Alien(self.game, center_x, start_y)
        self.aliens.add(alien)

        # Create the left and right sides of the V.
        for i in range(1, 5):
            left_x = center_x - (i * spacing_x)
            right_x = center_x + (i * spacing_x)
            y = start_y + (i * spacing_y)

            self.aliens.add(Alien(self.game, left_x, y))
            self.aliens.add(Alien(self.game, right_x, y))

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