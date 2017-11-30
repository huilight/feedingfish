import pygame

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