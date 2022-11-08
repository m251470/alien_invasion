import pygame
from pygame.sprite import Sprite
from settings1 import Settings
from random import randint

class Star(Sprite):
    """Single Alien in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Load Star image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left corner
        self.rect.left = self.screen.get_rect().right
        self.rect.y = self.rect.height
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    def check_gone(self):
        if self.rect.right > self.screen.get_rect().left:
            return True
        else:
            return False
    def update(self):
        """Move alien"""
        self.x -= (self.settings.star_speed)
        self.rect.x = self.x

