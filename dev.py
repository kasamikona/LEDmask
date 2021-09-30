#! /usr/bin/env python

import pygame
import time
import math

windowwidth = 48 * 10
windowheight = 12 * 10
fps = 10
matrix = [[0 for col in range(48)] for row in range(12)]

logo1 = [ \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
	[2,2,2,2,0,0,0,2,2,0,0,2,2,0,0,0,2,2,2,0,0,0,2,0,2,2,2,2,0,2,0,2,0,2,2,2,0,0,2,2,0,0,0,2,2,2,2,2], \
	[2,2,2,0,1,1,1,0,0,1,1,0,0,1,1,1,0,2,0,1,1,1,0,1,0,0,2,0,1,0,1,0,1,0,2,0,1,1,0,0,1,1,1,0,2,2,2,2], \
	[2,2,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,1,0,2,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,2,2,2], \
	[2,2,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,2,2,2], \
	[2,2,2,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,2,2,2], \
	[2,2,2,2,0,0,0,2,2,0,2,2,2,0,2,2,0,2,0,0,0,2,2,0,2,2,0,2,0,2,0,2,2,0,2,2,0,2,2,2,0,2,2,0,2,2,2,2], \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], \
]

logo2 = [ \
	[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0], \
	[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0], \
	[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0], \
	[0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0], \
	[0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0], \
	[0,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0], \
	[0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0], \
	[0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0], \
	[0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0], \
	[0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,0,0], \
	[0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0], \
	[0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,1], \
	[0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1], \
	[0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0], \
	[1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0], \
	[1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0], \
	[1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,0], \
	[0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0], \
	[0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0], \
	[0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0], \
	[0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0], \
	[0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0], \
	[0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0], \
	[0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0], \
	[1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0], \
	[1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
	[0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
]

screen = pygame.Surface((48, 12), pygame.SRCALPHA, 32)
window = pygame.display.set_mode((windowwidth, windowheight), pygame.NOFRAME)
pygame.display.set_caption("LED dev app")
pygame.mouse.set_visible(False)

running = True

startDate = time.time()
curTime = startDate
frame = 0
drawFrame = True

######################
### EFFECTS START HERE
######################

def testEffect(curTime, frame):
	x = frame % 48
	y = int(math.sin(curTime) * 6 + 6)
	matrix[y][x] = 1

def drawLogo1(curTime, frame):
	for x in range(48):
		for y in range(12):
			if logo1[y][x] == 0 or logo1[y][x] == 1:
				matrix[y][x] = logo1[y][x]

def drawLogo2(curTime, frame):
	if frame > 20:
		for x in range(48):
			for y in range(12):
				offset = int((frame - 32) + y)
				if offset >= 0 and offset < 32:
					matrix[y][x] = logo2[offset][x]

def fadeScanlines(curTime, frame, startFrame):
	if startFrame <= frame:
		for x in range(48):
			for y in range(12):
				if y % 2 == 1:
					if x < (frame - startFrame) * 2:
						matrix[y][x] = 0
				else:
					if (47 - x) < (frame - startFrame) * 2:
						matrix[y][x] = 0

rotozoomerAtans = [[0 for col in range(96)] for row in range(24)]
def preloadRotozoomer():
	for x in range(96):
		for y in range(24):
			rotozoomerAtans[y - 12][x - 48] = math.atan2(y, x)

def drawDizzyCircleTiles(curTime, frame):
	angle = frame / 15
	for x in range(48):
		for y in range(12):
			xOffset = x - 24
			yOffset = y - 6
			trigParam = rotozoomerAtans[yOffset][xOffset] + angle
			hypoParam = math.sqrt(yOffset * yOffset + xOffset * xOffset)
			mappedY = round((math.sin(trigParam) * hypoParam) * math.sin(frame / 50))
			mappedX = round((math.cos(trigParam) * hypoParam) * math.sin(frame / 50))
			matrix[y][x] = (mappedX % 8 < 4) ^ (mappedY % 8 >= 4)

def drawRotozoomer(curTime, frame):
	angle = frame / 15
	for x in range(48):
		for y in range(12):
			xOffset = x - 24
			yOffset = y - 6
			trigParam = math.atan2(yOffset, xOffset) + angle
			hypoParam = math.sqrt(yOffset * yOffset + xOffset * xOffset)
			mappedY = round((math.sin(trigParam) * hypoParam) * math.sin(frame / 50))
			mappedX = round((math.cos(trigParam) * hypoParam) * math.sin(frame / 50))
			matrix[y][x] = (mappedX % 8 < 4) ^ (mappedY % 8 >= 4)

####################
### EFFECTS END HERE
####################

def drawMatrix():
	for x in range(48):
		for y in range(12):
			if matrix[y][x] == 1:
				pygame.draw.polygon(screen, (255, 255, 255), ((x, y), (x, y), (x, y), (x, y)))

while running:
	keys = pygame.key.get_pressed()
	event = pygame.event.poll()
	if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
		running = False

	newTime = time.time()
	curFrame = math.floor((newTime - startDate) * fps)
	if curFrame > frame:
		matrix = [[0 for col in range(48)] for row in range(12)]
		screen.fill((0, 0, 0))
		curTime = newTime
		frame = curFrame
		drawFrame = True

	if drawFrame:
		pygame.display.set_caption("LED dev -- frame " + str(frame))

		# drawLogo2(curTime, frame)
		# drawLogo1(curTime, frame)
		# fadeScanlines(curTime, frame, 64)

		preloadRotozoomer()
		# drawRotozoomer(curTime, frame)
		drawDizzyCircleTiles(curTime, frame)

		drawMatrix()
		drawFrame = False

	resized_screen = pygame.transform.scale(screen, (windowwidth, windowheight))
	window.blit(resized_screen, (0, 0))
	pygame.display.flip()

