"""
Program Name: Attacked by Rebels - Track 2
Author: Yasir 
Purpose: Create a visual explosion when a TIE fighter is destroyed.
Starter Code: Alien Invasion in class tutorial
Date: 11/21/2026
"""

import pygame

class Explosion:
    """Create a short explosion animation"""

    def __init__(self, x, y):
        """Set the explosion postion, size, and duartion"""

        self.x = x
        self.y = y
        self.radius = 5
        self.max_radius = 35
        self.active = True

    def update(self):
        """Expand the explosion until it disappears."""
        self.radius += 2

        if self.radius >= self.max_radius:
            self.active = False

    def draw(self, screen):
        """Draw an orange explosion with a yellow center."""
        pygame.draw.circle(
            screen, (255, 100, 0),
            (self.x, self.y), self.radius
        )

        pygame.draw.circle(
            screen, (255, 220, 0),
            (self.x, self.y), max(1, self.radius // 2)
        )