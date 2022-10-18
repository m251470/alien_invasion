import pygame

class Ship:
    """Ship Class"""
    def __init__(self, ai_game):
        """Get ship and starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Ship's image
        self.image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()

        #Ship's position at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
