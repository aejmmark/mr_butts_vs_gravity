"""Handles sprite movement and collision"""
import pygame
from constants import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, ACC, JUMP, FRIC, GRAV, MAX, ROCKET

VEC = pygame.math.Vector2

class Movement:
    """Handles sprite movement and collision"""
    def __init__(self, sprite):
        self.sprite = sprite
        self.edges = [False] * 4
        self.vel = VEC(0,0)
        self.acc = VEC(0,0)
        self.ability = False
        self.rocket = False
        self.reverse = False
        self.left = False
        self.right = False

    def jump(self, platforms):
        """Player jumps. Usable in the air if self.ability is true"""
        for platform in platforms:
            self.collision_table(platform.rect)
            if self.edges[2]:
                self.vel.y = JUMP
                return
        if self.ability:
            self.vel.y = JUMP
            self.ability = False

    def move(self):
        """Calculates movement and updates player location accordingly"""
        if self.reverse:
            self.acc = VEC(0,-GRAV)
        elif self.rocket:
            self.acc = VEC(0,ROCKET)
        else:
            self.acc = VEC(0,GRAV)
        if self.left:
            self.acc.x = -ACC
        if self.right:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.sprite.pos += self.vel + 0.5 * self.acc
        if self.sprite.pos.x > WIDTH-PLAYER_WIDTH/2:
            self.sprite.pos.x = WIDTH-PLAYER_WIDTH/2
        if self.sprite.pos.x < 0+PLAYER_WIDTH/2:
            self.sprite.pos.x = 0+PLAYER_WIDTH/2
        if self.sprite.pos.y > HEIGHT:
            self.sprite.pos.y = 0
        if self.sprite.pos.y < 0:
            self.sprite.pos.y = HEIGHT
        if self.vel.y > MAX:
            self.vel.y = MAX
        if self.vel.y < -MAX:
            self.vel.y = -MAX

    def platform_collision(self, platforms):
        """Check collision with platforms using collision_table()" \
            "and adjusts player position accordingly"""
        for platform in platforms:
            self.collision_table(platform.rect)
            if self.edges[3]:
                self.sprite.pos.x = platform.rect.right + PLAYER_WIDTH/2
                self.vel.x = 0
            if self.edges[1]:
                self.sprite.pos.x = platform.rect.left - PLAYER_WIDTH/2
                self.vel.x = 0
            if self.edges[0]:
                self.sprite.pos.y = platform.rect.bottom + PLAYER_HEIGHT
                self.vel.y = 0
                if self.reverse:
                    self.ability = True
            if self.edges[2]:
                if self.vel.y > 0:
                    self.sprite.pos.y = platform.rect.top
                    self.vel.y = 0
                    if not self.reverse:
                        self.ability = True
        self.edge_reset()

    def collision_table(self, rect):
        """Checks edge collisions and adds them to self.edges"""
        self.edges[0] = rect.collidepoint(self.sprite.rect.midtop)
        self.edges[1] = rect.collidepoint(self.sprite.rect.midright)
        self.edges[2] = rect.collidepoint(self.sprite.rect.midbottom)
        self.edges[3] = rect.collidepoint(self.sprite.rect.midleft)

    def edge_reset(self):
        """Resets the edge collision list"""
        self.edges = [False] * 4
