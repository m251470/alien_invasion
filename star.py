import pygame
from pygame.sprite import Sprite
from settings1 import Settings

class Star(Sprite):
    """Single Alien in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Load Star image and set its rect
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.y = float(self.rect.y)
    def check_gone(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False
    def update(self):
        """Move alien"""
        self.y += (self.settings.star_speed)
        self.rect.y = self.y

