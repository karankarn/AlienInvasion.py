import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ship image and get rect
        self.image = pygame.image.load('Images/ship.bmp.')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #start ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Store a decimal value for ships center
        self.center = float(self.rect.centerx)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        #center ship on screen
        self.center = self.screen_rect.centerx

    def update(self):
        #Update ships position based on movement flags by
        #updating ships center value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx =self.center


    def blitme(self):
        self.screen.blit(self.image,self.rect)

