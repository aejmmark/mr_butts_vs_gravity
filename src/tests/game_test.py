import unittest
import pygame
import game
from constants import TEST_LEVEL

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.set_stage(TEST_LEVEL)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.scrolling = False
                
    def test_jump(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.vel.y < -1)

    def test_double_jump(self):
        self.game.stage.player.double_jump = True
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(15)
        self.game.quit_game()
        self.assertFalse(self.game.stage.player.double_jump and self.game.stage.player.vel.y > 0)

    def test_left_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.vel.x < 0)

    def test_right_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.vel.x > 0)

    def test_x_button_quits(self):
        self.game.add_event(pygame.event.Event(pygame.QUIT))
        self.game.run(5)
        self.assertFalse(self.game.running)
