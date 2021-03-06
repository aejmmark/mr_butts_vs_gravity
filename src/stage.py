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
        defaults to FIRST
        character: chosen character to be created
        defaults to BUTTS

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
        if not self.effects.powerups["ICE AGE"]:
            for baddie in self.baddies:
                baddie.pos.x -= 2
                if self.player.pos.y < baddie.pos.y:
                    baddie.pos.y -= 0.1
                if self.player.pos.y > baddie.pos.y:
                    baddie.pos.y += 0.1
        self.generate()

    def generate(self):
        """Generates new platforms, baddies and powerups"""
        while len(self.platforms) < 7:
            _pos_x = randint(WIDTH + 50,WIDTH + 300)
            _pos_y = randint(50, 450)
            _width = randint(80, 130)
            _height = randint(20, 45)
            _new_plat = Platform(_pos_x, _pos_y, _width, _height)
            self.check_overlap(_new_plat, self.platforms, 150, 100)
        while len(self.baddies) < int((self.score+2200)/3000):
            _pos_x = randint(WIDTH + 50,WIDTH + 500)
            _pos_y = randint(-30,HEIGHT + 30)
            _new_baddie = Baddie(_pos_x, _pos_y)
            self.check_overlap(_new_baddie, self.baddies, 50, 50)
        if int(self.score%3000) == 0:
            _pos_x = randint(WIDTH + 50,WIDTH + 200)
            _pos_y = randint(30,HEIGHT - 30)
            _powerup = Powerup(_pos_x, _pos_y)
            self.all_sprites.add(_powerup)
            self.powerups.add(_powerup)

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
