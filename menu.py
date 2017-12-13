import pygame, drawbg, data, time, sys

class Menu:
	fn_img_play = "Images/Image 16.png"
	fn_img_play2 = "Images/Image 18.png"

	def __init__(self, surface):
		self.surface = surface
		self.play1 = pygame.image.load(Menu.fn_img_play).convert_alpha()
		self.play2 = pygame.image.load(Menu.fn_img_play2).convert_alpha()
		self.my_font = pygame.font.SysFont("simsunnsimsun", 46)
		self.my_font.set_bold(True)
		self.title = self.my_font.render("大鱼吃小鱼", True, (0,0,0))
		self.play = self.play1
		self.choose_font = pygame.font.SysFont("simsunnsimsun", 20)
		self.easy = self.choose_font.render("简单", True, (0,0,0))
		self.ordinary = self.choose_font.render("普通", True, (0,0,0))
		self.hard = self.choose_font.render("困难", True, (0,0,0))
		self.choose_font.set_bold(True)
		self.right = self.choose_font.render("√", True, (255,255,255))

	def draw(self):
		drawbg.DrawBackground().draw(self.surface)
		self.surface.blit(self.title, (275,80))
		self.surface.blit(self.easy, (381,220))
		self.surface.blit(self.ordinary, (381,250))
		self.surface.blit(self.hard, (381,280))
		self.surface.blit(self.play, (data.SCREEN_SIZE[0]/2-56,380))
		position = (362, 220)
		if data.hard_level == 2:
			position = (362, 250)
		elif data.hard_level == 3:
			position = (362, 280)
		#pygame.draw.rect(self.surface, (0,0,255),pygame.locals.Rect(position,(16,16)))
		self.surface.blit(self.right, position)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					sys.exit()
				if event.type == pygame.locals.MOUSEMOTION:
					if event.pos[0]>=344 and event.pos[0]<=452 and \
						event.pos[1]>=380 and event.pos[1]<=410:
						self.play = self.play2
					else:
						self.play = self.play1
				if event.type == pygame.locals.MOUSEBUTTONDOWN:
					if event.pos[0]>=344 and event.pos[0]<=452 and \
						event.pos[1]>=380 and event.pos[1]<=410:
						return
					if event.pos[0]>=370 and event.pos[0]<=424:
						if event.pos[1]>=220:
							if event.pos[1]<=246:
								data.hard_level = 1
							elif event.pos[1]<=276:
								data.hard_level = 2
							elif event.pos[1]<=306:
								data.hard_level = 3
			self.draw()
			pygame.display.update()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode(data.SCREEN_SIZE,0,32)
	Menu(screen).run()