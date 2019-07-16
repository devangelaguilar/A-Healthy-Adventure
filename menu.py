from aha_libraries import *


class Opcion:

    def __init__(self, fuente, text_color, titulo, x, y, igualdad, funcion_asignada):
        self.x = x
        self.imagen_normal = fuente.render(titulo, 1, text_color)
        self.imagen_destacada = fuente.render(titulo, 1, text_color)
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * igualdad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = settings.WIDTH / 5 * 2
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
        self.image = pygame.image.load('resources/img/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)
        self.to_y = 0

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class ShowMenu:

    def __init__(self, opciones, text_color):
        self.opciones = []
        pygame.display.set_caption(settings.TITLE)
        fuente = pygame.font.Font(resources.FONTS.JOYSTIX, 25)
        x = settings.WIDTH
        y = settings.HEIGHT
        igualdad = 1

        self.cursor = Cursor(x - 1000, y - 375, 55)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, text_color, titulo, x, y, igualdad, funcion))
            y += 55
            if igualdad == 1:
                igualdad = -1
            else:
                igualdad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[pygame.K_UP]:
                self.seleccionado -= 1
            elif k[pygame.K_DOWN]:
                self.seleccionado += 1
            elif k[pygame.K_RETURN]:
                self.opciones[self.seleccionado].activar()

        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        self.mantiene_pulsado = k[pygame.K_UP] or k[pygame.K_DOWN] or k[pygame.K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)


class ShowMenuLevels:

    def __init__(self, opciones, text_color):
        self.opciones = []
        pygame.display.set_caption(settings.TITLE)
        fuente = pygame.font.Font(resources.FONTS.JOYSTIX, 20)
        x = settings.WIDTH / 5 * 2
        y = settings.HEIGHT / 12 * 4
        igualdad = 1

        self.cursor = Cursor(x - 30, y, 50)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, text_color, titulo, x, y, igualdad, funcion))
            y += 50
            if igualdad == 1:
                igualdad = -1
            else:
                igualdad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[pygame.K_UP]:
                self.seleccionado -= 1
            elif k[pygame.K_DOWN]:
                self.seleccionado += 1
            elif k[pygame.K_RETURN]:
                self.opciones[self.seleccionado].activar()

        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        self.mantiene_pulsado = k[pygame.K_UP] or k[pygame.K_DOWN] or k[pygame.K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)
