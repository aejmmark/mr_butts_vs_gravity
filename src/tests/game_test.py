
import unittest
import game
import pygame

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.start()

    def test_jump(self):
        self.pos = self.game.player.pos.y
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(20)
        self.new_pos = self.game.player.pos.y
        self.game.quit_game()
        self.assertTrue(self.new_pos < self.pos)
