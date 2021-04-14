
import unittest
import game
import pygame
from constants import TEST_LEVEL, TEST_FLAG, NO_FLAG

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.start(TEST_LEVEL, TEST_FLAG)
        self.game.player.pos.x = 400
        self.game.player.pos.y = 370
                
    def test_jump(self):
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(1)
        self.game.quit_game()
        self.assertTrue(self.game.player.vel.y < -7)

    def test_left_movement(self):
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(1)
        self.new_pos = self.game.player.pos.x
        self.game.quit_game()
        self.assertTrue(self.new_pos < self.pos)

    def test_right_movement(self):
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.run(1)
        self.new_pos = self.game.player.pos.x
        self.game.quit_game()
        self.assertTrue(self.new_pos > self.pos)

    def test_win_condition(self):
        self.game.player.pos.x = 231
        self.game.player.pos.y = 370
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.win)

    def test_x_button_quits(self):
        self.game.new_event(pygame.event.Event(pygame.QUIT))
        self.game.run(1)
        self.assertFalse(self.game.running)

    def test_quitting_wont_win(self):
        self.game.run(1)
        self.game.quit_game()
        self.assertFalse(self.game.win)
