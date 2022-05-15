#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and setting its initial position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image of the spaceship and get its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put each spaceship in the center at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store the decimal in the attribute 'center' of the spaceship
        self.center = float(self.rect.centerx)

        # Movement signs
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Adjust the position of the spaceship according to the moving sign"""
        # Update the spaceship's 'center' value instead of 'rect' value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # According to 'self.center' to update 'rect' object
        self.rect.centerx = self.center

    def blit_image(self):
        """ Draw the spaceship in specified position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center the ship on the screen
        self.center = self.screen_rect.centerx
