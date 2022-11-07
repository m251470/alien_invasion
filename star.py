import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Single star in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        #Load Star image and set its rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        #Start each new star near the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the star's exact horizontal position
        self.x = float(self.rect.x)
