import pygame

def loadImage(fileName):
	pygame.init()
	return pygame.image.load(fileName).convert_alpha()