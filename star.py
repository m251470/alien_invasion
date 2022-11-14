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
        self.rect.right = self.screen.get_rect().right
        self.rect.y = self.rect.height
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = self.rect.top

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    def check_gone(self):
        if self.rect.left > self.screen.get_rect().right:
            return True
        else:
            return False
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom or self.rect.bottom <= 0:
            return True
    def update(self):
        """Move alien"""
        self.y -= self.settings.star_speed * self.settings.fleet_direction
        self.rect.y = self.y

