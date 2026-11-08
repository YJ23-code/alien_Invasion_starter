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
        collisions = pygame.sprite.groupcollide(
            self.arsenal,
            self.game.fleet.aliens,
            True,
            True
        )
        # Award points for each destroyed alien.
        if collisions:
            for aliens_hit in collisions.values():
                self.game.stats.score += 50 * len(aliens_hit)
                self.game.hud.prep_score()
                            # Check for a new high score.
            if self.game.stats.score > self.game.stats.high_score:
                self.game.stats.high_score = self.game.stats.score
                self.game.stats.save_high_score()
                self.game.hud.prep_high_score()

        if not self.game.fleet.aliens:
            self.settings.increase_difficulty()
            self.game.fleet.create_fleet()
            self.game.stats.level += 1
            self.game.hud.prep_level()

    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()


    

    def fire_bullet(self) -> bool:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False  