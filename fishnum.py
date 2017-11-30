import data
from fishes import Fishes
from pygame.math import Vector2
from random import randint

class ControlFishNum:

	@classmethod
	def update(cls):
		for i in range(0,5,2):
			num =  data.fish_num[str(i)]- CheckFishNum.get_num(i)
			if num != 0:
				CreateFish.get_fish(i, 1)

class CheckFishNum:
	# num = {"0":0,"2":0,"4":0}

	# @classmethod
	# def add_num(cls, level, num=1):
	# 	CreateFishNum.num[level] += num

	# @classmethod
	# def sub_num(cls, level, num=1):
	# 	CreateFishNum.num[level] -= num

	@classmethod
	def get_num(cls, level):
		return len(data.level_group[str(level)])


class CreateFish:
	@classmethod
	def level2imgid(cls, level):
			if level == 0:
				return 193
			elif level == 2:
				return 245
			else:
				return 131

	@classmethod
	def get_x(cls, ch):
		if ch==0:
			return -1
		else:
			return 800

	@classmethod
	def get_fish(cls, level, num=1):
		for i in range(num):
			f1 = Fishes(Vector2(CreateFish.get_x(randint(-1,0)), randint(0,550)),level, \
				CreateFish.level2imgid(level))
			f1.add(data.level_group[str(level)])