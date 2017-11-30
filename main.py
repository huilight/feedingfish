import pygame, drawbg, tools, eat, data,fishnum, sound
import time as timer
from player import Player
from pygame.math import Vector2
from pygame.locals import *
from fishes import Fishes

pygame.mixer.pre_init(44100, 16, 2, 1024*4)

pygame.init()

screen = pygame.display.set_mode(data.SCREEN_SIZE,0,32)

bg = drawbg.DrawBackground()

clock = pygame.time.Clock()

fishnum.ControlFishNum.update()
p1 = Player(Vector2(data.SCREEN_SIZE[0]/2,data.SCREEN_SIZE[1]/2),1)
time = 0

se = sound.SoundEffect()
bgmusic = sound.BgMusic()
bgmusic.set_volume(1)
ea = eat.Eat()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

		if event.type == MOUSEMOTION:
			p1.set_dest(Vector2(event.pos))
			bg.move(event.pos)
			
		if event.type == MOUSEBUTTONDOWN:
			if event.pos[0] >= 440 and event.pos[0] <= 465 and \
			 event.pos[1] >= 2 and event.pos[1] <= 27:
				sound.SoundControl.visible = True
				
			elif event.pos[0] >= 480 and event.pos[0] <= 505 and \
			 event.pos[1] >= 2 and event.pos[1] <= 27:
				ev = pygame.event.wait()
				while not ev.type == MOUSEBUTTONDOWN:
					ev = pygame.event.wait()
				clock.tick()

	bg.update()
	time_passed = clock.tick()/1000

	time += time_passed
	if time >= 0.2:
		time = 0
		p1.update()
		data.level0.update()
		data.level2.update()
		data.level4.update()
		fishnum.ControlFishNum.update()

	p1.move()

	for level in data.level_group.values():
		for f in level.sprites():
			f.move(time_passed, bg.bg_position)

	ea.eat(bg, p1)

	bg.draw(screen)
	p1.draw(screen)
	data.level4.draw(screen)
	data.level2.draw(screen)
	data.level0.draw(screen)
	if ea.e != None:
		ea.e.update(time_passed)
		ea.e.draw(screen)

	bg.draw_state(screen)
	bg.draw_score(screen)

	if sound.SoundControl.visible:
		sound.SoundControl.draw_surface(screen)
		sound.SoundControl.open(screen)
		clock.tick()
	pygame.display.update()
