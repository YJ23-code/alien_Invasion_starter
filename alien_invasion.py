import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h)
        )

        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)
        self.arsenal = Arsenal(self)
        self.fleet = AlienFleet(self)
        self.fleet.create_fleet()

    def run_game(self):
        """Start the main game loop."""
        while self.running:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.arsenal.update_arsenal()
                self.fleet.update_fleet()

                if pygame.sprite.spritecollideany(
                    self.ship, self.fleet.aliens
                ):
                    self._ship_hit()

                elif self.fleet.check_aliens_bottom():
                    self._ship_hit()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _ship_hit(self):
        """Respond when an alien hits the ship or reaches the bottom."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            print(f"Ships left: {self.stats.ships_left}")

            if self.stats.ships_left == 0:
                self.stats.game_active = False
                print("Game Over!")
            else:
                self.fleet.create_fleet()
                self.settings.fleet_direction = 1

                # Reset the spaceship position.
                self.ship.rect.midbottom = self.ship.screen_rect.midbottom
                self.ship.x = float(self.ship.rect.x)

                # Stop any previous horizontal movement.
                self.ship.moving_right = False
                self.ship.moving_left = False

                # Clear existing bullets.
                self.arsenal.arsenal.empty()

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if self.stats.game_active:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.ship.rect.y -= 5
                    elif event.key == pygame.K_DOWN:
                        self.ship.rect.y += 5
                    elif event.key == pygame.K_SPACE:
                        if self.arsenal.fire_bullet():
                            pygame.mixer.Sound(
                                self.settings.laser_sound
                            ).play()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.blitme()
        self.arsenal.draw()
        self.fleet.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()