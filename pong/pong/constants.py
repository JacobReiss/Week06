import os
from game.elements.color import Color
from game.elements.point import Point
#----------------------------------------------
# GENERAL GAME CONSTANTS
#----------------------------------------------

# GAME
GAME_NAME = "PONG"
FRAME_RATE = 60

#SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

#FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#FONT
ASSETS_FONT = 'pong/assets/fonts'
FONT_FILE = 'pong/assets/fonts/zorque.otf'
FONT_SMALL = 32
FONT_LARGE = 48

#SOUND
ASSETS_SOUND = 'pong/assets/sounds'
BOUNCE_SOUND = 'pong/assets/sounds/game_boing.wav'
OVER_SOUND = 'pong/assets/sounds/game_points.wav'
WELCOME_SOUND = 'pong/assets/sounds/game_start.mp3'
INIT_SOUND = 'pong/assets/sounds/game_init_2.wav'

#IMAGES
ASSETS_IMAGES = 'pong/assets/images'

#TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

#COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

#KEYS
UP = "up"
DOWN = "down"
ENTER = "enter"
PAUSE = "p"

#SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

#-------------------------------------------------
# CASTING CONSTANTS
#-------------------------------------------------

#STATS
STATS_GROUP = 'stats'

#HUD 
HUD_MARGIN = 15
SCORE_GROUP = 'score'
SCORE_FORMAT = 'SCORE: {}'
SCORE_1_POSITION = Point(80, HUD_MARGIN)
SCORE_2_POSITION = Point(SCREEN_WIDTH - 100, HUD_MARGIN)

#BALL
BALL_GROUP = 'balls'
BALL_IMAGE = 'pong/assets/images/000.png'
BALL_HEIGHT = 28
BALL_WIDTH = 28
BALL_VELOCITY = 10

#RACKET
RACKET_GROUP = "rackets"
RACKET_WIDTH = 25
RACKET_HEIGHT = 200
RACKET_VELOCITY = 7
RACKET_RATE = 6
RACKET_IMAGES = [f'pong/assets/images/pong{n:03}.png' for n in range(111, 120)]

#DIALOG
DIALOG_GROUP = 'dialogs'
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WINNER_GAME = "Winner: {}"

#PLAYER
PLAYER_1_IDX = 0
PLAYER_2_IDX = 1

PLAYER_1_NAME = "PLAYER 1"
PLAYER_2_NAME = "PLAYER 2"

PLAYER_1_KEY_UP = 'w'
PLAYER_1_KEY_DOWN = 's'

PLAYER_2_KEY_UP = 'i'
PLAYER_2_KEY_DOWN = 'k'

PLAYER_DEFAULT_POINTS = 1
GAME_MAX_SCORE = 5