import json
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        # High score should not reset with each new game.
        self.high_score = 0
        # Location of the saved high-score file.
        self.high_score_file = Path(__file__).parent / "high_score.json"
        # Load the saved high score.
        try:
            self.high_score = json.loads(
                self.high_score_file.read_text()
            )
        except (FileNotFoundError, json.JSONDecodeError):
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the high score to a JSON file."""
        self.high_score_file.write_text(
            json.dumps(self.high_score)
        )