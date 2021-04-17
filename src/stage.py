"""Stage of the game"""
import pygame
from sprites import Player, Platform, Flag

class Stage:
    """Game stage"""
    def __init__(self, level, flag):
        """Initializes sprites"""
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for platform in level:
            plat = Platform(platform[0],platform[1],platform[2],platform[3])
            self.all_sprites.add(plat)
            self.platforms.add(plat)
        self.flag = Flag(flag[0], flag[1])
        self.all_sprites.add(self.flag)

    def generate(self):
        """Randomly generates new stage"""
        pass
