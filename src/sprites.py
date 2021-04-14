
import pygame
from constants import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/player.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.edges = [False] * 4
        self.pos = vec(WIDTH-100, HEIGHT-100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.double_jump = False
        self.rect.midbottom = self.pos

    def jump(self, platforms):
        for platform in platforms:
            self.collision(platform.rect)
            if self.edges[2]:
                self.vel.y = -10
                self.edge_reset
                return
        if self.double_jump:
            self.vel.y = -10
            self.double_jump = False

    def update(self):
        self.acc = vec(0,GRAV)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if keys[pygame.K_RIGHT]:
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
        self.rect.midbottom = self.pos

    def edge_reset(self):
        edges = [False] * 4

    def collision(self, rect):
        self.edges[0] = rect.collidepoint(self.rect.midtop)
        self.edges[1] = rect.collidepoint(self.rect.midright)
        self.edges[2] = rect.collidepoint(self.rect.midbottom)
        self.edges[3] = rect.collidepoint(self.rect.midleft)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG + "/flag.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
