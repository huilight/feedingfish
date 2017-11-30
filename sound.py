import pygame, eat, data

class SoundControl:
	fn_sound_pad = "./images/ImageSoundControlPad.png"
	visible = False
	pos = pygame.math.Vector2(170, 160)
	
	@classmethod
	def draw_surface(cls, surface):
		sound_pad = pygame.image.load(SoundControl.fn_sound_pad).convert_alpha()
		surface.blit(sound_pad, SoundControl.pos)
		SoundControl.draw_status(surface, BgMusic)
		SoundControl.draw_status(surface, SoundEffect)
		SoundControl.draw_volume(surface, BgMusic)
		SoundControl.draw_volume(surface, SoundEffect)

	@classmethod
	def draw_status(cls, surface, obj):
		if obj.sound_is_open:
			color = (0, 0, 255)
		else:
			color = (255,255,255)
		pygame.draw.rect(surface, color,\
			pygame.locals.Rect(SoundControl.pos+obj.pos,(21,21)))

	@classmethod
	def draw_volume(cls, surface, obj):
		pygame.draw.rect(surface, (255,255,255),\
			pygame.locals.Rect(SoundControl.pos+obj.volume_pos,(143,12)))
		vol_length = obj.get_volume()*143
		pygame.draw.rect(surface, (0,0,255),\
			pygame.locals.Rect(SoundControl.pos+obj.volume_pos,(vol_length,12)))
	
	@classmethod
	def change_volume(cls, surface, sound, pos, base_num):
		length = pos - base_num
		sound.set_volume(length/143)
		SoundControl.draw_volume(surface, sound)
		while True:
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.locals.MOUSEMOTION:
					length = event.pos[0] - SoundControl.pos[0] - base_num
					if length <= 0:
						sound.set_volume(0)
					elif length >= 143:
						sound.set_volume(1)
					else:	
						sound.set_volume(length/143)
					SoundControl.draw_volume(surface, sound)
				if event.type == pygame.locals.MOUSEBUTTONUP:
					return

	@classmethod
	def open(cls, surface):
		sound_pad = SoundControl.draw_surface(surface)
		pygame.display.update()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					exit()
				if event.type == pygame.locals.MOUSEBUTTONDOWN:

					pos = event.pos-SoundControl.pos
					if pos[0] >= 95 and pos[1]>= 46 and \
					pos[0] <= 115 and pos[1] <= 66:
						BgMusic.change_status()
						SoundControl.draw_status(surface, BgMusic)

					if pos[0] >= 347 and pos[1]>= 46 and \
					pos[0] <= 367 and pos[1] <= 66:
						SoundEffect.change_status()
						SoundControl.draw_status(surface, SoundEffect)

					if pos[0] >= 81 and pos[1]>= 81 and \
					pos[0] <= 224 and pos[1] <= 92:
						SoundControl.change_volume(surface, BgMusic, pos[0], 81)

					if pos[0] >= 333 and pos[1]>= 81 and \
					pos[0] <= 475 and pos[1] <= 92:
						SoundControl.change_volume(surface, SoundEffect, pos[0], 333)

					if pos[0] >= 196 and pos[1]>= 134 and \
					pos[0] <= 304 and pos[1] <= 164:
						SoundControl.visible = False
						return

				if event.type == pygame.locals.KEYDOWN:
					if event.key == pygame.locals.K_ESCAPE:
						SoundControl.visible = False
						return
			pygame.display.update()
		clock.tick()

class Sound:

	volume = 0.5

	def __init__(self):
		pass

	def open(self):
		pass

	def close(self):
		pass

	@classmethod
	def set_volume(cls, volume):
		cls.volume = volume

class BgMusic(Sound):
	fn_bgmusic = "Sounds/Sound 569.ogg"
	sound_is_open = True
	pos = (95, 46)
	volume_pos = (81, 81)
	def __init__(self):
		pygame.mixer.music.load("Sounds/Sound 569.ogg")
		pygame.mixer.music.play(-1)

	@classmethod
	def change_status(cls):
		if BgMusic.sound_is_open:
			BgMusic.close()
		else:
			BgMusic.open()

	@classmethod
	def open(cls):
		BgMusic.sound_is_open = True
		pygame.mixer.music.play(-1)

	@classmethod
	def close(cls):
		BgMusic.sound_is_open = False
		pygame.mixer.music.stop()

	@classmethod
	def set_volume(cls, volume):
		pygame.mixer.music.set_volume(volume)

	@classmethod
	def get_volume(cls):
		return pygame.mixer.music.get_volume()

class SoundEffect(Sound):
	pos = (347,46)
	volume_pos = (333, 81)
	sound_is_open = True
	sound_volume = 1
	fn_sound_eat = "./Sounds/Sound 571.ogg" #eat

	def __init__(self):
		pass
		
	@classmethod
	def change_status(cls):
		if SoundEffect.sound_is_open:
			SoundEffect.close()
		else:
			SoundEffect.open()

	@classmethod
	def open(cls):
		SoundEffect.sound_is_open = True
	
	@classmethod
	def close(cls):
		SoundEffect.sound_is_open = False

	@classmethod
	def set_volume(cls, volume):
		SoundEffect.sound_volume = volume

	@classmethod
	def get_volume(cls):
		return SoundEffect.sound_volume

	@classmethod
	def play(cls, type):
		if not SoundEffect.sound_is_open:
			return

		if type == "eat":
			sound = pygame.mixer.Sound(SoundEffect.fn_sound_eat)

		sound.set_volume(SoundEffect.sound_volume)
		sound.play()


if __name__ == '__main__':
	import time
	pygame.init()

	pygame.display.set_mode((320,320),0,32)
	# bg = BgMusic()
	pygame.mixer.music.load("Sounds/Sound 569.ogg")
	pygame.mixer.music.play(-1)
	time.sleep(5)