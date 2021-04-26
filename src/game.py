"""Main module for the game"""
import pygame
from constants import WIDTH, HEIGHT, FPS, PLAYER_WIDTH, \
    PLAYER_HEIGHT, WHITE, BLACK, FIRST, IMG, HS
from stage import Stage

class Game:
    """Contains the main parts of the game loop"""
    def __init__(self):
        pygame.init()
        pygame.font.init() # NEW
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mr. Butts vs Gravity")
        self.clock = pygame.time.Clock()
        self.stage = Stage(FIRST)
        self.running = True
        self.scrolling = True
        self.game_over = False
        self.event_list = []

    def set_stage(self, level):
        """Select stage"""
        self.stage = Stage(level)

    def run(self, timer):
        """Runs the game loop"""
        while self.running:
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
        if pygame.sprite.spritecollide(self.stage.player, self.stage.baddies, True):
            self.game_over = True
            self.running = False

    def render(self):
        """Draws the images to the display"""
        self.display.fill(WHITE)
        self.stage.all_sprites.draw(self.display)
        self.display_text(("SCORE: " + str(self.stage.score)), 30, 10, 10)
        pygame.display.update()

    def display_text(self, text, size, x_pos, y_pos):
        """Draws text to the display"""
        font = pygame.font.SysFont("arial", size)
        text_surface = font.render(text, False, BLACK)
        self.display.blit(text_surface,(x_pos,y_pos))

    def display_highscore(self, scores):
        """Draws top scores to the display"""
        if self.stage.score > int(scores[1]):
            self.display_text("NEW HIGHSCORE!", 40, 300, 110)
        self.display_text(("SCORE: " + str(self.stage.score)), 30, 30, 110)
        self.display_text("TOP SCORES", 30, 30, 170)
        padding = 220
        for score in scores:
            self.display_text(score, 30, 30, padding)
            padding += 30

    def get_scores(self):
        """Retrieves previous highscores from file and rewrites them, returns list of scores"""
        with open(HS, "r") as highscore:
            highscores = highscore.read()
            scores = highscores.split(",")
            scores.append(str(self.stage.score))
            scores.append(str(0))
            if "" in scores:
                scores.remove("")
            scores.sort(key=int, reverse=True)
            scores = scores[:5]
            highscore.close()
        with open(HS, "w") as highscore:
            for score in scores:
                highscore.write(score + ",")
            highscore.close()
        return scores

    def game_over_screen(self):
        """Shows game over screen"""
        showing = True
        scores = self.get_scores()
        while showing:
            self.display.fill(WHITE)
            self.display_text("WELCOME TO THE GRAVEYARD OF YOU", 35, 30, 50)
            self.display_highscore(scores)
            self.display_text("PRESS SPACE TO RESTART", 30, 30, 400)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    showing = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.set_stage(FIRST)
                        self.game_over = False
                        self.running = True
                        showing = False


    def quit_game(self):
        """Shuts down the game"""
        pygame.quit()
