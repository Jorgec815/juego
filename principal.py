import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Choque" )
    background_image = util.cargar_imagen('imagenes/fondonuevo.jpg');
    gameover_image = util.cargar_imagen('imagenes/gameover2.png')
    pierde_vida = util.cargar_sonido('sonidos/barril.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    villano = [Villano((randint(0,610),randint(0,410)),1),
               Villano((randint(0,610),randint(0,410)),1),
               Villano((randint(0,610),randint(0,410)),1),
               Villano((randint(0,610),randint(0,410)),1),
               Villano((randint(0,610),randint(0,410)),1)]
                          
    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,0,0))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,0,0))
        texto_dificultad = fuente.render("A = easy || D = hard",1,(0,0,0))
        
        heroe.update()
        
        for n in villano:
            n.update(heroe)
        
        for n in villano:
            if heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[0]
                pierde_vida.play()
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1
                n.rect.x = 610
                n.rect.y = randint(1,410)
            elif n.rect.x <=20:
				heroe.puntos += 1
				n.rect.x = 610
				n.rect.y = randint(0,410)  
			
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(450,450))
        screen.blit(texto_puntos,(100,450))
        screen.blit(texto_dificultad,(250,450))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

      
if __name__ == '__main__':
      game()

