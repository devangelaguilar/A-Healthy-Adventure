import pygame as pg
#Opciones
TITLE = "A Healthy Adventure - Vesion: Alpha 0.6 - Milledo Dogio"

PLAYER_ACC = 0.6
PLAYER_FRICTION = -0.14
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
PLAYER_MAR_JUMP = 20
FONT_NAME = 'joystix'
HS_FILE = "highscore.txt"
FPS = 60
WIDTH = 1024
HEIGHT = 640

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (150, HEIGHT * 3 / 5,100,20),
                 (400,HEIGHT * 3 / 7,100,20)]

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_ROT_SPEED = 250
PLAYER_SPEED = 300
PLAYER_IMG = 'player.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 10, 10)
POW_SPAWN_PCT = 1

JOSEPH_SPRITESHEET = 'Joseph_Spritesheet.png'
MARIANA_SPRITESHEET = 'Mariana_Anorexia.png'
BREATH_DRUGS = 'Breath_Drugs.png'
WALK_DRUGS = 'Walk_Drugs.png'
HEART_ANIM = 'heart_anim.png'
HEART_LY_ANIM = 'heart_ly_anim.png'