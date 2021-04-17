"""Main module for the game"""
import pygame
from constants import IMG, WIDTH, HEIGHT, FPS, PLAYER_WIDTH, \
    PLAYER_HEIGHT, WHITE, FIRST_LEVEL, FIRST_FLAG
from stage import Stage

class Game:
    """Contains the main parts of the game loop"""
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mr. Butts vs Gravity")
        self.clock = pygame.time.Clock()
        self.stage = Stage(FIRST_LEVEL, FIRST_FLAG)
        self.running = True
        self.win = False

    def set_stage(self, level, flag):
        """Select stage"""
        self.stage = Stage(level, flag)

    def run(self, timer):
        """Runs the game loop"""
        while self.running:
            # add event from list function
            self.events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            timer -= 1
            if timer == 0:
                self.running = False

    # testing purposes
    # something like this
    #def new_eventlist(self, list):
    #    self.eventlist = list
    #def new_event(self):
    #    if self.eventlist.notempty():
    #        event = self.eventlist.poll()
    #        pygame.event.post(event)

    def new_event(self, event):
        """Adds a new event to the event list"""
        pygame.event.post(event)

    def events(self):
        """Handles game events such as key presses and clearing stages"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.stage.player.jump(self.stage.platforms)
                if event.key == pygame.K_LEFT:
                    self.stage.player.left = True
                if event.key == pygame.K_RIGHT:
                    self.stage.player.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.stage.player.left = False
                if event.key == pygame.K_RIGHT:
                    self.stage.player.right = False
        goal = pygame.sprite.collide_rect(self.stage.player, self.stage.flag)
        if goal:
            self.win = True
            self.running = False

    def update(self):
        """Updates the locations of sprites"""
        self.stage.all_sprites.update()
        for platform in self.stage.platforms:
            self.stage.player.collision(platform.rect)
            if self.stage.player.edges[3]:
                self.stage.player.pos.x = platform.rect.right + PLAYER_WIDTH/2
                self.stage.player.vel.x = 0
            if self.stage.player.edges[1]:
                self.stage.player.pos.x = platform.rect.left - PLAYER_WIDTH/2
                self.stage.player.vel.x = 0
            if self.stage.player.edges[0]:
                self.stage.player.pos.y = platform.rect.bottom + PLAYER_HEIGHT
                self.stage.player.vel.y = 0
            if self.stage.player.edges[2]:
                if self.stage.player.vel.y > 0:
                    self.stage.player.pos.y = platform.rect.top
                    self.stage.player.rect.midbottom = self.stage.player.pos
                    self.stage.player.vel.y = 0
                    self.stage.player.double_jump = True
        self.stage.player.edge_reset()

    def render(self):
        """Draws the images on to the display"""
        self.display.fill(WHITE)
        self.stage.all_sprites.draw(self.display)
        pygame.display.update()

    def victory(self):
        """Shows victory screen"""
        showing = True
        while showing:
            victory_screen = pygame.image.load(IMG + "/victory.png").convert()
            self.display.blit(victory_screen,[0,0])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    showing = False

    def quit_game(self):
        """Shuts down the game"""
        pygame.quit()
