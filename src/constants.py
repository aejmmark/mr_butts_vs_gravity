"""All constants"""
import os

# files
SRC = os.path.dirname(__file__)
IMG = SRC.replace("/src","/img")

# display
WIDTH = 800
HEIGHT = 500
FPS = 60

# player
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

# physics
JUMP = -10
ACC = 1.0
FRIC = -0.2
GRAV = 0.6

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# levels
TEST_LEVEL = [(400,500,850,130)]
FIRST_LEVEL = [(0,280,80,40),(100,280,80,40),(200,280,80,40),(300,280,80,40),\
    (400,280,80,40),(500,280,80,40),(600,280,80,40),(700,280,80,40),(800,280,80,40)]
