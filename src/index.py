"""Index"""
import game

game = game.Game()
while game.running:
    game.start()
    game.run(-1)
    if game.g_o:
        game.game_over()
game.quit_game()
