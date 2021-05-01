"""Handles menu screens and text"""
import pygame
from constants import BLACK, WHITE, HS, IMG, BUTTS, FROG, TUBRM


class Display:
    """Handles menu screens and text"""
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Mr. Butts vs Gravity")

    def start_screen(self):
        """Start screen and character selection"""
        start_screen = True
        while start_screen:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "FAIL"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 30 < mouse_pos[0] < 150 and 200 < mouse_pos[1] < 320:
                        return "/butts.png"
                    if 200 < mouse_pos[0] < 320 and 200 < mouse_pos[1] < 320:
                        return "/frog.png"
                    if 370 < mouse_pos[0] < 490 and 200 < mouse_pos[1] < 320:
                        return "/tubrm.png"
            #
            self.display.fill(WHITE)
            self.display_text("MR. BUTTS VS GRAVITY", 50, 30, 50)
            self.display_text("CLICK CHARACTER TO START", 25, 30, 130)
            #
            butts = pygame.image.load(IMG + "/big_butts.png").convert()
            butts.set_colorkey(WHITE)
            self.display.blit(butts, (30, 200))
            self.display_text("Mr. Butts", 30, 30, 330)
            frog = pygame.image.load(IMG + "/big_frog.png").convert()
            frog.set_colorkey(WHITE)
            self.display.blit(frog, (200, 200))
            self.display_text("Frog", 30, 230, 330)
            tubrm = pygame.image.load(IMG + "/big_tubrm.png").convert()
            tubrm.set_colorkey(WHITE)
            self.display.blit(tubrm, (370, 200))
            self.display_text("St. Tubrm", 30, 360, 330)
            #
            mouse_pos = pygame.mouse.get_pos()
            if 30 < mouse_pos[0] < 150 and 200 < mouse_pos[1] < 320:
                self.display_text(BUTTS, 30, 30, 400)
            if 200 < mouse_pos[0] < 320 and 200 < mouse_pos[1] < 320:
                self.display_text(FROG, 30, 30, 400)
            if 370 < mouse_pos[0] < 490 and 200 < mouse_pos[1] < 320:
                self.display_text(TUBRM, 30, 30, 400)
            #
            pygame.display.update()

    def render(self, all_sprites, current_score, powerup, timer):
        self.display.fill(WHITE)
        all_sprites.draw(self.display)
        self.display_text(("SCORE: " + str(current_score)), 30, 10, 10)
        if timer > 0:
            self.display_text((powerup + ": " \
                + str(timer)), 30, 10, 40)
        pygame.display.update()

    def display_text(self, text, size, x_pos, y_pos):
        """Draws text to the display"""
        font = pygame.font.SysFont("arial", size)
        text_surface = font.render(text, False, BLACK)
        self.display.blit(text_surface,(x_pos,y_pos))

    def display_highscore(self, final_score, scores):
        """Draws top scores to the display"""
        if final_score > int(scores[1]):
            self.display_text("NEW HIGHSCORE!", 40, 300, 110)
        self.display_text(("SCORE: " + str(final_score)), 30, 30, 110)
        self.display_text("TOP SCORES", 30, 30, 170)
        padding = 220
        for score in scores:
            self.display_text(score, 30, 30, padding)
            padding += 30

    def get_scores(self, final_score, file):
        """Retrieves previous highscores from file and rewrites them, returns list of scores"""
        with open(file, "r") as highscore:
            highscores = highscore.read()
            scores = highscores.split(",")
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

    def game_over_screen(self, final_score):
        """Shows game over screen"""
        scores = self.get_scores(final_score, HS)
        game_over = True
        while game_over:
            self.display.fill(WHITE)
            self.display_text("WELCOME TO THE GRAVEYARD OF YOU", 35, 30, 50)
            self.display_highscore(final_score, scores)
            self.display_text("CLICK HERE TO RESTART", 30, 30, 400)
            pygame.display.update()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 30 < mouse_pos[0] < 400 and 400 < mouse_pos[1] < 430:
                        return True
        return False
