"""Main module for the game"""
import pygame
from constants import BUTTS, FPS, FIRST
from stage import Stage
from display import Display

class Game:
    """Contains the main parts of the game loop

    Attributes:
        disp: Display class
        stage: Stage class
        running: is the game is running
        playing: is the gameplay loop is running
        scrolling: is the stage moving or not
        g_o: is the game over
        event_list: list of events used to automate inputs for testing
    """
    def __init__(self):
        pygame.init()
        self.disp = Display()
        self.clock = pygame.time.Clock()
        self.stage = Stage(FIRST, BUTTS)
        self.running = True
        self.playing = False
        self.scrolling = True
        self.g_o = False
        self.event_list = []

    def set_stage(self, level, character):
        """Select stage and character

        Args:
            level: list of platforms to be generated to the stage
            character: chosen player character
        """
        self.stage = Stage(level, character)

    def run(self, timer):
        """Runs the game loop. Has a timer feature for quick testing

        Args:
            timer: how many frames the loop runs
            -1 results in an infinite loop
        """
        while self.playing:
            self.events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            self.play_event()
            timer -= 1
            if timer == 0:
                self.running = False
                self.playing = False

    def add_event(self, event):
        """Add event to event_list for testing purposes
        Fills list with 10 empty events in between to create delays

        Args:
            event: event to be added
        """
        self.event_list.append(event)
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
                    if self.stage.effects.powerups["BOINGBOING"]:
                        self.stage.player.movement.ability = True
                    self.stage.player.use_ability(self.stage.platforms)
                if event.key == pygame.K_LEFT:
                    self.stage.player.movement.left = True
                if event.key == pygame.K_RIGHT:
                    self.stage.player.movement.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.stage.player.movement.rocket = False
                if event.key == pygame.K_LEFT:
                    self.stage.player.movement.left = False
                if event.key == pygame.K_RIGHT:
                    self.stage.player.movement.right = False

    def update(self):
        """Updates the status and locations of sprites while checking collision"""
        if self.scrolling:
            self.stage.scroll()
        self.stage.all_sprites.update()
        self.stage.player.movement.platform_collision(self.stage.platforms)
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
        """Shows game over screen"""
        if self.disp.game_over_screen(self.stage.score, self.stage.player.character):
            self.g_o = False
        else:
            self.quit_game()

    def start(self):
        """Shows start screen
        Begins game loop when player character is chosen
        """
        character = self.disp.start_screen()
        if character == "FAIL":
            self.quit_game()
        else:
            self.set_stage(FIRST, character)
            self.playing = True

    def quit_game(self):
        """Shuts down the game"""
        self.running = False
        pygame.quit()
