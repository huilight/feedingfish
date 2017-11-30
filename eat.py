import pygame, data, tools, sound

class DrawEat:

	fn_image_eat = "./Images/Image 658.png"

	def __init__(self, pos):
		self.image = pygame.image.load(DrawEat.fn_image_eat).convert_alpha()
		self.pos = pos
		self.time = 0
		sound.SoundEffect.play("eat")

	def draw(self, surface):
		if self.time <= 0.5:
			surface.blit(self.image, self.pos)

	def update(self, time_passed):
		self.time += time_passed
		# if Eat.time > 0.2:
		# 	Eat.time = 0

class Eat:
	def __init__(self):
		self.e = None

	def eat(self, bg, player):
		for level in data.level_group.values():
			r = pygame.sprite.spritecollideany(player, level, tools.collide_rect)
			if r != None:
				self.e = DrawEat(player.pos)
				if r.level > player.level:
					player.kill()
				else:
					player.add_score(r.level)
					r.kill()

		r = pygame.sprite.groupcollide(data.level0, data.level2, True, False, tools.collide_rect)
		if r != None:
			for i in r:
				i.kill()
				self.e = DrawEat(i.pos+bg.bg_position)

		r = pygame.sprite.groupcollide(data.level0, data.level4, True, False, tools.collide_rect)
		if r != None:
			for i in r:
				i.kill()
				self.e = DrawEat(i.pos+bg.bg_position)

		r = pygame.sprite.groupcollide(data.level2, data.level4, True, False, tools.collide_rect)
		if r != None:
			for i in r:
				i.kill()
				self.e = DrawEat(i.pos+bg.bg_position)

