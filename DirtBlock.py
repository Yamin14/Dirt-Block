#3d cube

import pygame
pygame.init()
screen = pygame.display.set_mode((700, 1400))
brown = (101, 67, 33)
green = (0, 255, 0)

running = True
while running:
	screen. fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

        shadow = pygame.draw.polygon(screen, (100, 100, 100), [(200, 800), (100, 600), (170, 420), (358, 400)])

	front = pygame.draw.rect(screen, brown, (200, 500, 300, 300))
	
	top = pygame.draw.polygon(screen, green, [(200, 500), (358, 345), (658, 345), (500, 500)])
	
	side = pygame.draw.polygon(screen, brown, [(658, 345), (658, 645), (500, 800), (500, 500)])
	
	line = pygame.draw.line(screen, (0, 0, 0), (500, 500), (500, 800))

	pygame.display.flip()
pygame.quit()
