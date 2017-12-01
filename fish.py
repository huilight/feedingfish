import pygame
import drawbg

class Fish(pygame.sprite.Sprite):

	def __init__(self, pos, level, img):
		super().__init__()
		self.pos = pos
		self.level = level
		self.image = img
		self.rect = self.image.get_rect()
		self.rect2 = self.image.get_rect() #矩形大小
		self.time = 0
		self.dest = pos
		self.direction = (0,0)
		self.left = True
		self.speed = 220

	def set_dest(self, pos):
		self.dest = pos
		self.direction = (self.dest-self.pos).normalize()
		# if self.dir[0]<0:
		# 	Fn2img.isLeft = True
		# else:
		# 	Fn2img.isLeft = False

	def move(self, time_passed, bg_position):
		pos = self.dest - self.pos
		try:
			self.pos += self.direction * (self.speed*time_passed)
		except:
			print(self.pos, self.direction, self.speed, self.time_passed)
		self.change_rect(bg_position)

	def get_pos(self):
		return self.pos

	def change_rect(self, bg_position=(0,0)):
		self.rect[0] = self.rect2[0] + self.pos[0] + bg_position[0]
		self.rect[1] = self.rect2[1] + self.pos[1] + bg_position[1]
		self.rect[2] = self.rect2[2] + self.pos[0] + bg_position[0]
		self.rect[3] = self.rect2[3] + self.pos[1] + bg_position[1]

	def change_img(self, img):
		self.image = img
