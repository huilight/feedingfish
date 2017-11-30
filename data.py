import pygame

SCREEN_SIZE = (800,550)

score = 0

level1_score = 300
level2_score = 800
level3_score = 2000

level0 = pygame.sprite.Group()
level2 = pygame.sprite.Group()
level4 = pygame.sprite.Group()
level_group = {"0":level0, "2":level2, "4":level4}

level0_fish_num = 10
level2_fish_num = 0
level4_fish_num = 0
fish_num = {"0":level0_fish_num, \
			"2":level2_fish_num, \
			"4":level4_fish_num}