"""Handles menu screens and text"""
import pygame
from constants import WIDTH, HEIGHT, BLACK, WHITE, HS, \
    IMG, BUTTS, FROG, TUBRM, BUTTS_BIO, FROG_BIO, TUBRM_BIO


class Display:
    """Handles menu screens and text

    Args:
        width: width of screen
        height: height of screen

    Attributes:
        display: pygame display module
    """
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mr. Butts vs Gravity")

    def start_screen(self):
        """Start screen and character selection via mouse input
        Shows character bios when hovering over images

        Returns:
            file name of selected character
        """
        start_screen = True
        while start_screen:
            self.start_screen_base()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "FAIL"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 170 < mouse_pos[0] < 290 and 200 < mouse_pos[1] < 320:
                        return BUTTS
                    if 340 < mouse_pos[0] < 460 and 200 < mouse_pos[1] < 320:
                        return FROG
                    if 500 < mouse_pos[0] < 620 and 200 < mouse_pos[1] < 320:
                        return TUBRM
            if 170 < mouse_pos[0] < 290 and 200 < mouse_pos[1] < 320:
                self.draw_text(BUTTS_BIO, 30, 200, 400)
            if 340 < mouse_pos[0] < 460 and 200 < mouse_pos[1] < 320:
                self.draw_text(FROG_BIO, 30, 320, 400)
            if 500 < mouse_pos[0] < 620 and 200 < mouse_pos[1] < 320:
                self.draw_text(TUBRM_BIO, 30, 110, 400)
            pygame.display.update()

    def start_screen_base(self):
        """Draws text and character images to the start screen"""
        self.display.fill(WHITE)
        self.draw_text("MR. BUTTS VS GRAVITY", 50, 120, 50)
        self.draw_text("CLICK CHARACTER TO START", 25, 220, 130)
        butts = pygame.image.load(IMG + "/big_butts.png").convert()
        self.display.blit(butts, (170, 200))
        self.draw_text("Mr. Butts", 30, 170, 330)
        frog = pygame.image.load(IMG + "/big_frog.png").convert()
        self.display.blit(frog, (340, 200))
        self.draw_text("Frog", 30, 370, 330)
        tubrm = pygame.image.load(IMG + "/big_tubrm.png").convert()
        self.display.blit(tubrm, (510, 200))
        self.draw_text("St. Tubrm", 30, 500, 330)

    def render(self, all_sprites, current_score, powerup, timer):
        """Draws sprites, score, and powerup timers to the display

        Args:
            all_sprites: group containing all sprites to be drawn
            current_score: current game score to be shown
            powerup: name of powerup
            timer: powerup timer
        """
        self.display.fill(WHITE)
        all_sprites.draw(self.display)
        self.draw_text(("SCORE: " + str(current_score)), 30, 10, 10)
        if timer > 0:
            self.draw_text((powerup + ": " \
                + str(timer)), 30, 10, 40)
        pygame.display.update()

    def draw_text(self, text, size, x_pos, y_pos):
        """Draws text to the display

        Args:
            text: text to be drawn
            size: size of text
            x_pos: x position of drawn text
            y_pos: y position of drawn text
        """
        font = pygame.font.SysFont("arial", size)
        text_surface = font.render(text, False, BLACK)
        self.display.blit(text_surface,(x_pos,y_pos))

    def draw_highscores(self, final_score, scores):
        """Draws top scores to the display

        Args:
            final_score: current final score
            scores: previous scores
        """
        if final_score > int(scores[1]):
            self.draw_text("NEW HIGHSCORE!", 40, 300, 110)
        self.draw_text(("SCORE: " + str(final_score)), 30, 30, 115)
        self.draw_text("TOP SCORES", 30, 30, 170)
        padding = 220
        for score in scores:
            self.draw_text(score, 30, 30, padding)
            padding += 30

    def get_scores(self, final_score, file):
        """Retrieves previous draw_ from file and rewrites them

        Args:
            final_score: current final score
            file: path of file

        Returns:
            list of scores
        """
        with open(file, "r") as highscore:
            draw_ = highscore.read()
            scores = draw_.split(",")
            scores.append(str(final_score))
            scores.append(str(0))
            if "" in scores:
                scores.remove("")
            scores.sort(key=int, reverse=True)
            scores = scores[:5]
            highscore.close()
        with open(file, "w") as highscore:
            for score in scores:
                highscore.write(score + ",")
            highscore.close()
        return scores

    def game_over_screen(self, final_score, character):
        """Shows game over screen
            Timer ensures that the game is not restarted accidentally

        Args:
            final_score: current final score
            character: current character affects text

        Returns:
            "start" if the player clicks on the screen, "quick" if space key is pressed
            or False if game is shut down
        """
        scores = self.get_scores(final_score, HS)
        game_over = True
        timer = 0
        while game_over:
            timer += 1
            self.display.fill(WHITE)
            if character == TUBRM:
                self.draw_text("EVIL VANQUISHED", 35, 30, 50)
            else:
                self.draw_text("WELCOME TO THE GRAVEYARD OF YOU", 35, 30, 50)
            self.draw_highscores(final_score, scores)
            self.draw_text("CLICK ANYWHERE TO RESTART", 30, 30, 400)
            self.draw_text("PRESS SPACE TO TRY AGAIN", 30, 30, 450)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "false"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "start"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and timer > 200:
                        return "quick"
        return False
