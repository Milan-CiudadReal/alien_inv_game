import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image, (150, 175))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # movement flags
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """ update the ships position based on movement flags"""
        # update the ships x val, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
