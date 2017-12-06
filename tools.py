import data

def collide_rect(sprite1, sprite2):
	"""接收两个精灵作为参数，检测是否碰撞"""
	if sprite1.rect[0]+6<sprite2.rect[0] and \
	   sprite2.rect[0]<sprite1.rect[2]-6 and \
	   sprite1.rect[1]+6<sprite2.rect[1] and \
	   sprite2.rect[1]<sprite1.rect[3]-6:
		return True
	if sprite1.rect[0]+6<sprite2.rect[0] and \
	   sprite2.rect[0]<sprite1.rect[2]-6 and \
	   sprite1.rect[1]+6<sprite2.rect[3] and \
	   sprite2.rect[3]<sprite1.rect[3]-6:
		return True
	if sprite1.rect[0]+6<sprite2.rect[2] and \
	   sprite2.rect[2]<sprite1.rect[2]-6 and \
	   sprite1.rect[1]+6<sprite2.rect[1] and \
	   sprite2.rect[1]<sprite1.rect[3]-6:
		return True
	if sprite1.rect[0]+6<sprite2.rect[2] and \
	   sprite2.rect[2]<sprite1.rect[2]-6 and \
	   sprite1.rect[1]+6<sprite2.rect[3] and \
	   sprite2.rect[3]<sprite1.rect[3]-6:
		return True
	return False

def hard_choose():
	if data.hard_level == 1:
		data.level0_fish_num = 20
		data.level2_fish_num = 2
		data.level4_fish_num = 1
	elif data.hard_level == 2:
		data.level0_fish_num = 15
		data.level2_fish_num = 3
		data.level4_fish_num = 2
	else:
		data.level0_fish_num = 10
		data.level2_fish_num = 4
		data.level4_fish_num = 3

	data.fish_num = {"0":data.level0_fish_num, \
			"2":data.level2_fish_num, \
			"4":data.level4_fish_num}