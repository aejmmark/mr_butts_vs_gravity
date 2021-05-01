"""Contains classes for sprites"""
import pygame
from constants import IMG, HEIGHT, WIDTH, WHITE, BLACK, BUTTS, FROG
from movement import Movement

VEC = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """Player character sprite"""
    def __init__(self, character):
        pygame.sprite.Sprite.__init__(self)
        self.character = character
        self.image = pygame.image.load(IMG + character).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.movement = Movement(self)
        self.pos = VEC(WIDTH/2 + 10, HEIGHT/2)
        self.rect.midbottom = self.pos

    def update(self):
        self.movement.move()
        self.rect.midbottom = self.pos

    def use_ability(self, platforms):
        if self.character == BUTTS:
            self.movement.jump(platforms)
        elif self.character == FROG:
            if self.movement.ability:
                self.movement.rocket = True
                self.movement.ability = False
        else:
            if self.movement.ability:
                self.movement.reverse = not self.movement.reverse
                self.movement.ability = False

class Platform(pygame.sprite.Sprite):
    """Platforms that the player collides with"""
    def __init__(self, pos_x, pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of platform"""
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()

class Baddie(pygame.sprite.Sprite):
    """Mean enemies that attack the player"""
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/baddie.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of baddie"""
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()

class Powerup(pygame.sprite.Sprite):
    """Causes some sort of temporary effect on the game when collided with"""
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/powerup.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of powerup"""
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()
