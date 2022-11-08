import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        #Create bullet at (0,0)
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        #Store the bullet's position as a decimal value
        self.x = float(self.rect.x)
    def update(self):
        """Move bullet up the screen"""
        #Update decimal position
        self.x += self.settings.bullet_speed
        #Update the rect
        self.rect.x = self.x
    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)