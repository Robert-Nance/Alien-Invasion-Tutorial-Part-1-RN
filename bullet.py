import pygame

from pathlib import Path

from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        bullet_path = (
            Path(__file__).resolve().parent
            / "images" 
            / "Bullet.png"
        )
        self.image = pygame.image.load(str(bullet_path))

        # Resize the bullet.
        self.image = pygame.transform.scale(
            self.image, (12, 30)
        )

        # Create a rectangle from the image.
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)