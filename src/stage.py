"""Stage of the game"""
from random import randint
import pygame
from effects import Effects
from sprites import Player, Platform, Baddie, Powerup
from constants import WIDTH, HEIGHT

class Stage:
    """Game stage"""
    def __init__(self, level):
        """Initializes sprites"""
        self.effects = Effects()
        self.difficulty = 1
        self.timer = 1
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.baddies = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for platform in level:
            plat = Platform(platform[0],platform[1],platform[2],platform[3])
            self.all_sprites.add(plat)
            self.platforms.add(plat)

    def scroll(self):
        """Moves the screen diagonally"""
        self.player.pos.x -= 1
        for platform in self.platforms:
            platform.pos.x -= 1
        for powerup in self.powerups:
            powerup.pos.x -= 1
        if not self.effects.powerups["REVERSE"]:
            for baddie in self.baddies:
                baddie.pos.x -= 2.5
                if self.player.pos.y < baddie.pos.y:
                    baddie.pos.y -= 0.2
                if self.player.pos.y > baddie.pos.y:
                    baddie.pos.y += 0.2
        self.timer += 1
        self.score += 1
        if self.timer == 3000:
            self.difficulty += 1
            self.timer = 0

    def generate(self):
        """Generates new platforms"""
        while len(self.platforms) < 8:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(50, 450)
            width = randint(80, 120)
            height = randint(20, 45)
            new_plat = Platform(pos_x, pos_y, width, height)
            self.check_overlap(new_plat, self.platforms, 150, 100)
        while len(self.baddies) < self.difficulty:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(-30,HEIGHT + 30)
            new_baddie = Baddie(pos_x, pos_y)
            self.check_overlap(new_baddie, self.baddies, 50, 50)
        if self.timer == 0:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(30,HEIGHT - 30)
            powerup = Powerup(pos_x, pos_y)
            self.all_sprites.add(powerup)
            self.powerups.add(powerup)

    def check_overlap(self, new_sprite, group, x_pos, y_pos):
        """Checks if the given sprite overlaps with any in the given group.
        Uses the given measurements"""
        for sprite in group:
            if (abs(new_sprite.pos.x - sprite.pos.x) < x_pos) \
                and (abs(new_sprite.pos.y - sprite.pos.y) < y_pos):
                new_sprite.kill()
                return
        group.add(new_sprite)
        self.all_sprites.add(new_sprite)
