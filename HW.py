### This is DJ's pygame
import sys
import pygame
from settings1 import Settings
from ship import Ship
from bullet import Bullet
from star import Star
from random import randint
random_number = randint(-10,10)
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
        self.stars = pygame.sprite.Group()
        self._create_fleet()
        # set background color
        self.bg_color = (0, 0, 255)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self._update_star()



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

        # Move ship to the up
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Move ship to the down
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the rest"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old ones"""
        self.bullets.update()
        # Rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))


    def _create_fleet(self):
        """Create fleet of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2* star_width)
        self.number_stars_x = available_space_x // (2* star_width)

        #Determine the number of rows of stars that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2* star_height)

        #Create the full fleet
        for row_number in range(number_rows):
            self._create_row(row_number)
    def _create_row(self, row_number):
        for star_number in range(self.number_stars_x):
            self._create_star(star_number, row_number)
    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 2 * star_width * star_number
        star.y = 2* star.rect.height * row_number
        star.rect.y = star.y
        self.stars.add(star)


    def _update_star(self):
        """Update positions of all aliens in fleet"""
        self.stars.update()
        make_new_star = False
        for star in self.stars.copy():
            if star.check_gone():
                self.stars.remove(star)
                make_new_star = True
        if make_new_star:
            self._create_row(0)


    def _update_screen(self):
            # Redraw the screen during each pass thorugh the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # make the most recently drawn screen visible
        self.stars.draw(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run game
    ai = AlienInvasion()
    ai.run_game()
