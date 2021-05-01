"""All constants"""
import os

# files
SRC = os.path.dirname(__file__)
IMG = SRC.replace("/src","/img")
HS = SRC.replace("/src", "/highscore.csv")

# display
WIDTH = 800
HEIGHT = 500
FPS = 120 # 60

# player
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

# characters
BUTTS = "/butts.png"
FROG = "/frog.png"
TUBRM = "/tubrm.png"

# character bios
BUTTS_BIO = "Gravity defying hero of Buttopia"
FROG_BIO = "Slimy sidekick"
TUBRM_BIO = "Evil incarnate and archnemesis of Mr. Butts"

# physics
JUMP = -7
ACC = 0.5
FRIC = -0.15
GRAV = 0.2
MAX = 15
ROCKET = -0.1

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# stages
TEST_LEVEL = [(400,500,850,130)]
FIRST = [(0,280,80,40),(100,280,80,40),(200,280,80,40),(300,280,80,40),\
    (400,280,80,40),(500,280,80,40),(600,280,80,40),(700,280,80,40),(800,280,80,40)]
