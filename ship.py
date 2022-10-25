import pygame

class Ship:
    """Ship Class"""
    def __init__(self, ai_game):
        """Get ship and starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Ship's image
        self.image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()

        #Ship's position at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal vlae for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ship's position based on movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Update rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
