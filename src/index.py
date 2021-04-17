"""Index"""
import game

game = game.Game()
while game.running:
    game.run(-1)
    if game.game_over:
        game.game_over_screen()
game.quit_game()
