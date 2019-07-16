from aha_libraries import *


def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
    screen_main = ""
    run = True
    if settings.WIDTH == 1366 and settings.HEIGHT == 768:
        print(str(settings.WIDTH) + " - " + str(settings.HEIGHT))
        screen_main = pygame.image.load(resources.SCREEN1.MAIN_SCREEN)
    else:
        exit()
    while run:
        screen.blit(screen_main, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menus.main_menu()
        pygame.display.update()
