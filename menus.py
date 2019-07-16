from aha_libraries import *


def main_menu():
    pygame.init()

    opciones = [('Test', None)]

    if settings.LANGUAGE == 0:
        if settings.WIDTH == 1366 and settings.HEIGHT == 768:
            fondo = pygame.image.load(resources.SCREEN1.MAIN_MENU_ESP).convert()
            opciones = [(arrays.SPANISH.OPTIONS[0], game_modes_menu),
                        (arrays.SPANISH.OPTIONS[1], None),
                        (arrays.SPANISH.OPTIONS[2], None),
                        (arrays.SPANISH.OPTIONS[3], out)]

    if settings.LANGUAGE == 1:
        if settings.WIDTH == 1366 and settings.HEIGHT == 768:
            fondo = pygame.image.load(resources.SCREEN1.MAIN_MENU_ENG).convert()
            opciones = [(arrays.ENGLISH.OPTIONS[0], game_modes_menu),
                        (arrays.ENGLISH.OPTIONS[1], None),
                        (arrays.ENGLISH.OPTIONS[2], None),
                        (arrays.ENGLISH.OPTIONS[3], out)]
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
    menu_principal = menu.ShowMenu(opciones, colors.BASIC.WHITE)
    salir = False

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True
                os.sys.exit()

        screen.blit(fondo, (0, 0))
        menu_principal.actualizar()
        menu_principal.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)


def game_modes_menu():
    pygame.init()
    salir = False
    niveles = [('Test', None)]

    if settings.LANGUAGE == 0:
        niveles = [(arrays.SPANISH.GAME_MODES[0], None),
                   (arrays.SPANISH.GAME_MODES[1], levels_menu),
                   (arrays.SPANISH.GAME_MODES[2], main_menu)]

    if settings.LANGUAGE == 1:
        niveles = [(arrays.ENGLISH.GAME_MODES[0], None),
                   (arrays.ENGLISH.GAME_MODES[1], levels_menu),
                   (arrays.ENGLISH.GAME_MODES[2], main_menu)]

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
    game_modes_screen = pygame.image.load(resources.SCREEN1.GAME_MODES_SCREEN).convert_alpha()
    game_modes = menu.ShowMenuLevels(niveles, colors.BASIC.WHITE)

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True
                os.sys.exit()

        screen.blit(game_modes_screen, (0, 0))
        game_modes.actualizar()
        game_modes.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
    pygame.display.quit()


def levels_menu():
    pygame.init()
    salir = False
    niveles = [('Test', None)]

    if settings.LANGUAGE == 0:
        niveles = [(arrays.SPANISH.LEVELS[0], gameLevels.depressionLevels.DepressionLevel),
                   (arrays.SPANISH.LEVELS[1], None),
                   (arrays.SPANISH.LEVELS[2], None),
                   (arrays.SPANISH.LEVELS[3], None),
                   (arrays.SPANISH.LEVELS[4], None),
                   (arrays.SPANISH.LEVELS[5], main_menu)]

    if settings.LANGUAGE == 1:
        niveles = [(arrays.ENGLISH.LEVELS[0], gameLevels.depressionLevels.DepressionLevel),
                   (arrays.ENGLISH.LEVELS[1], None),
                   (arrays.ENGLISH.LEVELS[2], None),
                   (arrays.ENGLISH.LEVELS[3], None),
                   (arrays.ENGLISH.LEVELS[4], None),
                   (arrays.ENGLISH.LEVELS[5], main_menu)]

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
    levels_screen = pygame.image.load(resources.SCREEN1.LEVELS_MENU).convert_alpha()
    levels = menu.ShowMenuLevels(niveles, colors.BASIC.WHITE)

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True
                os.sys.exit()

        screen.blit(levels_screen, (0, 0))
        levels.actualizar()
        levels.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
    pygame.display.quit()


def out():
    os.sys.exit()
