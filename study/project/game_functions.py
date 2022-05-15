#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import sys
import pygame
from time import sleep


from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Response by pressing the keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """If the limit is not reached, fired a bullet"""
    # Create a bullet and it to the group 'bullets'
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Response release keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Response to keyboard and mouse press events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update the image on the screen and switch to the new screen"""
    # Redraw the screen in each time the loop
    screen.fill(ai_settings.background_color)
    # Draw all the bullets behind the spaceship and the aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blit_image()
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """Update the bullets position and delete lost bullets"""
    # Update the bullets position
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    # Check to see if a bullet hit the alien
    # If so, delete the bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Delete all existing bullets and create a new swarm of aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculate how many aliens each row can hold"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate how many aliens liens the screen can hold"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create a alien and add join the current line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create alien groups"""
    # Create an alien and calculate how many aliens a row can hold
    # The distance between aliens is the width of aliens
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first line of Aliens
    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, number_row)


def check_fleet_edges(ai_settings, aliens):
    """There are measures taken by aliens when they reach the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move all the aliens down and change their direction at the same time"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responding to a spaceship hit by an alien"""
    if stats.ships_left > 0:
        # 'ship_left' minus one
        stats.ships_left -= 1

        # Delete alien list and bullet list
        aliens.empty()
        bullets.empty()

        # Create a new group of aliens and defend the spaceship to the bottom center of the screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Stop
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check to see if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Deal with it like a spaceship is hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    Check if the aliens are at the edge of the screen
    Update the location of all aliens in the Alien Group
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check for collisions between spaceships and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Check to see if there are aliens at the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
