"""
Program Name: Attacked by Rebels - Track 2
Author: Yasir 
Purpose: Run the main game and control the x-wing player, laser firing, and game screen for Milestone 1 
Starter Code Links: Alien Invasion in class tutorial
Date: 11/15.2026
"""




import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from button import Button
from hud import HUD


class AlienInvasion:
    """Manage the Rebel Assault game, player controls """
    def __init__(self):
        """Intialize the game settings, screen, ship, and lasers"""
        pygame.init()
        self.settings = Settings()
        #Disabled for milestone 1
        #self.stats = GameStats(self)
        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        # Make the play button.
        #self.play_button = Button(self, "Play")
        # Create the HUD.
       # self.hud = HUD(self)
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
        #Disabled till milestone 2
        self.fleet = AlienFleet(self)
        self.fleet.create_fleet()

    def run_game(self):
        """Milestone 1 player prototype"""
        while self.running:
            self._check_events()
            # Milestone 1: Only update the player and lasers.

            
            self.ship.update()
            self.arsenal.update_arsenal()

            # Fleet and collision disabled for milestone 1 
            self.fleet.update_fleet()

                

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _ship_hit(self):
        """Respond when an alien hits the ship or reaches the bottom."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            print(f"Ships left: {self.stats.ships_left}")
            # Update the remaining ship icons.
            self.hud.prep_ships()

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

            #elif event.type == pygame.MOUSEBUTTONDOWN:
                
                #mouse_pos = pygame.mouse.get_pos()
                #self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            self.restart_game() 



    def restart_game(self):
        """reset game stats,difficulty, and player position."""
        self.stats.reset_stats()
        # Reset the difficulty to its starting settings.
        self.settings.initialize_dynamic_settings()
        # Reset the HUD for a new game.
        self.hud.prep_score()
        self.hud.prep_high_score()
        self.hud.prep_level()
        self.hud.prep_ships()

        self.stats.game_active = True    
        self.arsenal.arsenal.empty()  
        self.settings.fleet_direction = 1
        self.fleet.create_fleet()  
        self.ship.center_ship()

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.blitme()
        self.arsenal.draw()
        self.fleet.aliens.draw(self.screen)
        # Draw theplay button if the game is inactive.
        # Disable for milestone 1 
        #if not self.stats.game_active:
            #self.play_button.draw_button()
            # Draw the HUD.
        #self.hud.show_hud()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()