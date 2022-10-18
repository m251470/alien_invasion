import pygame

class Ship:
    """Ship Class"""
    def __int__(self, ai_game):
        """Get ship and starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Ship's image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Ship's position at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
