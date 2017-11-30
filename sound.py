import pygame, eat, data

class SoundControl:
	fn_sound_pad = "./images/ImageSoundControlPad.png"
	visible = False
	pos = pygame.math.Vector2(170, 160)
	
	@classmethod
	def draw_surface(cls, surface):
		sound_pad = pygame.image.load(SoundControl.fn_sound_pad).convert_alpha()
		surface.blit(sound_pad, SoundControl.pos)
		SoundControl.draw_state(surface, BgMusic)
		SoundControl.draw_state(surface, SoundEffect)
		SoundControl.draw_volume(surface, BgMusic)
		SoundControl.draw_volume(surface, SoundEffect)

	@classmethod
	def draw_state(cls, surface, obj):
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
						BgMusic.change_state()
						SoundControl.draw_state(surface, BgMusic)

					if pos[0] >= 347 and pos[1]>= 46 and \
					pos[0] <= 367 and pos[1] <= 66:
						SoundEffect.change_state()
						SoundControl.draw_state(surface, SoundEffect)

					if pos[0] >= 81 and pos[1]>= 81 and \
					pos[0] <= 224 and pos[1] <= 92:
						length = pos[0] - 81
						BgMusic.set_volume(length/143)
						SoundControl.draw_volume(surface, BgMusic)
						pygame.display.update()
						loop = True
						while loop:
							for event in pygame.event.get():
								if event.type == pygame.locals.MOUSEMOTION:
									length = event.pos[0] - SoundControl.pos[0] - 81
									print(length)
									if length >= 0 and length <= 143:
										BgMusic.set_volume(length/143)
										SoundControl.draw_volume(surface, BgMusic)
										pygame.display.update()
								if event.type == pygame.locals.MOUSEBUTTONUP:
									loop = False

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
	def change_state(cls):
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
	fn_sound_eat = "./Sounds/Sound 571.ogg" #eat
	def __init__(self):
		pass
		
	@classmethod
	def change_state(cls):
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
		pygame.mixer.music.set_volume(volume)

	@classmethod
	def get_volume(cls):
		return pygame.mixer.music.get_volume()

	@classmethod
	def play(cls, type):
		if not SoundEffect.sound_is_open:
			return

		if type == "eat":
			sound = pygame.mixer.Sound(SoundEffect.fn_sound_eat)

		sound.play()


if __name__ == '__main__':
	import time
	pygame.init()

	pygame.display.set_mode((320,320),0,32)
	# bg = BgMusic()
	pygame.mixer.music.load("Sounds/Sound 569.ogg")
	pygame.mixer.music.play(-1)
	time.sleep(5)