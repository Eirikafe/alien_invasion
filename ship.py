import pygame

class Ship:

    def __init__(self, ai_game):
        """Initializes the ship and sets starting location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship and get it's rect
        self.image = pygame.image.load('resources/ship.bmp')
        self.rect = self.image.get_rect()
        # set ship at bottom middle
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # set default status for ship movement
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x