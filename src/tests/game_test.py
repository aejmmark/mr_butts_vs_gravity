import unittest
import pygame
import game
from sprites import Baddie, Platform, Powerup
from constants import TEST_LEVEL, FIRST, BUTTS, FROG, TUBRM, MAX, PLAYER_WIDTH, HEIGHT, WIDTH

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
        self.assertTrue(self.game.stage.player.movement.vel.y < -1)

    def test_butts_double_jump(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(15)
        self.assertFalse(self.game.stage.player.movement.ability \
            and self.game.stage.player.movement.vel.y > 0)

    def test_frog_ability(self):
        self.game.set_stage(TEST_LEVEL, FROG)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.acc.y < 0 \
            and self.game.stage.player.movement.rocket)

    def test_frog_ability_stop(self):
        self.game.set_stage(TEST_LEVEL, FROG)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.add_event(pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE))
        self.game.run(15)
        self.assertTrue(self.game.stage.player.movement.acc.y > 0 \
            and not self.game.stage.player.movement.rocket)

    def test_tubrm_ability(self):
        self.game.set_stage(TEST_LEVEL, TUBRM)
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 440
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.acc.y < 0 \
            and self.game.stage.player.movement.reverse)

    def test_ability_wont_work_without_charging(self):
        self.game.set_stage([(100,100,100,100)], TUBRM)
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.assertFalse(self.game.stage.player.movement.ability)

    def test_left_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.acc.x < 0)

    def test_right_movement(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.acc.x > 0)

    def test_left_movement_stops(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.add_event(pygame.event.Event(pygame.KEYUP, key=pygame.K_LEFT))
        self.game.run(15)
        self.assertTrue(self.game.stage.player.movement.acc.x > -0.5)

    def test_right_movement_stops(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.add_event(pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT))
        self.game.run(15)
        self.assertTrue(self.game.stage.player.movement.acc.x < 0.5)

    def test_left_movement_platform_collision(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        plat = Platform(300,400,100,100)
        self.game.stage.platforms.add(plat)
        self.game.stage.all_sprites.add(plat)
        self.game.run(20)
        self.assertTrue(self.game.stage.player.pos.x == plat.rect.right + PLAYER_WIDTH/2)

    def test_right_movement_platform_collision(self):
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        plat = Platform(500,400,100,100)
        self.game.stage.platforms.add(plat)
        self.game.stage.all_sprites.add(plat)
        self.game.run(20)
        self.assertTrue(self.game.stage.player.pos.x == plat.rect.left - PLAYER_WIDTH/2)

    def test_fall_speed_limit(self):
        self.game.set_stage([(100,100,100,100)], BUTTS)
        self.game.stage.player.movement.vel.y = -MAX - 1
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.vel.y >= -MAX)

    def test_fall_speed_limit_in_reverse(self):
        self.game.set_stage([(100,100,100,100)], BUTTS)
        self.game.stage.player.movement.reverse = True
        self.game.stage.player.movement.vel.y = MAX + 1
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.vel.y <= MAX)

    def test_player_lands_on_platform(self):
        self.game.stage.player.pos.x = 400
        self.game.stage.player.pos.y = 400
        self.game.run(10)
        self.assertTrue(self.game.stage.player.pos.y < 440)

    def test_player_lands_on_platform_in_reverse(self):
        self.game.stage.player.movement.reverse = True
        plat = Platform(400,380,600,15)
        self.game.stage.platforms.add(plat)
        self.game.stage.all_sprites.add(plat)
        self.game.run(15)
        self.assertTrue(self.game.stage.player.movement.ability)

    def test_player_cant_exit_screen_on_left(self):
        self.game.stage.player.pos.x = -10
        self.game.run(5)
        self.assertTrue(self.game.stage.player.pos.x == 0 + PLAYER_WIDTH/2)

    def test_player_cant_exit_screen_on_right(self):
        self.game.stage.player.pos.x = WIDTH + 10
        self.game.run(5)
        self.assertTrue(self.game.stage.player.pos.x == WIDTH - PLAYER_WIDTH/2)

    def test_player_returns_from_top_when_falling(self):
        self.game.set_stage([(100,100,100,100)], BUTTS)
        self.game.stage.player.pos.y = HEIGHT + 50
        self.game.run(5)
        self.assertTrue(self.game.stage.player.pos.y < HEIGHT)

    def test_reverse_gravity_reverses_falling_loop(self):
        self.game.set_stage([(100,100,100,100)], BUTTS)
        self.game.stage.player.movement.reverse = True
        self.game.stage.player.pos.y = -50
        self.game.run(5)
        self.assertTrue(self.game.stage.player.pos.y > 0)

    def test_x_button_quits(self):
        self.game.add_event(pygame.event.Event(pygame.QUIT))
        self.game.run(5)
        self.assertFalse(self.game.running)

    def test_quit_game_stops_running(self):
        self.game.quit_game()
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

    def test_screen_edge_kills_platforms(self):
        plat = Platform(-100, -100, 10, 10)
        self.game.stage.all_sprites.add(plat)
        self.game.run(5)
        self.assertTrue(len(self.game.stage.all_sprites) == 6)

    def test_screen_edge_kills_baddie(self):
        bad = Baddie(-100, -100)
        self.game.stage.all_sprites.add(bad)
        self.game.run(5)
        self.assertTrue(len(self.game.stage.all_sprites) == 6)

    def test_screen_edge_kills_powerups(self):
        power = Powerup(-100, -100)
        self.game.stage.platforms.add(power)
        self.game.stage.all_sprites.add(power)
        self.game.run(5)
        self.assertTrue(len(self.game.stage.all_sprites) == 6)

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

    def test_powerup_boingboing(self):
        self.game.set_stage([(100,100,100,100)], TUBRM)
        self.game.stage.effects.powerups["BOINGBOING"] = True
        self.game.add_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(5)
        self.assertTrue(self.game.stage.player.movement.reverse)

    def test_powerup_indestruct(self):
        self.game.stage.effects.powerups["INDESTRUCTIBILITY"] = True
        baddie = Baddie(400, 440)
        self.game.stage.baddies.add(baddie)
        self.game.stage.all_sprites.add(baddie)
        self.game.run(5)
        self.assertFalse(self.game.g_o)

    def test_powerup_ice_age(self):
        self.game.set_stage(FIRST, BUTTS)
        self.game.scrolling = True
        self.game.stage.effects.powerups["ICE AGE"] = True
        baddie = Baddie(100, 100)
        self.game.stage.baddies.add(baddie)
        self.game.stage.all_sprites.add(baddie)
        self.game.run(5)
        self.assertTrue(baddie.pos.x == 100)
