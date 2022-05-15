#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """Initialize a single alien class"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each alien is initially attached to the top of left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact location of the aliens
        self.x = float(self.rect.x)

    def bilt_image(self):
        """Draw an alien at a specified location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """If the alien is at the edge of the screen return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
