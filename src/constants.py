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
ACC = 1.0
FRIC = -0.2
GRAV = 0.4

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# levels
NO_FLAG = (0,0)
TEST_LEVEL = [(0,371,800,130)]
TEST_FLAG = (200,341)
FIRST_LEVEL = [(100,300,120,40),(300,300,120,40),(500,300,120,40),\
    (200,400,120,40),(400,400,120,40),(600,400,220,40),(200,200,120,40),\
        (400,200,120,40),(600,200,120,40),(0,100,220,40),(300,100,120,40),(500,100,120,40)]
FIRST_FLAG = (30,70)