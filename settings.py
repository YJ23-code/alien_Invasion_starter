from pathlib import Path

class Settings:
    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship.png'
        self.ship_limit = 3
        self.ship_h = 60
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 50
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # Initialize settings that change during gameplay.
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change during gameplay."""
        self.bullet_speed = 7
        self.fleet_speed = 5
        self.fleet_direction = 1   

    def increase_difficulty(self):
        """Increase the game's speed settings."""
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale  