"""Index"""
import game

game = game.Game()
while game.running:
    game.run(-1)
    if game.win:
        game.victory()
game.quit_game()
