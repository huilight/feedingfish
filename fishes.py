from fish import Fish
import pygame
from random import randint
from fn2img import Fn2img

class Fishes(Fish):

	def __init__(self, pos, level, imageStartNum):
		self.imgo = Fn2img("./Images/Image "+str(imageStartNum)+".png")
		self.image = self.imgo.img
		super().__init__(pos, level, self.image)
		self.time = 0

	def move(self, time_passed, bg_position):
		pos = self.dest - self.pos
		self.imgo.set_direction(pos[0])
		self.image = self.imgo.img
		if (pos[0]<2 and pos[0]>-2) and (pos[1]<5 and pos[1]>-5):
			super().set_dest(pygame.math.Vector2(randint(0, 908),randint(0, 720)))
		super().move(time_passed, bg_position)


	def update(self):
		self.time += 1
		id = int(self.imgo.fn[-7:-4])
		if self.time<24:
			id += 2
		else:
			self.time = 0
			id -= 46
		self.imgo = Fn2img(self.imgo.fn[:-7]+str(id)+".png")
		self.image = self.imgo.img
		super().change_img(self.image)