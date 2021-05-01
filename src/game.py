"""Main module for the game"""
import pygame
from constants import WIDTH, HEIGHT, FPS, FIRST
from stage import Stage
from display import Display

class Game:
    """Contains the main parts of the game loop"""
    def __init__(self):
        pygame.init()
        self.disp = Display(WIDTH, HEIGHT)
        self.clock = pygame.time.Clock()
        self.stage = Stage(FIRST, "/butts.png")
        self.running = True
        self.playing = False
        self.scrolling = True
        self.g_o = False
        self.event_list = []

    def set_stage(self, level, character):
        """Select stage"""
        self.stage = Stage(level, character)

    def run(self, timer):
        """Runs the game loop"""
        while self.playing:
            self.events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            self.play_event()
            timer -= 1
            if timer == 0:
                self.running = False

    def add_event(self, event):
        """Add event to event_list for testing purposes"""
        self.event_list.append(event)
        # Fill list with empty events to create delays
        for x_x in range(10):
            self.event_list.append(-1)

    def play_event(self):
        """Plays an event from the event_list"""
        if len(self.event_list) > 0:
            event = self.event_list.pop(0)
            if event == -1:
                return
            pygame.event.post(event)

    def events(self):
        """Handles game events such as key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
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

    def update(self):
        """Updates the locations of sprites"""
        # disable scrolling for testing
        if self.scrolling:
            self.stage.scroll()
            self.stage.generate()
        self.stage.all_sprites.update()
        self.stage.player.platform_collision(self.stage.platforms)
        if self.stage.effects.powerups["BOINGBOING"]:
            self.stage.player.double_jump = True
        if pygame.sprite.spritecollide(self.stage.player, self.stage.powerups, True):
            self.stage.effects.random_powerup()
        if not self.stage.effects.powerups["INDESTRUCTIBILITY"]:
            if pygame.sprite.spritecollide(self.stage.player, self.stage.baddies, True):
                self.g_o = True
                self.playing = False
        self.stage.effects.countdown()

    def render(self):
        """Draws the images to the display"""
        self.disp.render(self.stage.all_sprites, self.stage.score, \
            self.stage.effects.active, self.stage.effects.timer)

    def game_over(self):
        if self.disp.game_over_screen(self.stage.score):
            self.g_o = False
        else:
            self.quit_game()

    def start(self):
        character = self.disp.start_screen()
        if character == "FAIL":
            self.quit_game()
        else:
            # set character
            self.set_stage(FIRST, character)
            self.playing = True

    def quit_game(self):
        """Shuts down the game"""
        self.running = False
        pygame.quit()
