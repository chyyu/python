#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class GameStats:
    """Track game statistics"""

    def __init__(self, ai_settings):
        """Initialize information for statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.ships_left = self.ships_left

        # The game is active at the beginning
        self.game_active = True

    def reset_stats(self):
        """Initialize statistical information that may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
