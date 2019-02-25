import pygame as pg
# Opciones
TITLE = "A Healthy Adventure"

PLAYER_ACC = 0.9
ENEMY_ACC = 0.6
PLAYER_FRICTION = -0.14
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
PLAYER_MAR_JUMP = 20
FONT_NAME = 'Roboto Lt'
HS_FILE = "highscore.txt"
FPS = 60
WIDTH = 1024
HEIGHT = 640

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_ROT_SPEED = 250
PLAYER_SPEED = 300
PLAYER_HIT_RECT = pg.Rect(0, 0, 10, 10)
POW_SPAWN_PCT = 1

JOSEPH_SPRITESHEET = 'Joseph_Spritesheet.png'
JOSEPH_SPRITESHEET_75 = 'Sad Boy 75%.png'
JOSEPH_SPRITESHEET_50 = 'Sad Boy 50%.png'
MINION_DEPRESSION_SPRITESHEET = 'Enemies/Minion - Spritesheet.png'
MARIANA_SPRITESHEET = 'Mariana_Anorexia.png'
JUAN_SPRITESHEET = 'final_deportista_obesidad.png'
MACHO_SPRITESHEET = 'El_Macho.png'
BREATH_DRUGS = 'Breath_Drugs.png'
WALK_DRUGS = 'Walk_Drugs.png'
HEART_ANIM = 'heart_anim.png'
HEART_LY_ANIM = 'heart_ly_anim.png'