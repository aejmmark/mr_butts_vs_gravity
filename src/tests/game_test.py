import unittest
import pygame
import game
from sprites import Baddie, Platform, Powerup
from constants import TEST_LEVEL, FIRST, BUTTS, FROG, TUBRM

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.set_stage(TEST_LEVEL, BUTTS)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.scrolling = False
        self.game.playing = True

    def test_butts_jump(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.vel.y < -1)

    def test_butts_double_jump(self):
        self.game.stage.player.double_jump = True
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(15)
        self.game.quit_game()
        self.assertFalse(self.game.stage.player.movement.ability \
            and self.game.stage.player.movement.vel.y > 0)

    def test_frog_ability(self):
        self.game.set_stage(TEST_LEVEL, FROG)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.acc.y < 0 \
            and self.game.stage.player.movement.rocket)

    def test_tubrm_ability(self):
        self.game.set_stage(TEST_LEVEL, TUBRM)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.game.quit_game()
        self.assertTrue(self.game.stage.player.movement.acc.y < 0 \
            and self.game.stage.player.movement.reverse)

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

    def test_platform_generation(self):
        self.game.scrolling = True
        self.game.set_stage(TEST_LEVEL, BUTTS)
        self.game.run(5)
        self.assertTrue(len(self.game.stage.platforms) > 5)

    def test_baddie_generation(self):
        self.game.scrolling = True
        self.game.set_stage(TEST_LEVEL, BUTTS)
        self.game.stage.score += 1000
        self.game.run(5)
        self.assertTrue(len(self.game.stage.baddies) > 0)

    def test_powerup_generation(self):
        self.game.scrolling = True
        self.game.set_stage(TEST_LEVEL, BUTTS)
        self.game.stage.score += 2995
        self.game.run(5)
        self.assertTrue(len(self.game.stage.powerups) > 0)

    def test_powerup_activates_on_collision(self):
        power = Powerup(400, 440)
        self.game.stage.powerups.add(power)
        self.game.stage.all_sprites.add(power)
        self.game.run(5)
        self.assertTrue(self.game.stage.effects.active != "")

    def test_powerup_deactivates_when_timer_zero(self):
        self.game.stage.effects.random_powerup()
        self.game.stage.effects.timer = 3
        self.game.run(5)
        self.assertTrue(self.game.stage.effects.active == "")
