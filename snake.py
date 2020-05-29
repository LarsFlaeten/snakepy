from pygame.locals import *
import pygame
import time
from random import randint

base_unit = 44

class Pannekake:
    x = 0
    y = 0   
    verdi = 0
    def __init__(self, x, y, verdi):
        self.x = x * base_unit
        self.y = y * base_unit
        self.verdi = verdi



class Slange:
    x = []
    y = []
    fart = base_unit
    retning = 0
    lengde = 0

    def __init__(self, lengde):
        self.lengde = lengde
        for i in range(0, lengde):
            self.x.append(0)
            self.y.append(0)

    def nyLengde(self, lengde):
        for i in range(0, lengde - self.lengde):
            self.x.append(self.x[self.lengde-1])
            self.y.append(self.y[self.lengde-1])
        self.lengde = lengde

    def update(self):
        for i in range(self.lengde-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.retning == 0:
            self.x[0] = self.x[0] + self.fart
        if self.retning == 1:
            self.x[0] = self.x[0] - self.fart
        if self.retning == 2:
            self.y[0] = self.y[0] + self.fart
        if self.retning == 3:
            self.y[0] = self.y[0] - self.fart
        
    def draw(self, surface, image):
        for i in range(0,self.lengde):
            surface.blit(image,(self.x[i],self.y[i])) 


    def flyttHoyre(self):
        self.retning = 0
        
    def flyttVenstre(self):
        self.retning = 1
        
    def flyttOpp(self):
        self.retning = 3

    def flyttNed(self):
        self.retning = 2



class App:
    step = 200
    poeng = 0

    bredde = 30
    hoyde = 20

    windowHeight = hoyde * base_unit
    windowWidth = bredde * base_unit
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.slange = Slange(3) 
        self.pannekake = Pannekake(randint(0, self.bredde-1), randint(0, self.hoyde-1), 100)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('SNAKE: Du har {} poeng'.format(self.poeng))
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()
        self._pannekake_surf = pygame.image.load("pannekake.png").convert() 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.slange.update()
        if self.slange.x[0] < 0 or self.slange.x[0] >= self.windowWidth or self.slange.y[0] < 0 or self.slange.y[0] >= self.windowHeight:
            print("DU KJØRTE UTENFOR BRETTET! Du fikk {} poeng!".format(self.poeng))
            self._running = False



        if self.slange.x[0] == self.pannekake.x and self.slange.y[0] == self.pannekake.y:
            self.slange.nyLengde(self.slange.lengde+2)
            self.poeng += self.pannekake.verdi
            pygame.display.set_caption('SNAKE: Du har {} poeng'.format(self.poeng))
            self.pannekake = Pannekake(randint(0, self.bredde-1), randint(0, self.hoyde-1), 100)
            if(self.slange.lengde > 10):
                self.step /= 1.2

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.slange.draw(self._display_surf,self._image_surf)
        self._display_surf.blit(self._pannekake_surf,(self.pannekake.x,self.pannekake.y))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            
            if (keys[K_RIGHT]):
                self.slange.flyttHoyre()

            if (keys[K_LEFT]):
                self.slange.flyttVenstre()

            if (keys[K_UP]):
                self.slange.flyttOpp()

            if (keys[K_DOWN]):
                self.slange.flyttNed()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()


            time.sleep(self.step/1000)
        self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()
