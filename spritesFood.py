import pygame as pg
import math
import colors
from settings import *
from random import choice, randrange
vec = pg.math.Vector2

class Brocoli(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Brocoli.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Cafe(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Cafe.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Camaron(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Camaron.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Pollo(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Pollo.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Chocolate(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Chocolate.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Chorizo(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Chrizo.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Cuerno(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Cuerno.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Filete(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Filete.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Papitas(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Papitas.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class HotDog(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Hot_Dog.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Huevos(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Huevos.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Paleta(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Paleta.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Palomitas(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Palomitas.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Pizza(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Pizza.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Refresco(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['minus_coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Refresco.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Ensalada(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/Food/Ensalada.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


'''class Pow_Coin_Drugs(pg.sprite.Sprite):
    def __init__(self, game, x,y):
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(['coin'])
        self.current_frame = 0
        self.last_update = 0
        #self.load_images()
        self.image = pg.image.load("img/marijuana.png").convert_alpha()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE '''


