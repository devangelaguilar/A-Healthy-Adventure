#!/usr/bin/env python
import pygame as pg
from spritesFood import Papitas
from spritesFood import Pizza
from spritesFood import Ensalada
from spritesFood import Filete
from spritesFood import Chocolate
from spritesFood import Brocoli
from spritesFood import Pollo
import os
from pygame.locals import *
from settings import *
from sprites import *
import colors
import spritesFood
from random import randrange
import datetime

opciones_espanol = ['Jugar',
                    'Opciones',
                    'Acerca de',
                    'Salir']
                    

opciones_ingles = ['Play',
                    'Options',
                    'About',
                    'Exit']

niveles = ['Depresion',
            'Drogas',
            'Desordenes Alimenticios',
            'Obesidad',
            'ETS',
            'Regresar al menu principal']


niveles_ingles = ['Depression',
            'Drugs',
            'Food Disorders',
            'Obesity',
            'STD',
            'Back To Menu']

pause = False
idioma = 0

class Opcion:

    def __init__(self, fuente,text_color,titulo, x, y, igualdad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, text_color)
        self.imagen_destacada = fuente.render(titulo, 1, text_color)
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * igualdad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = WIDTH / 5 * 2
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pg.image.load('img/Items/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

class Menu:
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    def __init__(self, opciones,text_color):
        self.opciones = []
        pg.display.set_caption(TITLE)
        fuente = pg.font.Font('Joystix.ttf', 25)
        x = WIDTH / 5 * 2
        y = HEIGHT / 2
        igualdad= 1

        self.cursor = Cursor(x - 40, y, 55)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente,text_color,titulo, x, y, igualdad, funcion))
            y += 55
            if igualdad == 1:
                igualdad = -1
            else:
                igualdad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pg.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funcion asociada a la opcion
                self.opciones[self.seleccionado].activar()

        # procura que el cursor est entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opcion del menu."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)



class Menu_Niveles:
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    def __init__(self, opciones,text_color):
        self.opciones = []
        pg.display.set_caption(TITLE)
        fuente = pg.font.Font('Joystix.ttf', 20)
        x = WIDTH / 5 * 2
        y = HEIGHT / 12 * 4
        igualdad= 1

        self.cursor = Cursor(x - 30, y, 50)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente,text_color,titulo, x, y, igualdad, funcion))
            y += 50
            if igualdad == 1:
                igualdad = -1
            else:
                igualdad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pg.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funcion asociada a la opciin.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor este entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opcion del menu."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)


class Depression_Level:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.lm = pg.image.load("img/Items/heart_ly.png").convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder,'img/Depression')
        self.img_items = os.path.join(self.game_folder,'img/Items')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(self.game_folder,'maps/Depression - map_1.txt'))
        self.spritesheet = Spritesheet(os.path.join(self.img_folder,JOSEPH_SPRITESHEET))
        self.spritesheet_minion = Spritesheet(os.path.join(self.img_folder,MINION_DEPRESSION_SPRITESHEET))
        
        self.energy_ball = pg.image.load("img/Items/Energy_Ball.png").convert_alpha()
        self.energy = self.energy_ball.get_rect()
        
        self.heart_anim = Spritesheet(os.path.join(self.img_items,HEART_ANIM))
        self.heart_ly_anim = Spritesheet(os.path.join(self.img_items,HEART_LY_ANIM))
        self.background = pg.image.load("img/Depression/Scenario.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd/')
    

    def new_game(self):
        #New game.
        self.score = 0
        self.lifes = 3
        self.volumen = 1
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.proyectiles = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self,col,row)
                if tile == '1':
                    Floor_Depression(self, col, row)
                if tile == '2':
                    Floor_Depression_1(self, col, row)
                if tile == '6':
                    Floor_Depression_2(self,col,row)
                if tile == '3':
                    Pow_Life(self,col,row)
                if tile == '4':
                    Minus_Life(self,col,row)
                if tile == '5':
                    Pow_Coin(self,col,row)
                if tile == 'P':
                    self.player = Joseph(self, col, row)
                if tile == 'D':
                    Door(self,col,row)
                if tile == 'M':
                    self.minion = Minion_Depression(self,col,row)
        pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        pg.mixer.music.set_volume(self.volumen)
        self.camera = Camara(self.map.width,self.map.height)
        self.show_start_screen()


    def run(self):
        #Loop Principal.
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(1500)

    def update(self):
        #Update para el loop.
        self.screen.fill(colors.WHITE)
        self.screen.blit(self.background, (0,0))
        self.all_sprites.update()
        self.powerups.update()
        self.enemies.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

            hit_enemy = pg.sprite.spritecollide(self.player,self.enemies,True)
            if hit_enemy:
                self.lifes -= 1
                self.player.jump()
                print(self.lifes)
                self.update_lifes()

        if self.minion.vel.y > 0:
            hits_minion = pg.sprite.spritecollide(self.minion, self.walls, False)
            if hits_minion:
                self.minion.pos.y = hits_minion[0].rect.top + 1
                self.minion.vel.y = 0

        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)

            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False
            elif pow.type == 'life':
                self.lifes += 1
                self.update_lifes()
            elif pow.type == 'minus_life':
                self.lifes -= 1
                self.update_lifes()
            elif pow.type == 'door':
                self.endlevel()
        self.camera.update(self.player)

    def events(self):
        #Eventos del loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    global pause
                    pause = True
                    self.pause()


    def draw(self):
        #Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.lm,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        if idioma == 0:
            self.draw_text('Joystix.ttf', 'Depresion: 100%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('Joystix.ttf', 'Depresion - Nivel 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        else:
            self.draw_text('Joystix.ttf', 'Depression: 100%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('Joystix.ttf', 'Depression - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        pg.display.flip()

    def update_lifes(self):
        if self.lifes == 0:
            self.quitgame()
        if self.lifes == 1:
            self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/no_heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 2:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 3:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()

    def load_arrays(self):
        pass

    def show_start_screen(self):
        screen_load = True
        if idioma == 0:
            self.load_screen_1 = pg.image.load("img/No_tocar/depression_load_screen_level_1.png").convert_alpha()
        else:
            self.load_screen_1 = pg.image.load("img/No_tocar/depression_load_screen_level_1_english.png").convert_alpha()
        while screen_load:
            self.screen.blit(self.load_screen_1,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    os.sys.exit()
            pg.display.update()
            pg.time.delay(3000)
            self.run()


    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass
    

    def pause(self):
        pg.mixer.music.stop()
        reloj = pg.time.Clock()
        if idioma == 0:
            self.load_screen = pg.image.load("img/No_tocar/depression_pause_menu.png").convert_alpha()
        else:
            self.load_screen = pg.image.load("img/Pantallas/depression_pause_menu_english.png").convert_alpha()
        while pause:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        self.unpased()
                    if event.key == pg.K_s:
                        select_level()
                    if event.key == pg.K_q:
                        self.quitgame()
            pg.display.update()
            reloj.tick(FPS)
    
    def unpased(self):
        pg.mixer.music.play()
        global pause
        pause = False

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def quitgame(self):
        pg.quit()
        quit()

    def endlevel(self):
        pg.mixer.music.stop()
        screen_load = True
        self.load_screen = pg.image.load("img/No_tocar/depresion_completado1.png")
        while screen_load:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        d_l_2 = Depression_Level_2()
                        d_l_2.show_start_screen()
                        
                        while d_l_2.running:

                            d_l_2.new_game()
                            d_l_2.show_go_screen()

                        pg.quit()
            pg.display.update()

class Depression_Level_2:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.lm = pg.image.load("img/Items/heart_ly.png").convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,'img/Depression')
        img_items = os.path.join(game_folder,'img/Items')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(game_folder,'maps/Depression - map_2.txt'))
        self.spritesheet = Spritesheet(os.path.join(img_folder,JOSEPH_SPRITESHEET_50))
        self.heart_anim = Spritesheet(os.path.join(img_items,HEART_ANIM))
        self.heart_ly_anim = Spritesheet(os.path.join(img_items,HEART_LY_ANIM))
        self.background = pg.image.load("img/Depression/Scenario.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd')
    

    def new_game(self):
        #New game.
        self.score = 00
        self.lifes = 3
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self,col,row)
                if tile == '1':
                    Floor_Depression(self, col, row)
                if tile == '2':
                    Floor_Depression_1(self, col, row)
                if tile == '6':
                    Floor_Depression_2(self,col,row)
                if tile == '3':
                    Pow_Life(self,col,row)
                if tile == '4':
                    Minus_Life(self,col,row)
                if tile == '5':
                    Pow_Coin(self,col,row)
                if tile == 'P':
                    self.player = Joseph(self, col, row)
                if tile == 'D':
                    Door(self,col,row)
        pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        pg.mixer.music.set_volume(1);
        self.camera = Camara(self.map.width,self.map.height)
        self.run_depression()


    def run_depression(self):
        #Loop Principal.
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events_depression()
            self.draw_depression()
            self.update_depression()
        pg.mixer.music.fadeout(500)

    def update_depression(self):
        #Update para el loop.
        self.screen.fill(colors.WHITE)
        self.screen.blit(self.background, (0,0))
        self.all_sprites.update()
        self.powerups.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False
            elif pow.type == 'life':
                self.lifes += 0.5
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'minus_life':
                self.lifes -= 0.5
                if self.lifes == 0:
                    self.heart = pg.image.load("img/Items/no_heart.png")
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'door':
                self.endlevel()
        self.camera.update(self.player)

    def events_depression(self):
        #Eventos del loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_p:
                    global pause
                    pause = True
                    self.pause()

    def draw_depression(self):
        #Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.lm,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        if idioma == 0:
            self.draw_text('Joystix.ttf', 'Depresion: 50%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('Joystix.ttf', 'Depresion - Nivel 2', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        else:
            self.draw_text('Joystix.ttf', 'Depression: 50%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('Joystix.ttf', 'Depression - Level 2', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        pg.display.flip()

    def update_lifes(self):
        if self.lifes == 0:
            self.quitgame()
        if self.lifes == 1:
            self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/no_heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 2:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/no_heart.png").convert_alpha()
        if self.lifes == 3:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()

    def pause(self):
        pg.mixer.music.stop()
        reloj = pg.time.Clock()
        if idioma == 0:
            self.load_screen = pg.image.load("img/No_Tocar/depression_pause_menu.png").convert_alpha()
        else:
            self.load_screen = pg.image.load("img/No_tocar/depression_pause_menu_english.png").convert_alpha()
        while pause:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        self.unpased()
                    if event.key == pg.K_s:
                        select_level()
                    if event.key == pg.K_q:
                        self.quitgame()
            pg.display.update()
            reloj.tick(FPS)
    
    def unpased(self):
        pg.mixer.music.play()
        global pause
        pause = False

    def load_arrays(self):
        pass

    def show_start_screen(self):
        pass


    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def quitgame(self):
        pg.quit()
        quit()

    def endlevel(self):
        pg.mixer.music.stop()
        screen_load = True
        self.load_screen = pg.image.load("img/No_tocar/depresion_completado2.png")
        while screen_load:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        select_level()
            pg.display.update()

class Drugs_level:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        pg.display.set_caption(TITLE)
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.img_score = pg.image.load("img/Items/diamante.png").convert_alpha()
        self.power_bar = pg.image.load('img/Items/bar.png').convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        self.dir = os.path.dirname(__file__)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,'img/Drugs')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(game_folder,'maps/Drugs - map_1.txt'))
        #self.heart_anim = Spritesheet(os.path.join(img_folder,HEART_ANIM))
        #self.heart_ly_anim = Spritesheet(os.path.join(img_folder,HEART_LY_ANIM))
        self.breath_player = Spritesheet(os.path.join(img_folder,BREATH_DRUGS))
        self.walk_player = Spritesheet(os.path.join(img_folder,WALK_DRUGS))
        self.snd_dir = os.path.join(self.dir, 'snd')
        self.background = pg.image.load("img/Drugs/Fondo Drogas.png").convert_alpha()
    

    def new(self):
        #New game.
        self.score = 00
        self.lifes = 3
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Floor_Drugs(self, col, row)
                if tile == '2':
                    Floor(self, col, row)
                if tile == '3':
                    Pow_Life(self,col,row)
                if tile == '4':
                    Minus_Life(self,col,row)
                if tile == '5':
                    Pow_Coin_Drugs(self,col,row)
                if tile == 'P':
                    self.player = Jon_Snow(self, col, row)
                if tile == 'D':
                    Door(self,col,row)
        #pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        #pg.mixer.music.set_volume(1);
        self.camera = Camara(self.map.width,self.map.height)
        self.show_start_screen()


    def run(self):
        #Loop Principal.
        #pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        #pg.mixer.music.fadeout(500)

    def update(self):
        #Update para el loop.
        self.all_sprites.update()
        self.powerups.update()

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False
            elif pow.type == 'life':
                self.lifes += 1
                self.update_lifes()
            elif pow.type == 'minus_life':
                self.lifes -= 1
                self.update_lifes()
            elif pow.type == 'door':
                self.endlevel()
        self.camera.update(self.player)

    def events(self):
        #Eventos del loop.
         for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    global pause
                    pause = True
                    self.pause()

    def update_lifes(self):
        if self.lifes == 0:
            self.quitgame()
        if self.lifes == 1:
            self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/no_heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 2:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 3:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()


    def draw(self):
        #Dibujar pantalla durante el loop.
        self.screen.fill(colors.WHITE)
        self.screen.blit(self.background,(0,0))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.img_score,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        if idioma == 0:
            self.draw_text('Joystix.ttf', 'Drogas - Nivel 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        else:
            self.draw_text('Joystix.ttf', 'Drugs - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        self.screen.blit(self.power_bar,(WIDTH / 32 * 12, 16))
        pg.display.flip()

    def animate_text_ly(self):
        pass

    def load_arrays(self):
        pass

    def show_start_screen(self):
        screen_load = True
        if idioma == 0:
            self.load_screen_1 = pg.image.load("img/No_tocar/drogas_load_screen_level_1.png").convert_alpha()
        else:
            self.load_screen_1 = pg.image.load("img/No_tocar/drogas_load_screen_level_1.png").convert_alpha()
        while screen_load:
            self.screen.blit(self.load_screen_1,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    os.sys.exit()
            pg.display.update()
            pg.time.delay(3000)
            self.run()

    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass
    
    def quitgame(self):
        pg.display.quit()
        os.sys.exit()

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def pause(self):
        pg.mixer.music.stop()
        reloj = pg.time.Clock()
        if idioma == 0:
            self.load_screen = pg.image.load("img/No_tocar/drogas_pause_menu.png").convert_alpha()
        else:
            self.load_screen = pg.image.load("img/No_tocar/drogas_pause_menu_english.png").convert_alpha()
        while pause:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        self.unpased()
                    if event.key == pg.K_s:
                        select_level()
                    if event.key == pg.K_q:
                        self.quitgame()
            pg.display.update()
            reloj.tick(FPS)
    
    def unpased(self):
        pg.mixer.music.play()
        global pause
        pause = False
    
    def endlevel(self):
        screen_load = True
        self.load_screen = pg.image.load("img/No_tocar/drogas_completado1.png").convert_alpha()
        while screen_load:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                       select_level()
            pg.display.update()

class Anorexia_Level:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.lm = pg.image.load("img/Items/heart_ly.png").convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,'img/Anorexia')
        img_items = os.path.join(game_folder,'img/Items')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(game_folder,'maps/Anorexia - map_1.txt'))
        self.spritesheet_mariana = Spritesheet(os.path.join(img_folder,MARIANA_SPRITESHEET))
        self.heart_anim = Spritesheet(os.path.join(img_items,HEART_ANIM))
        self.heart_ly_anim = Spritesheet(os.path.join(img_items,HEART_LY_ANIM))
        self.background = pg.image.load("img/Anorexia/Fondo Anorexia.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd')
    

    def new_game(self):
        #New game.
        self.score = 0
        self.lifes = 3
        self.level_Name = "Level 1 - Anorexia"
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self,col,row)
                if tile == '1':
                    Floor_Drugs(self, col, row)

                #Sprites de comida
                if tile == '3':
                    Pollo(self, col, row)
                if tile == '4':
                    Brocoli(self, col, row)
                if tile =='5':
                    Chocolate(self, col, row)
                if tile == '6':
                    Filete(self, col, row)
                if tile == '7':
                    Ensalada(self, col, row)
                if tile == '8':
                    Pizza(self, col, row)
                if tile == '9':
                    Papitas(self, col, row)
                if tile == 'P':
                    self.player = Mariana(self, col, row)
                if tile == 'D':
                    Door(self,col,row)

        pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        pg.mixer.music.set_volume(1);
        self.camera = Camara(self.map.width,self.map.height)
        self.run()


    def run(self):
        #Loop Principal.
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.screen.fill(colors.WHITE)
            self.screen.blit(self.background, (0,0))
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
        pg.mixer.music.fadeout(500)

    def update(self):
        #Update para el loop.
        self.all_sprites.update()
        self.powerups.update()

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False

            elif pow.type =='minus_coin':
                self.score -=5
                self.player.jumping = False

            elif pow.type == 'life':
                self.lifes += 1
                self.update_lifes()

            elif pow.type == 'minus_life':
                self.lifes -= 1
                self.update_lifes()

            elif pow.type == 'door':
                self.endlevel()
        self.camera.update(self.player)

    def events(self):
        #Eventos del loop.
         for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    global pause
                    pause = True
                    self.pause()

    def draw(self):
        #Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.lm,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        if idioma == 0:
            self.draw_text('Joystix.ttf', 'Anorexia - Area 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        else:
            self.draw_text('Joystix.ttf', 'Anorexia - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        pg.display.flip()

    def update_lifes(self):
        if self.lifes == 0:
            self.quitgame()
        if self.lifes == 1:
            self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/no_heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 2:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/no_heart.png").convert_alpha()
        if self.lifes == 3:
            self.heart_1 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()


    def animate_text_ly(self):
        pass

    def load_arrays(self):
        pass

    def show_start_screen(self):
        pass


    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass

    def pause(self):
        pg.mixer.music.stop()
        reloj = pg.time.Clock()
        if idioma == 0:
            self.load_screen = pg.image.load("img/No_tocar/drogas_pause_menu.png").convert_alpha()
        else:
            self.load_screen = pg.image.load("img/No_tocar/drogas_pause_menu_english.png").convert_alpha()
        while pause:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        self.unpased()
                    if event.key == pg.K_s:
                        select_level()
                    if event.key == pg.K_q:
                        self.quitgame()
            pg.display.update()
            reloj.tick(FPS)
    
    def unpased(self):
        pg.mixer.music.play()
        global pause
        pause = False
    
    def endlevel(self):
        screen_load = True
        self.load_screen = pg.image.load("img/No_tocar/anorexia_completado1.png").convert_alpha()
        while screen_load:
            self.screen.blit(self.load_screen,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                       select_level()
            pg.display.update()

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def quitgame(self):
        pg.quit()
        quit()

class Obesidad_Level:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.lm = pg.image.load("img/Items/heart_ly.png").convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,'img')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(game_folder,'maps/Obesidad - map_1.txt'))
        self.spritesheet_don_juan = Spritesheet(os.path.join(img_folder,JUAN_SPRITESHEET))
        #self.heart_anim = Spritesheet(os.path.join(img_folder,HEART_ANIM))
        #self.heart_ly_anim = Spritesheet(os.path.join(img_folder,HEART_LY_ANIM))
        self.background = pg.image.load("img/Obesidad/Fondo_Obesidad.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd')
    

    def new_game(self):
        #New game.
        self.score = 00
        self.lifes = 3
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self,col,row)
                if tile == '1':
                    Floor_Drugs(self, col, row)
                if tile == '2':
                    Floor_Depression_1(self, col, row)
                if tile == '6':
                    Floor_Depression_2(self,col,row)
                if tile == '3':
                    Pow_Life(self,col,row)
                if tile == '4':
                    Minus_Life(self,col,row)
                #if tile == '5':
                    #Pow_Coin(self,col,row)
                if tile == 'P':
                    self.player = Don_Juan(self, col, row)
                if tile == 'D':
                    Door(self,col,row)
        pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        pg.mixer.music.set_volume(1);
        self.camera = Camara(self.map.width,self.map.height)
        self.run()


    def run(self):
        #Loop Principal.
        #pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.screen.fill(colors.WHITE)
            self.screen.blit(self.background, (0,0))
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
        #pg.mixer.music.fadeout(500)

    def update(self):
        #Update para el loop.
        self.all_sprites.update()
        self.powerups.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False
            elif pow.type == 'life':
                self.lifes += 0.5
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'minus_life':
                self.lifes -= 0.5
                if self.lifes == 0:
                    self.heart = pg.image.load("img/Items/no_heart.png")
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'door':
                self.quitgame()
        self.animate_text_ly()
        self.camera.update(self.player)

    def events(self):
        #Eventos del loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   self.quitgame()

    def draw(self):
        #Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.lm,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        self.draw_text('Joystix.ttf', 'Obesidad - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        pg.display.flip()

    def animate_text_ly(self):
        pass

    def load_arrays(self):
        pass

    def show_start_screen(self):
        pass


    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def quitgame(self):
        pg.quit()
        quit()

class ETS_Level:
    def __init__(self):
        #Inicia el juego, ventana, etc.
        pg.init()
        pg.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        fuente = pg.font.Font('Joystix.ttf', 20)
        pg.key.set_repeat(1, 10)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        self.heart = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_2 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.heart_3 = pg.image.load("img/Items/heart.png").convert_alpha()
        self.lm = pg.image.load("img/Items/heart_ly.png").convert_alpha()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,'img')
        with open(os.path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(game_folder,'maps/ETS - map_1.txt'))
        self.spritesheet_macho = Spritesheet(os.path.join(img_folder,MACHO_SPRITESHEET))
        #self.heart_anim = Spritesheet(os.path.join(img_folder,HEART_ANIM))
        #self.heart_ly_anim = Spritesheet(os.path.join(img_folder,HEART_LY_ANIM))
        self.background = pg.image.load("img/ETS/Fondo_ETS.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd')
    

    def new_game(self):
        #New game.
        self.score = 00
        self.lifes = 3
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.current_frame = 0
        self.last_update = 0
        self.load_arrays()
        #self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self,col,row)
                if tile == '1':
                    Floor_Drugs(self, col, row)
                if tile == '2':
                    Floor_Depression_1(self, col, row)
                if tile == '6':
                    Floor_Depression_2(self,col,row)
                if tile == '3':
                    Pow_Life(self,col,row)
                if tile == '4':
                    Minus_Life(self,col,row)
                #if tile == '5':
                    #Pow_Coin(self,col,row)
                if tile == 'P':
                    self.player = El_Macho(self, col, row)
                if tile == 'D':
                    Door(self,col,row)
        pg.mixer.music.load(os.path.join(self.snd_dir, 'The Truth Untold (feat. Steve Aoki).mp3'))
        pg.mixer.music.set_volume(1);
        self.camera = Camara(self.map.width,self.map.height)
        self.run()


    def run(self):
        #Loop Principal.
        #pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.screen.fill(colors.WHITE)
            self.screen.blit(self.background, (0,0))
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
        #pg.mixer.music.fadeout(500)

    def update(self):
        #Update para el loop.
        self.all_sprites.update()
        self.powerups.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            
        for pow in pow_hits:
            if pow.type == 'coin':
                self.score += 10
                self.player.jumping = False
            elif pow.type == 'life':
                self.lifes += 0.5
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'minus_life':
                self.lifes -= 0.5
                if self.lifes == 0:
                    self.heart = pg.image.load("img/Items/no_heart.png")
                if self.lifes == 0.5:
                    self.heart = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 1:
                    self.heart = pg.image.load("img/Items/heart.png")
                elif self.lifes == 1.5:
                    self.heart_2 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 2:
                    self.heart_2 = pg.image.load("img/Items/heart.png")
                elif self.lifes == 2.5:
                    self.heart_3 = pg.image.load("img/Items/half_heart.png")
                elif self.lifes == 3:
                    self.heart_3 = pg.image.load("img/Items/heart.png")
            elif pow.type == 'door':
                self.quitgame()
        self.animate_text_ly()
        self.camera.update(self.player)

    def events(self):
        #Eventos del loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:  
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   self.quitgame()

    def draw(self):
        #Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.lm,(WIDTH / 32 * 24, 0))    
        self.draw_text('Joystix.ttf', '= ' + str(self.score), 18, colors.WHITE, WIDTH / 32 * 27, 22)
        self.draw_text('Joystix.ttf', 'ETS - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart,(WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2,(WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3,(WIDTH / 32 * 17, 2))
        pg.display.flip()

    def animate_text_ly(self):
        pass

    def load_arrays(self):
        pass

    def show_start_screen(self):
        pass


    def show_go_screen(self):
        #Muestra la pantalla de game over. 
        pass

    def draw_text(self, font_name,text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def quitgame(self):
        pg.quit()
        quit()


def depression():
    d_l = Depression_Level()
        
    while d_l.running:

        d_l.new_game()
        d_l.show_go_screen()

    pg.quit()

def select_level():
    if __name__ == '__main__':
        salir = False
        opcion = [('Test',Drugs_level),
                    ('Hi',Depression_Level)]

        if idioma == 0:
            opcion = [(niveles[0], depression),
                        (niveles[1], drugs),
                        (niveles[2], food_disorders),
                        (niveles[3], test_level),
                        (niveles[4],test_level),
                        (niveles[5],main_menu)]
        if idioma == 1:
            opcion = [(niveles_ingles[0], depression),
                        (niveles_ingles[1], drugs),
                        (niveles_ingles[2], food_disorders),
                        (niveles_ingles[3], test_level),
                        (niveles_ingles[4],test_level),
                        (niveles_ingles[5],main_menu)]

    pg.font.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    levels_screen = pg.image.load("img/Pantallas/levels_menu.png").convert_alpha()
    menu = Menu_Niveles(opcion,colors.WHITE)

    while not salir:

        for e in pg.event.get():
            if e.type == QUIT:
                salir = True
                os.sys.exit()

        screen.blit(levels_screen,(0,0))
        menu.actualizar()
        menu.imprimir(screen)

        pg.display.flip()
        pg.time.delay(10)
    pg.display.quit()

def drugs():
    g = Drugs_level()
        
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()

def food_disorders():
    a_l = Anorexia_Level()
    a_l.show_start_screen()
        
    while a_l.running:

        a_l.new_game()
        a_l.show_go_screen()

    pg.quit()

def obesity():
    o_l = Obesidad_Level()
    o_l.show_start_screen()
        
    while o_l.running:

        o_l.new_game()
        o_l.show_go_screen()

    pg.quit()

def ets():
    e_l = ETS_Level()
    e_l.show_start_screen()
        
    while e_l.running:

        e_l.new_game()
        e_l.show_go_screen()

    pg.quit()

def options():
    pass

def creditos():
    pass

def exit_out():
    import sys
    sys.exit(0)

def test_level():
    pass

def language():
    if __name__ == '__main__':
        salir = False
        opciones = [('Spanish',espanol),
                    ('English', ingles),
                    ('Salir',exit_out)]

    pg.font.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    fondo = pg.image.load("img/Pantallas/language_menu.png").convert()
    menu = Menu(opciones,colors.WHITE)

    while not salir:
        for e in pg.event.get():
            if e.type == QUIT:
                salir = True
                os.sys.exit()

        screen.blit(fondo,(0,0))
        menu.actualizar()
        menu.imprimir(screen)

        pg.display.flip()
        pg.time.delay(10)
    pg.display.quit()

def espanol():
    global idioma
    idioma = 0
    main_menu()

def ingles():
    global idioma
    idioma = 1
    main_menu()

def main_menu():
    if __name__ == '__main__':
        salir = False
        opciones = [('Test',Drugs_level),
                    ('Hi',Depression_Level)]
        if idioma == 0:
            opciones = [  (opciones_espanol[0], select_level),
                            (opciones_espanol[1], options),
                            (opciones_espanol[2], creditos),
                            (opciones_espanol[3], exit_out)]
        if idioma == 1:
            opciones = [  (opciones_ingles[0], select_level),
                            (opciones_ingles[1], options),
                            (opciones_ingles[2], creditos),
                            (opciones_ingles[3], exit_out)]

    pg.font.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    fondo = pg.image.load("img/Pantallas/main_menu.png").convert()
    menu = Menu(opciones,colors.WHITE)

    while not salir:

        for e in pg.event.get():
            if e.type == QUIT:
                salir = True
                os.sys.exit()

        screen.blit(fondo,(0,0))
        menu.actualizar()
        menu.imprimir(screen)

        pg.display.flip()
        pg.time.delay(10)

def options():
    if __name__ == '__main__':
        salir = False
        if idioma == 0:
            opciones = [('Cambiar Idioma',language),
                        ('Audio', ingles),
                        ('Regresar',main_menu)]
        if idioma == 1:
            opciones = [('Change Language',language),
                        ('Audio', ingles),
                        ('Back',main_menu)]
    pg.font.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    fondo = pg.image.load("img/Pantallas/language_menu.png").convert()
    menu = Menu(opciones,colors.WHITE)

    while not salir:
        for e in pg.event.get():
            if e.type == QUIT:
                salir = True
                os.sys.exit()

        screen.blit(fondo,(0,0))
        menu.actualizar()
        menu.imprimir(screen)

        pg.display.flip()
        pg.time.delay(10)
    pg.display.quit()

language()