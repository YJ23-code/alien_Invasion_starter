import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
            
    def update_arsenal(self) -> None:
        self.arsenal.update()
        pygame.sprite.groupcollide(
            self.arsenal,
            self.game.fleet.aliens,
            True,
            True
        )

        if not self.game.fleet.aliens:
            self.game.fleet.create_fleet()

    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()


    

    def fire_bullet(self) -> bool:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False  