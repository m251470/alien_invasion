### This is DJ's pygame
import sys
import pygame
from settings1 import Settings
from ship import Ship
from bullet1 import Bullet
from star import Star
from random import randint
from time import sleep
from game_stats import GameStats
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

        self.stats = GameStats(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
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
        #Rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_star_collisions()

    def _check_bullet_star_collisions(self):
        # Check for bullets that hit aliens and get ride of bullet and alien if so
        collisions = pygame.sprite.groupcollide(self.bullets, self.stars, True, True)
        if not self.stars:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()


    def _create_fleet(self):
        """Create fleet of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_y = self.settings.screen_height - (2* star_height)
        number_stars_y = available_space_y // (2* star_height)

        #Determine the number of rows of stars that fit on screen
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (3*star_width) - ship_width)
        number_col = available_space_x // (2* star_width)

        #Create the full fleet
        for col_number in range(number_col):
            for star_number in range(number_stars_y):
                self._create_star(star_number, col_number)
    def _create_star(self, star_number, col_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.y = star_height + 2 * star_height * star_number
        star.rect.y = star.y
        star.x = star_width + 2 * star.rect.width * col_number
        self.stars.add(star)
    def _check_fleet_edges(self):
        """Respond fleet to reaching edges"""
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """Drop the entire fleet and change fleets direction"""
        for star in self.stars.sprites():
            star.rect.x += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            self.stars.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for star in self.stars.sprites():
            if star.rect.left >= screen_rect.left:
                self._ship_hit()
                break

    def _update_star(self):
        """Update positions of all aliens in fleet"""
        self._check_fleet_edges()
        self.stars.update()
        if pygame.sprite.spritecollideany(self.ship, self.stars):
            self._ship_hit()
        self._check_aliens_bottom()

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
