"""Contains classes for sprites"""
import pygame
from constants import IMG, HEIGHT, WIDTH, WHITE, BLACK, BUTTS, FROG
from movement import Movement

VEC = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """Player character sprite

    Args:
        character: determines image and abilities of player sprite

    Attributes:
        character: name of character used for ability checks
        image: image of player sprite
        rect: collision box of player sprite
        movement: Movement class
        pos: position of player sprite
    """
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
        """Updates location of player sprite"""
        self.movement.move()
        self.movement.border_check()
        self.rect.midbottom = self.pos

    def use_ability(self, platforms):
        """Uses ability if ability is True and sets it to False
        chooses ability based on player character
        BUTTS jump or doublejumps
        FROG flies
        TUBRM reverses gravity

        Args:
            platforms: group of platforms used for collision checks
        """
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
    """Platforms that the player collides with

    Args:
        pos_x: x position of platform
        pos_y: y position of platform
        width: width of platform
        height: height of platform

    Attributes:
        image: image of platform
        rect: collision box of platform
        pos: position of platform
    """
    def __init__(self, pos_x, pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of platform
        Removes it when it exits view
        """
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()

class Baddie(pygame.sprite.Sprite):
    """Mean enemies that attack the player

    Args:
        pos_x: x position of enemy
        pos_y: y position of enemy

    Attributes:
        image: image of enemy
        rect: collision box of enemy
        pos: position of enemy
    """
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/baddie.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of baddie
        Removes it when it exits view
        """
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()

class Powerup(pygame.sprite.Sprite):
    """Causes some sort of temporary effect on the game when collided with

    Args:
        pos_x: x position of powerup
        pos_y: y position of powerup

    Attributes:
        image: image of powerup
        rect: collision box of powerup
        pos: position of powerup
    """
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/powerup.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.pos = VEC(pos_x,pos_y)
        self.rect.center = self.pos

    def update(self):
        """Updates location of powerup
        Removes it when it exits view
        """
        self.rect.center = self.pos
        if self.rect.right < 0:
            self.kill()
