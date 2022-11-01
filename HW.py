### This is DJ's pygame
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # set background color
        self.bg_color = (0, 0, 255)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()



    def _check_events(self):
        #Responds to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        # Move ship to the right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Move ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Move ship to the up
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Move ship to the down
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
            # Redraw the screen during each pass thorugh the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # make the most recently drawn screen visible
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run game
    ai = AlienInvasion()
    ai.run_game()
