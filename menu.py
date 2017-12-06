import pygame, drawbg, data, time

class Menu:
	fn_img_play = "Images/Image 16.png"

	def __init__(self, surface):
		self.surface = surface
		self.play = pygame.image.load(Menu.fn_img_play).convert_alpha()
		self.my_font = pygame.font.SysFont("simsunnsimsun", 46)
		self.my_font.set_bold(True)
		self.title = self.my_font.render("大鱼吃小鱼", True, (0,0,0))
		
		self.choose_font = pygame.font.SysFont("simsunnsimsun", 20)
		self.easy = self.choose_font.render("简单", True, (0,0,0))
		self.ordinary = self.choose_font.render("普通", True, (0,0,0))
		self.hard = self.choose_font.render("困难", True, (0,0,0))

	def draw(self):
		drawbg.DrawBackground().draw(self.surface)
		self.surface.blit(self.title, (275,80))
		self.surface.blit(self.easy, (381,220))
		self.surface.blit(self.ordinary, (381,250))
		self.surface.blit(self.hard, (381,280))
		self.surface.blit(self.play, (data.SCREEN_SIZE[0]/2-56,380))

	def run(self):
		self.draw()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					exit()
				if event.type == pygame.locals.MOUSEBUTTONDOWN:
					print(event.pos)
					if event.pos[0]>=380 and event.pos[0]<=424:
						if event.pos[1]>=220 and event.pos[1]<=235:
							pygame.draw.rect(self.surface, (0,0,255),pygame.locals.Rect((360,220),(16,16)))
							data.hard_level = 1
						elif event.pos[1]<=265:
							data.hard_level = 2
						elif event.pos[1]<=295:
							data.hard_level = 3
			
			pygame.display.update()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode(data.SCREEN_SIZE,0,32)
	Menu(screen).run()
	time.sleep(3)