# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            # event loop to track user input
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        # sets event loop to track for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # checks to see if right arrow is pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # handles when keys are pressed
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    # handles when keys are released
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # brings screen to front
        pygame.display.flip()


# sets up the game and runs it
if __name__ ==  '__main__':
    ai = AlienInvasion()
    ai.run_game()