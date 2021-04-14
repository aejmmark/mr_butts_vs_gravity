
import game
from constants import FIRST_LEVEL, FIRST_FLAG

game = game.Game()
while game.running:
    game.start(FIRST_LEVEL, FIRST_FLAG)
    game.run(-1)
    if game.win:
        game.victory()
game.quit_game()