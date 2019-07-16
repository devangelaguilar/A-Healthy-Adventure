from aha_libraries import *

pygame.init()
run = True
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)

if true_res == settings.SCREEN1:
    settings.WIDTH = 1366
    settings.HEIGHT = 768


while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            os.sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                os.sys.exit()
    screens.main_screen()
