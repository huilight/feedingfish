import pygame, data

class GameStatus:

	def __init__(self, player, surface):
		fn_img_gameover = "Images/Image 1118.png"
		
		self.surface = surface
		self.player = player
		self.game_over = pygame.image.load(fn_img_gameover).convert_alpha()
		self.my_font = pygame.font.SysFont("simsunnsimsun", 16)
		self.restart = self.my_font.render("单击重新开始", True, (0,0,0))
		my_font2 = pygame.font.SysFont("simsunnsimsun", 26)
		my_font2.set_bold(True)
		self.show_win = my_font2.render("WIN", True, (0,0,0))

	def win_or_loss(self):
		if self.player.death_time == 3:
			self.loss()
			return True
		
		if self.player.score > data.level3_score:
			self.win()
			return True

		return False

	def loss(self):
		self.surface.blit(self.game_over, (data.SCREEN_SIZE[0]/2-118.5, data.SCREEN_SIZE[1]/2-28))
		self.surface.blit(self.restart, (352, 320))
		pygame.display.update()
		self.get_event()

	def win(self):
		self.surface.blit(self.show_win, (380, 220))
		self.surface.blit(self.restart, (352, 320))
		pygame.display.update()
		self.get_event()

	def get_event(self):
		while True:
			event = pygame.event.wait()
			if event.type == pygame.locals.QUIT:
				exit()
			if event.type == pygame.locals.MOUSEBUTTONDOWN:
				self.player.score = 0
				data.score = 0
				for group in data.level_group.values():
					group.empty()
				self.player.death_time = 0
				return True