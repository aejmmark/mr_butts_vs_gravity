import unittest
import pygame
import game
from sprites import Baddie, Platform
from constants import TEST_LEVEL, FIRST, BUTTS

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.set_stage(TEST_LEVEL, BUTTS)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.scrolling = False
        self.game.playing = True

    def test_jump(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.vel.y < -1)

    def test_double_jump(self):
        self.game.stage.player.double_jump = True
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(15)
        self.game.quit_game()
        self.assertFalse(self.game.stage.player.movement.ability \
            and self.game.stage.player.movement.vel.y > 0)

    def test_left_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.vel.x < 0)

    def test_right_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.vel.x > 0)

    def test_x_button_quits(self):
        self.game.add_event(pygame.event.Event(pygame.QUIT))
        self.game.run(5)
        self.assertFalse(self.game.running)

    def test_baddies_end_game(self):
        baddie = Baddie(400, 440)
        self.game.stage.baddies.add(baddie)
        self.game.stage.all_sprites.add(baddie)
        self.game.run(5)
        self.assertTrue(self.game.g_o)

    def test_score_increases(self):
        self.game.scrolling = True
        self.game.set_stage(FIRST, BUTTS)
        self.game.run(5)
        self.assertTrue(self.game.stage.score > 0)

    def test_scrolling_moves_player(self):
        self.game.scrolling = True
        self.game.set_stage(FIRST, BUTTS)
        pos_x = self.game.stage.player.pos.x
        self.game.run(5)
        self.assertTrue(pos_x > self.game.stage.player.pos.x)

    def test_scrolling_moves_platforms(self):
        self.game.scrolling = True
        self.game.set_stage(FIRST, BUTTS)
        plat = Platform(100,100,100,100)
        self.game.stage.platforms.add(plat)
        pos_x = plat.pos.x
        self.game.run(5)
        self.assertTrue(pos_x > plat.pos.x)
