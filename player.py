import pygame, data
from fish import Fish
from fn2img import Fn2img
class Player(Fish):

	def __init__(self, pos, level):
		img = self.get_img(level)
		super().__init__(pos, level, img.img)
		self.imgo = img
		self.image = self.imgo.img
		self.time = 0
		self.dest = pos
		self.dir = (0,0)
		self.death_time = 0
		self.score = 0


	def set_dest(self, pos):
		self.dest = pos-(20,20)
		self.imgo.set_direction(self.dir[0])

	def move(self):
		pos = self.dest - super().get_pos()
		self.dir = pos.normalize()
		distance = self.dir * (pos.length()/220)
		self.pos = distance + self.pos
		super().change_rect()

	def get_img(self, level):
		fn_img = "./Images/Image "
		if level == 1:
			img = fn_img + "297.png"
		elif level == 3:
			img = fn_img + "349.png"
		else:
			img = fn_img + "407.png"
		return Fn2img(img)

	def update(self):
		self.time += 1
		id = int(self.imgo.fn[-7:-4])
		if self.time<24:
			id += 2
		else:
			self.time = 0
			id -= 46
		self.imgo.change_img(self.imgo.fn[:-7]+str(id)+".png")
		self.image = self.imgo.img

	def kill(self):
		"""处理死亡后的事件"""
		self.death_time += 1
		self.pos = (data.SCREEN_SIZE[0]/2,data.SCREEN_SIZE[1]/2)

	def draw(self, surface):
		self.surface = surface
		surface.blit(self.image, self.pos)

	def add_score(self, level):
		if level == 0:
			self.score += 5
		elif level == 2:
			self.score += 10
		else:
			self.score += 20

		data.score = self.score

		if self.score >= data.level2_score and self.level == 3:
			self.grow()
		elif self.score >= data.level1_score and self.level == 1:
			self.grow()

	def grow(self):
		self.level += 2
		self.imgo = self.get_img(self.level)
		self.image = self.imgo.img
		self.time = 0
		self.rect = self.image.get_rect()
		self.rect2 = self.image.get_rect()