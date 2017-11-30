import pygame

class Fn2img:
	
	def __init__(self, fn):
		self.fn = fn
		self.img = pygame.image.load(fn).convert_alpha()
		self.current_dir = True
		self.move_dir = True 

	def set_direction(self, num):
		if num > 0:
			self.move_dir = False
		else:
			self.move_dir = True
		self.change_direction()

	def change_direction(self):
		if self.current_dir != self.move_dir:
			self.current_dir = not self.current_dir
			self.img = pygame.transform.flip(self.img, True, False)

	def change_img(self, fn):
		del self.img
		self.fn = fn
		self.img = pygame.image.load(fn).convert_alpha()
		self.current_dir = True
		self.change_direction()

	def __str__(self):
		return fn