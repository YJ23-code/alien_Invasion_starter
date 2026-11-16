"""
Program Name: Attacked by Rebels - Track 2
Author: Yasir 
Purpose: Run the main game and control the x-wing player, laser firing, and game screen for Milestone 1 
Starter Code Links: Alien Invasion in class tutorial
Date: 11/15.2026
"""


import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage the lasers fired by the player's X-Wing."""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the laser group and game settings."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
            
    def update_arsenal(self) -> None:
        """Update all active lasers for Milestone 1."""
        self.arsenal.update()
        # Disabled for milestone 1

    def draw(self) -> None:

     """Draw all active lasers on the screen."""
     for bullet in self.arsenal:
            bullet.draw_bullet()


    

    def fire_bullet(self) -> bool:
        """Fire a laser if the maximum number has not been reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False  