from aha_libraries import *


class DepressionLevel:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        back = pygame.image.load(resources.DEPRESSION.SCENARIO_DEPRESSION_1366x768).convert()
        run = True
        self.score = 0
        """self.lifes = 0
        self.volumen = 0
        self.all_sprites = ""
        self.walls = ""
        self.powerups = ""
        self.enemies = ""
        self.proyectiles = """""
        self.current_frame = 0
        self.last_update = 0
        pygame.mixer.music.load(resources.TTU)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(loops=-1)
        while run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                    os.sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        os.sys.exit()
            screen.blit(back, (0, 0))
            pygame.display.update()

    def new_game(self):
        self.score = 0
        """self.lifes = 3
        self.volumen = 1
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.proyectiles = pygame.sprite.Group()"""
        self.current_frame = 0
        self.last_update = 0