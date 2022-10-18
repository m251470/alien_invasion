### This is DJ's pyga
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Manage game assets and behavior"""
    def __int__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #set background color
        self.bg_color = (230,230,230)
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass thorugh the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #make the most recently drawn screen visible
            pygame.display.flip()
if __name__ == '__main__':
    #Make a game instance, and run game
    ai = AlienInvasion()
    ai.run_game()
