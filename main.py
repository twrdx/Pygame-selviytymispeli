import pygame
from pygame.locals import *

pygame.init()

#Määrittää pelialueen koon
pelialue = pygame.display.set_mode((500, 300))

pygame.display.set_caption("Kodarit 2 Selviytymispeli")

def talo (x, y, width, height, screen, color):
	points = [(x,y-((2/3.0)* height)), (x,y), (x+width,y), (x+width, y-(2/3.0)*height),
					 (x,y-((2/3.0)*height)), (x+width/2.0, y-height), (x+width, y-(2/3.0)*height)]
	lineThickness = 2
	pygame.draw.lines(screen, color, False, points, lineThickness)

#Hiiri
mouse = pygame.mouse.get_pos()

#pelaaja
pelaaja = pygame.Rect(mouse[0], mouse[1], 30, 30)
olio = pygame.image.load('skull_in_a_ufo_spacecraft.png')
olio.convert()
olio = pygame.transform.scale(olio, (30, 30))

#vihollinen
vihokuva = pygame.image.load('woodpecker.png')
vihokuva.convert()
vihokuva = pygame.transform.scale(vihokuva, (30, 10))
vihollinen = vihokuva.get_rect()
vihollisen_nopeus = [2, 2]

rajahdyskuva = pygame.image.load('rajahdys.png')
rajahdyskuva.convert()

#määritellään fps
FPS = 30
FramePerSec = pygame.time.Clock()

while True:
	
	#event-handler
	for event in pygame.event.get():
		if event.type == MOUSEMOTION:
			mouse = event.pos
			#siirretään pelaaja hiiren kohdalle
			pelaaja = pygame.Rect(mouse[0], mouse[1], 30, 30)

	vihollinen = vihollinen.move(vihollisen_nopeus)


	if vihollinen.left < 0:
		vihollisen_nopeus[0] *= -1
	if vihollinen.right > 500:
		vihollisen_nopeus[0] *= -1
	if vihollinen.top < 0:
		vihollisen_nopeus[1] *= -1
	if vihollinen.bottom > 250:
		vihollisen_nopeus[1] *= -1

	tausta = (102, 153, 255)
	
	pelialue.fill(tausta)

	#maa
	pygame.draw.rect(pelialue, "#663300", (0, 250, 500, 50))
	
	#kivi
	pygame.draw.ellipse(pelialue, (102, 102, 153), (50, 235, 50, 20))
	
	#talo
	talo(300, 250, 100, 100, pelialue, "red")
	
	#kuu
	pygame.draw.ellipse(pelialue, "white", (30, 30, 80, 80))
	pygame.draw.ellipse(pelialue, tausta, (50, 30, 60, 60))

	pelialue.blit(olio, pelaaja)
	pelialue.blit(vihokuva,vihollinen)

	if pygame.Rect.colliderect(pelaaja, vihollinen) == True:
		print("Osuma tapahtui")
		rajahdyskuva = pygame.transform.scale(rajahdyskuva, (100, 100))
		pelaaja.move_ip(-50, -50)
		pelialue.blit(rajahdyskuva, pelaaja)
		vihollisen_nopeus = [0, 0]

		pygame.display.update()
		break 
	else:
		pelialue.blit(olio, pelaaja)
		
		

	pygame.display.update()
	FramePerSec.tick(FPS)
