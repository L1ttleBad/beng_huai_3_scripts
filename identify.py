#coding=utf-8
from PIL import Image
from PIL import ImageGrab
import pytesseract 
import os
import time
import win32api
import win32con
import string
from random import random


def text_extract(im):
	im = ImageGrab.grab()
	return pytesseract.image_to_string(im.crop((700,365,900,410)),lang = 'chi_sim'), \
	pytesseract.image_to_string(im.crop((1300,850,1470,905)),lang = 'chi_sim'), \
	pytesseract.image_to_string(im.crop((700,830,900,900)),lang = 'chi_sim'), \
	pytesseract.image_to_string(im.crop((740,840,940,900)),lang = 'chi_sim'), \
	pytesseract.image_to_string(im.crop((1100,365,1300,410)),lang = 'chi_sim')

	
def key(idx):
	print "press " + str(idx)
	win32api.keybd_event(idx,0,0,0)
	time.sleep(0.25 + random()/2)
	win32api.keybd_event(idx,0,win32con.KEYEVENTF_KEYUP,0)

	
def key_quick(idx):
	for i in range(20):
		win32api.keybd_event(idx,0,0,0)
		time.sleep(0.1 + random()/15)
		win32api.keybd_event(idx,0,win32con.KEYEVENTF_KEYUP,0)	
		time.sleep(0.1 + random()/15)
	key(49)
	key(73)


	
im = ImageGrab.grab()
box = (0,0,1600,935)
im = im.crop(box)
w,h = im.size
s1, s2, s3, s4, s5 = text_extract(im)


state = 0
times = 10
time.sleep(5)
while times < 10 :
	while(s1 != '初级装备训练'.decode('utf-8')):
		time.sleep(1)
		key(88)
		time.sleep(0.5+random())
		s1, s2, s3, s4, s5 = text_extract(im)
	state = 1
	key(90) #z

	
	while(s2 != '协助匹配'.decode('utf-8')):
		time.sleep(1)
		s1, s2, s3, s4, s5 = text_extract(im)
		if(s1 == '初级装备训练'.decode('utf-8')):
			key(90)
	state = 2
	key(88) #x
	
	while(s3 != '准备'.decode('utf-8')) & (s3 != '开始'.decode('utf-8')):
		time.sleep(1)
		s1, s2, s3, s4, s5 = text_extract(im)
		#if(s2 == '协助匹配'.decode('utf-8')):
		#	key(88)	
			
			
	state = 3
	key(67) #c
	while(s3 == '准备'.decode('utf-8')) | (s3 == '开始'.decode('utf-8')):
		time.sleep(2)
		s1, s2, s3, s4, s5 = text_extract(im)
	
	time.sleep(25)
	while(s4 != '关闭'.decode('utf-8')):
		key_quick(74) #j
		key_quick(74) #j
		
		s1, s2, s3, s4, s5 = text_extract(im)
		if(s3 == '准备'.decode('utf-8')) | (s3 == '开始'.decode('utf-8')):
			key(67)
		
	state = 4
	key(67) #c
	
	
	time.sleep(2+random())
	
	# while(s5 != '确定'.decode('utf-8')):
		# print s5
		# time.sleep(1)
		# s1, s2, s3, s4, s5 = text_extract(im)
		# if(s4 == '关闭'.decode('utf-8')):
			# key(67)	
	key(88)
	time.sleep(2+random())
	state = 0
	times += 1

s1, s2, s3, s4, s5 = text_extract(im)


state = 0
times = 0
time.sleep(5)	
while times < 10 :
	while(s5 != '高级装备训练'.decode('utf-8')):
		time.sleep(1)
		key(88)
		time.sleep(0.5+random())
		s1, s2, s3, s4, s5 = text_extract(im)
	state = 1
	key(86) #z

	
	while(s2 != '协助匹配'.decode('utf-8')):
		time.sleep(1)
		s1, s2, s3, s4, s5 = text_extract(im)
		if(s5 == '高级装备训练'.decode('utf-8')):
			key(86)
	state = 2
	key(88) #x
	
	while(s3 != '准备'.decode('utf-8')) & (s3 != '开始'.decode('utf-8')):
		time.sleep(1)
		s1, s2, s3, s4, s5 = text_extract(im)
		#if(s2 == '协助匹配'.decode('utf-8')):
		#	key(88)	
			
			
	state = 3
	key(67) #c
	while(s3 == '准备'.decode('utf-8')) | (s3 == '开始'.decode('utf-8')):
		time.sleep(2)
		s1, s2, s3, s4, s5 = text_extract(im)
	
	time.sleep(25)
	while(s4 != '关闭'.decode('utf-8')):
		key_quick(74) #j


		
		s1, s2, s3, s4, s5 = text_extract(im)
		if(s3 == '准备'.decode('utf-8')) | (s3 == '开始'.decode('utf-8')):
			key(67)
		
	state = 4
	key(67) #c
	
	time.sleep(2+random())
	
	# while(s5 != '确定'.decode('utf-8')):
		# print s5
		# time.sleep(1)
		# s1, s2, s3, s4, s5 = text_extract(im)
		# if(s4 == '关闭'.decode('utf-8')):
			# key(67)	
	key(88)
	time.sleep(2+random())
	state = 0
	times += 1
#im.thumbnail((w/4,h/4))
#im.show()
#r,b,g = im.split()
#r.show()
#b.show()
#g.show()

#print "input anything to end program"
#raw_input()