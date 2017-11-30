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

	@classmethod
	def get_num(cls, level):
		return len(data.level_group[str(level)])


class CreateFish:
	@classmethod
	def level2imgid(cls, level):
		"""根据等级得到起始图像文件名"""
		if level == 0:
			return 193
		elif level == 2:
			return 245
		else:
			return 131

	@classmethod
	def get_x(cls):
		"""得到出生横坐标"""
		if randint(0,1):
			return -1  #出生在屏幕左侧
		else:
			return 900 #出生在右侧

	@classmethod
	def get_fish(cls, level, num=1):
		"""生成一个鱼"""
		for i in range(num):
			f1 = Fishes(Vector2(CreateFish.get_x(), randint(0,550)),level, \
				CreateFish.level2imgid(level))
			f1.add(data.level_group[str(level)])