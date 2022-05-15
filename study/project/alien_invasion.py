#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import os
import pygame

from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Center the output windows
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Setting caption
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Create a spaceship, a bullet group and an alien group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create alien groups
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
