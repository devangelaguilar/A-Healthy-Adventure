from aha_libraries import *


class DepressionLevel:
    def __init__(self):
        # Inicia el juego, ventana, etc.
        pygame.init()
        pygame.mixer.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(settings.TITLE)
        self.running = True
        self.heart = pygame.image.load("img/heart.png").convert_alpha()
        self.heart_2 = pygame.image.load("img/heart.png").convert_alpha()
        self.heart_3 = pygame.image.load("img/heart.png").convert_alpha()
        self.lm = pygame.image.load("img/heart_ly.png").convert_alpha()
        self.font_name = pygame.font.match_font(resources.FONTS.JOYSTIX)
        self.pos_song = 0
        self.load_data_depression()

    def load_data_depression(self):
        self.dir = os.path.dirname(__file__)
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'img/Depression')
        with open(os.path.join(self.dir, settings.HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.map = Map(os.path.join(self.game_folder, 'maps/Depression - map_1.txt'))
        self.spritesheet = Spritesheet(os.path.join(self.img_folder, JOSEPH_SPRITESHEET))
        self.spritesheet_minion = Spritesheet(os.path.join(self.img_folder, MINION_DEPRESSION_SPRITESHEET))
        self.energy_ball = pg.image.load("img/Depression/Energy_Ball.png").convert_alpha()
        self.energy = self.energy_ball.get_rect()
        self.heart_anim = Spritesheet(os.path.join(self.img_folder, HEART_ANIM))
        self.heart_ly_anim = Spritesheet(os.path.join(self.img_folder, HEART_LY_ANIM))
        self.background = pg.image.load("img/Depression/Scenario.png").convert_alpha()
        self.top_bar = pg.image.load("img/Depression/top_bar.png").convert_alpha()
        self.jos = pg.image.load("img/Depression/Joseph.png").convert_alpha()
        self.hfk = pg.image.load("img/hfk.png").convert_alpha()
        self.snd_dir = os.path.join(self.dir, 'snd')

    def new_game(self):
        # New game.
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
        # self.text = self.lov[0]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Floor(self, col, row)
                if tile == '1':
                    Floor_Depression(self, col, row)
                if tile == '2':
                    Floor_Depression_1(self, col, row)
                if tile == '6':
                    Floor_Depression_2(self, col, row)
                if tile == '3':
                    Pow_Life(self, col, row)
                if tile == '4':
                    Minus_Life(self, col, row)
                if tile == '5':
                    Pow_Coin(self, col, row)
                if tile == 'P':
                    self.player = Joseph(self, col, row)
                if tile == 'D':
                    Door(self, col, row)
                if tile == 'M':
                    self.minion = Minion_Depression(self, col, row)
        pg.mixer.music.load(os.path.join(self.snd_dir, 'Sorry.mp3'))
        pg.mixer.music.set_volume(self.volumen)
        self.camera = Camara(self.map.width, self.map.height)
        self.pos_x = 0
        self.pos_y = 0
        self.show_start_screen()

    def run(self):
        # Loop Principal.
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(1500)

    def update(self):
        # Update para el loop.
        self.screen.fill(colors.WHITE)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.update()
        self.powerups.update()
        self.enemies.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

            hit_enemy = pg.sprite.spritecollide(self.player, self.enemies, True)
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
        # if self.pos_y >= 1500:
        # self.show_go_screen()
        self.pos_x = self.player.pos.x
        self.pos_y = self.player.pos.y
        self.camera.update(self.player)

    def events(self):
        # Eventos del loop.
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
        # Dibujar pantalla durante el loop.
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.screen.blit(self.lm, (WIDTH / 32 * 24, 0))
        self.draw_text('fonts/Joystix.ttf', '= ' + str(self.score), 14, colors.WHITE, WIDTH / 32 * 27, 22)
        if idioma == 0:
            self.draw_text('fonts/Joystix.ttf', 'Depresion: 100%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('fonts/Joystix.ttf', 'Depresion - Nivel 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        else:
            self.draw_text('fonts/Roboto-Light.ttf', 'Depression: 100%', 14, colors.WHITE, WIDTH / 32 * 25, 62)
            self.draw_text('fonts/Roboto-Light.ttf', 'Depression - Level 1', 12, colors.WHITE, WIDTH / 32 * 16, 0)
        self.screen.blit(self.heart, (WIDTH / 32 * 13, 2))
        self.screen.blit(self.heart_2, (WIDTH / 32 * 15, 2))
        self.screen.blit(self.heart_3, (WIDTH / 32 * 17, 2))
        self.draw_text('fonts/Roboto-Light.ttf', 'Halsey - Sorry', 12, colors.WHITE, WIDTH / 32 * 28, 605)
        self.screen.blit(self.hfk, (WIDTH / 32 * 30, 590))
        """self.draw_text('fonts/Roboto-Light.ttf', str(self.pos_x), 12, colors.WHITE, WIDTH / 32 * 16, 240)
        self.draw_text('fonts/Roboto-Light.ttf', str(self.pos_y), 12, colors.WHITE, WIDTH / 32 * 16, 260)"""
        pg.display.flip()

    def update_lifes(self):
        if self.lifes == 0:
            self.quitgame()
        if self.lifes == 1:
            self.heart = pg.image.load("img/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/no_heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/no_heart.png").convert_alpha()
        if self.lifes == 2:
            self.heart_1 = pg.image.load("img/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/no_heart.png").convert_alpha()
        if self.lifes == 3:
            self.heart_1 = pg.image.load("img/heart.png").convert_alpha()
            self.heart_2 = pg.image.load("img/heart.png").convert_alpha()
            self.heart_3 = pg.image.load("img/heart.png").convert_alpha()

    def load_arrays(self):
        pass

    def show_start_screen(self):
        screen_load = True
        if idioma == 0:
            self.load_screen_1 = pg.image.load("img/Depression/load_screen_level_1.png").convert_alpha()
        else:
            self.load_screen_1 = pg.image.load("img/Depression/load_screen_level_1_english.png").convert_alpha()
        while screen_load:
            self.screen.blit(self.load_screen_1, (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    os.sys.exit()
            pg.display.update()
            pg.time.delay(3000)
            self.run()

    def show_go_screen(self):
        os.sys.exit()

    def pause(self):
        pg.mixer_music.pause()
        reloj = pg.time.Clock()
        if idioma == 0:
            self.load_screen = pg.image.load("img/Depression/pause_menu.png").convert_alpha()
        else:
            self.load_screen = pg.image.load("img/Depression/pause_menu_english.png").convert_alpha()
        while pause:
            self.screen.blit(self.load_screen, (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    os.sys.exit()
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
        pg.mixer_music.unpause()
        global pause
        pause = False

    def draw_text(self, font_name, text, size, color, x, y):
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
        self.load_screen = pg.image.load("img/Depression/depresion_screen_1.png")
        while screen_load:
            self.screen.blit(self.load_screen, (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    os.sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        """d_l_2 = Depression_Level_2()
                        d_l_2.show_start_screen()
                        while d_l_2.running:
                            d_l_2.new_game()
                            d_l_2.show_go_screen()"""
                        select_level()

                        pg.quit()
            pg.display.update()
