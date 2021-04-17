"""Contains classes for sprites"""
import pygame
from constants import IMG, HEIGHT, WIDTH, PLAYER_WIDTH, GRAV, ACC, FRIC, JUMP, WHITE, BLACK

VEC = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """Player character sprite"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/player.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.edges = [False] * 4
        self.pos = VEC(WIDTH/2 + 10, HEIGHT/2)
        self.vel = VEC(0,0)
        self.acc = VEC(0,0)
        self.rect.midbottom = self.pos
        self.double_jump = False
        self.left = False
        self.right = False

    def jump(self, platforms):
        """Player jumps. Usable in the air if self.double_jump is true"""
        for platform in platforms:
            self.collision(platform.rect)
            if self.edges[2]:
                self.vel.y = JUMP
                return
        if self.double_jump:
            self.vel.y = JUMP
            self.double_jump = False

    def update(self):
        """Calculates movement and updates player location accordingly"""
        self.acc = VEC(0,GRAV)
        if self.left:
            self.acc.x = -ACC
        if self.right:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH-PLAYER_WIDTH/2:
            self.pos.x = WIDTH-PLAYER_WIDTH/2
        if self.pos.x < 0+PLAYER_WIDTH/2:
            self.pos.x = 0+PLAYER_WIDTH/2
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        # limiting fallings speed to prevent clipping
        if self.vel.y > 15:
            self.vel.y = 15
        self.rect.midbottom = self.pos

    def edge_reset(self):
        """Resets the edge collision list"""
        self.edges = [False] * 4

    def collision(self, rect):
        """Checks edge collisions and adds them to self.edges"""
        self.edges[0] = rect.collidepoint(self.rect.midtop)
        self.edges[1] = rect.collidepoint(self.rect.midright)
        self.edges[2] = rect.collidepoint(self.rect.midbottom)
        self.edges[3] = rect.collidepoint(self.rect.midleft)

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
        