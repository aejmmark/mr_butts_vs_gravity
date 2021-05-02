"""Stage of the game, handles scrolling and sprite generation"""
from random import randint
import pygame
from effects import Effects
from sprites import Player, Platform, Baddie, Powerup
from constants import WIDTH, HEIGHT

class Stage:
    """Stage of the game, handles scrolling and sprite generation

    Args:
        level: list of platforms that are created at the start of the game
        character: chosen character to be created

    Attributes:
        effects: Effects class
        score: game score that increases over time
        all_sprites: group containing all sprites for easier management
        platforms: group containing platforms for collision checking
        baddies: group containing enemies for collision checking
        powerups: group containing powerups for collison checking
    """
    def __init__(self, level, character):
        self.effects = Effects()
        self.score = 1
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.baddies = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.player = Player(character)
        self.all_sprites.add(self.player)
        for platform in level:
            plat = Platform(platform[0],platform[1],platform[2],platform[3])
            self.all_sprites.add(plat)
            self.platforms.add(plat)

    def scroll(self):
        """Moves the screen diagonally and increases score"""
        self.score += 1
        self.player.pos.x -= 1
        for platform in self.platforms:
            platform.pos.x -= 1
        for powerup in self.powerups:
            powerup.pos.x -= 1
        if not self.effects.powerups["REVERSE"]:
            for baddie in self.baddies:
                baddie.pos.x -= 2
                if self.player.pos.y < baddie.pos.y:
                    baddie.pos.y -= 0.1
                if self.player.pos.y > baddie.pos.y:
                    baddie.pos.y += 0.1

    def generate(self):
        """Generates new platforms, baddies and powerups"""
        while len(self.platforms) < 7:
            pos_x = randint(WIDTH + 50,WIDTH + 300)
            pos_y = randint(50, 450)
            width = randint(80, 130)
            height = randint(20, 45)
            new_plat = Platform(pos_x, pos_y, width, height)
            self.check_overlap(new_plat, self.platforms, 150, 100)
        while len(self.baddies) < int((self.score+2200)/3000):
            pos_x = randint(WIDTH + 50,WIDTH + 500)
            pos_y = randint(-30,HEIGHT + 30)
            new_baddie = Baddie(pos_x, pos_y)
            self.check_overlap(new_baddie, self.baddies, 50, 50)
        if int(self.score%3000) == 0:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(30,HEIGHT - 30)
            powerup = Powerup(pos_x, pos_y)
            self.all_sprites.add(powerup)
            self.powerups.add(powerup)

    def check_overlap(self, new_sprite, group, x_pos, y_pos):
        """Checks if the given sprite overlaps with any in the given group.

        Args:
            new_sprite: newly created sprite to be tested
            group: group of sprites used for collision checking
            x_pos: how far the created sprites x position has to be from all platforms
            y_pos: how far the created sprites y position has to be from all platforms
        """
        for sprite in group:
            if (abs(new_sprite.pos.x - sprite.pos.x) < x_pos) \
                and (abs(new_sprite.pos.y - sprite.pos.y) < y_pos):
                new_sprite.kill()
                return
        group.add(new_sprite)
        self.all_sprites.add(new_sprite)
