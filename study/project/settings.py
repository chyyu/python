#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy


class Settings:
    """Class to store all settings 'alien invasion'"""

    def __init__(self):
        """Initialize game settings"""
        # Screen setting
        self.screen_width = 1600
        self.screen_height = 1000
        self.background_color = (230, 230, 230)

        # Spaceship settings
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # A 'fleet_direction' value of 1 indicates a right move and value of -1 indicates left move
        self.fleet_direction = 1




