import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

    

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
        self.alien = Alien(
            self,
            self.settings.alien_w,
            self.settings.alien_h
        )

    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self.arsenal.update_arsenal()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
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
                        pygame.mixer.Sound(self.settings.laser_sound).play()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                     self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                
               
                           

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.blitme()
        self.arsenal.draw()
        self.screen.blit(self.alien.image, self.alien.rect)
        pygame.display.flip()

            
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()