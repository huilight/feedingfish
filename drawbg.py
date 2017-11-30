import pygame,data
from pygame.locals import *

class DrawBackground:
	fn_background = "./images/Image 112.jpg"
	fn_stone = "./images/Image 120.png"
	fn_stage1 = "./images/Image 582.png"
	fn_stage2 = "./images/Image 585.png"
	fn_state_line = "./images/Image 1104.png"
	fn_control = "./images/ImageControl.png"
	fn_pause = "./images/ImagePause.png"
	position = (55,0)

	def __init__(self):
		pygame.init()
		self.my_font = pygame.font.SysFont("arial", 16)

		self.background = pygame.image.load(DrawBackground.fn_background).convert()
		self.bg = pygame.transform.smoothscale(self.background, (908,720))

		self.stone = pygame.image.load(DrawBackground.fn_stone).convert_alpha()
		self.stage1 = pygame.image.load(DrawBackground.fn_stage1).convert_alpha()
		self.stage2 = pygame.image.load(DrawBackground.fn_stage2).convert_alpha()
		self.state_line = pygame.image.load(DrawBackground.fn_state_line).convert_alpha()
		self.state_line = pygame.transform.smoothscale(self.state_line, (data.SCREEN_SIZE[0],55))
		self.control = pygame.image.load(DrawBackground.fn_control).convert_alpha()
		self.pause = pygame.image.load(DrawBackground.fn_pause).convert_alpha()
		self.bg_position = pygame.math.Vector2(0,-170)
		self.step = (0,0)
		self.pos = (0,55)

	def move(self,pos):
		self.pos = pos
		if pos[0] < 150:
			self.step = (1,0)
		elif pos[0] > 650:
			self.step = (-1,0)
		elif pos[1] < 150:
			self.step = (0, 1)
		elif pos[1] > 400:
			self.step = (0,-1)
		else:
			self.step = (0,0)

	def update(self):
		if self.bg_position[0]>=0 and self.pos[0]<150:
			self.step = (0,0)
		elif self.bg_position[0]<=-108 and self.pos[0]>650:
			self.step = (0,0)
		elif self.bg_position[1]>=0 and self.pos[1]<150:
			self.step = (0,0)
		elif self.bg_position[1]<=-170 and self.pos[1]>400:
			self.step = (0,0)

		self.bg_position += self.step
		DrawBackground.position = self.bg_position

		#update score
		self.score = self.my_font.render(str(data.score), True, (255, 255, 255))


	def draw(self, surface):
		#surface.set_clip(0,0,data.SCREEN_SIZE[0],49)
		
		
		#surface.set_clip(0,50,data.SCREEN_SIZE[0]-1,data.SCREEN_SIZE[1]-1)
		surface.blit(self.bg,self.bg_position)
		surface.blit(self.stone,self.bg_position+(0, 180))
		surface.blit(self.stage1,self.bg_position+(424, 568))
		surface.blit(self.stage2,self.bg_position+(252, 650))

	def draw_state(self, surface):
		surface.blit(self.state_line,(0,0))
		surface.blit(self.control,(440,2))
		surface.blit(self.pause,(480,2))

	def draw_score(self, surface):
		surface.blit(self.score,(78,5))

		if data.score <= data.level1_score:
			length = data.score/data.level1_score*72
		elif data.score <= data.level2_score:
			length = 72 + (data.score-data.level1_score)/(data.level2_score\
				-data.level1_score)*72
		elif data.score <= data.level3_score:
			length = 144 + (data.score-data.level2_score)/(data.level3_score\
				-data.level2_score)*71
		else:
			length = 215
		pygame.draw.rect(surface, (0,0,255),Rect((578,25),(length,9)))
