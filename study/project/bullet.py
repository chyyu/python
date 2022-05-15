#!/usr/bin/env python
# -*- coding:utf-8 -*-
# chy
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that manages the bullets launched by a spaceship"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rectangle representing the bullet at '(0 ,0)', and set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet position with decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move up"""
        # Update the bullet position with decimal
        self.y -= self.speed_factor
        # Update the bullet's 'rect' position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
