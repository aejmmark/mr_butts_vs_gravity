
import pygame
from constants import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Escape from Dangerland")
        self.clock = pygame.time.Clock()
        self.running = True
        self.win = False

    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.platforms = pygame.sprite.Group()
        for platform in FIRST_LEVEL:
            p = Platform(platform[0],platform[1],platform[2],platform[3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.flag = Flag(30,70)
        self.all_sprites.add(self.flag)

    def run(self, timer):
        while(self.running):
            self.events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            timer -= 1
            if timer == 0:
                self.running = False

    def new_event(self, event):
        pygame.event.post(event)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump(self.platforms)

    def update(self):
        self.all_sprites.update()
        for platform in self.platforms:
            self.player.collision(platform.rect)
            if self.player.edges[3] == True:
                self.player.pos.x = platform.rect.right + PLAYER_WIDTH/2 # seems to work
                self.player.vel.x = 0
            if self.player.edges[1] == True:
                self.player.pos.x = platform.rect.left - PLAYER_WIDTH/2 # seems to work
                self.player.vel.x = 0
            if self.player.edges[0] == True:
                self.player.pos.y = platform.rect.bottom + PLAYER_HEIGHT # seems to work
                self.player.vel.y = 0
            if self.player.edges[2] == True: # seems to work
                if self.player.vel.y > 0: 
                    self.player.pos.y = platform.rect.top
                    self.player.rect.midbottom = self.player.pos
                    self.player.vel.y = 0
        self.player.edge_reset()
        self.goal = pygame.sprite.collide_rect(self.player, self.flag)
        if self.goal:
            self.win = True
            self.running = False
               
    def render(self):
        self.display.fill(WHITE)
        self.all_sprites.draw(self.display)
        pygame.display.update()

    def victory(self):
        self.showing = True
        while self.showing:
            victory_screen = pygame.image.load(IMG + "/victory.png").convert()
            self.display.blit(victory_screen,[0,0])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.showing = False

    def quit_game(self):
        pygame.quit()
            
