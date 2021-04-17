"""Stage of the game"""
from random import randint
import pygame
from sprites import Player, Platform, Baddie
from constants import WIDTH, HEIGHT

class Stage:
    """Game stage"""
    def __init__(self, level):
        """Initializes sprites"""
        self.difficulty = 1
        self.timer = 0
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.baddies = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for platform in level:
            plat = Platform(platform[0],platform[1],platform[2],platform[3])
            self.all_sprites.add(plat)
            self.platforms.add(plat)

    def scroll(self):
        """Moves the screen diagonally"""
        self.player.pos.x -= 0.5
        for platform in self.platforms:
            platform.pos.x -= 0.5
        for baddie in self.baddies:
            baddie.pos.x -= 3
            if self.player.pos.y < baddie.pos.y:
                baddie.pos.y -= 0.1
            if self.player.pos.y > baddie.pos.y:
                baddie.pos.y += 0.1

    def generate(self):
        """Generates new platforms"""
        while len(self.platforms) < 8:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(100, 400)
            width = randint(80, 120)
            height = randint(20, 45)
            new_plat = Platform(pos_x, pos_y, width, height)
            for platform in self.platforms:
                if (abs(new_plat.pos.x - platform.pos.x) < 150) \
                    and (abs(new_plat.pos.y - platform.pos.y) < 100):
                    new_plat.kill()
                    break
                else:
                    self.platforms.add(new_plat)
                    self.all_sprites.add(new_plat)
                    self.timer += 1
                    if self.timer == 100:
                        self.difficulty += 1
                        self.timer = 0
        while len(self.baddies) < self.difficulty:
            pos_x = randint(WIDTH + 50,WIDTH + 200)
            pos_y = randint(-30,HEIGHT + 30)
            baddie = Baddie(pos_x, pos_y)
            self.baddies.add(baddie)
            self.all_sprites.add(baddie)
