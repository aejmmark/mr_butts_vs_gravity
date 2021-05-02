"""Handles sprite movement and collision"""
import pygame
from constants import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, ACC, JUMP, FRIC, GRAV, MAX, ROCKET

VEC = pygame.math.Vector2

class Movement:
    """Handles sprite movement and collision

    Args:
        sprite: player sprite

    Attributes:
        sprite: player sprite
        edges: list of booleans representing edges of player sprite
        [0]=top [1]=right [2]=bottom [3]=left
        vel: player velocity vector
        acc: player acceleration vector
        ability: is the player ability ready for use
        rocket: is FROGs ability in use
        reverse: is the gravity reversed
        left: is the player moving left
        right: is the player moving right
    """
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
        """Player jumps if standing on a platform
        Usable in the air if self.ability is true

        Args:
            platforms: group of platforms used to determine if the player is on a platform
        """
        for platform in platforms:
            self.collision_table(platform.rect)
            if self.edges[2]:
                self.vel.y = JUMP
                return
        if self.ability:
            self.vel.y = JUMP
            self.ability = False

    def move(self):
        """Calculates movement and moves player location accordingly"""
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
        if self.vel.y > MAX:
            self.vel.y = MAX
        if self.vel.y < -MAX:
            self.vel.y = -MAX
        self.sprite.pos += self.vel + 0.5 * self.acc

    def border_check(self):
        """Prevents running out of the screen from the sides and
        returns the player back to the top when falling out
        """
        if self.sprite.pos.x > WIDTH-PLAYER_WIDTH/2:
            self.sprite.pos.x = WIDTH-PLAYER_WIDTH/2
        if self.sprite.pos.x < 0+PLAYER_WIDTH/2:
            self.sprite.pos.x = 0+PLAYER_WIDTH/2
        if self.reverse:
            if self.sprite.pos.y < 0:
                self.sprite.pos.y = HEIGHT + PLAYER_HEIGHT
        else:
            if self.sprite.pos.y < PLAYER_HEIGHT:
                self.rocket = False
            if self.sprite.pos.y > HEIGHT + PLAYER_HEIGHT:
                self.sprite.pos.y = 0

    def platform_collision(self, platforms):
        """Check collision with platforms
        Adjusts player position and velocity to simulate collision

        Args:
            platforms: group of platforms for collision checks
        """
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
        """Checks edge collisions and adds them to self.edges

        Args:
            rect: collision box of platform used to check collision
        """
        self.edges[0] = rect.collidepoint(self.sprite.rect.midtop)
        self.edges[1] = rect.collidepoint(self.sprite.rect.midright)
        self.edges[2] = rect.collidepoint(self.sprite.rect.midbottom)
        self.edges[3] = rect.collidepoint(self.sprite.rect.midleft)

    def edge_reset(self):
        """Resets the edge collision list"""
        self.edges = [False] * 4
