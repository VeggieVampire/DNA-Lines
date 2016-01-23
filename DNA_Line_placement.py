import pygame
import pygame.image
import sys
import os
from pygame.locals import *


pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

YELLOW = (255,255,0)
CYAN = (0,255,255)
PURPLE = (255,0,255)

#sets Frame rate
#FPS = 30
#fpsTime = pygame.time.Clock()

#set size of window
setDisplay = pygame.display.set_mode((1040, 780))
pygame.display.set_caption('DNA Lines')
#Set background colors
setDisplay.fill(BLACK)



singlePixil = pygame.PixelArray(setDisplay)

#building list from file
aList = [];

filename ='DNA.txt' 
f = open((filename),'r')
num_lines = sum(1 for line in (filename))

for i in range(num_lines):
	aList.append( f.readline() );
f.close()

imgx = 100
imgy = 100
imgx2 = 0
imgy2 = 0
for x in range(0, num_lines):
	for i in aList[x]:
    		if i == 'C':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 8
				imgy =  imgy + 0
				pygame.draw.line(setDisplay,GREEN,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'A':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 0
				imgy =  imgy + 4
				pygame.draw.line(setDisplay,YELLOW,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'T':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 4
				imgy =  imgy - 4
				pygame.draw.line(setDisplay,BLUE,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'G':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx - 4
				imgy =  imgy + 4
				pygame.draw.line(setDisplay,RED,(imgx2,imgy2),(imgx,imgy),5)
		print imgx
		print imgy
			#if imgx > 1040: 
			#	imgx = 100
			#if imgy > 750:
			#	imgy = 100	
bList = [];

filename ='DNA2.txt' 
f = open((filename),'r')
num_lines = sum(1 for line in (filename))

for i in range(num_lines):
	bList.append( f.readline() );
f.close()

imgx = 100
imgy = 100
imgx2 = 0
imgy2 = 0
for x in range(0, num_lines):
	for i in bList[x]:
    		if i == 'C':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 8
				imgy =  imgy + 0
				pygame.draw.line(setDisplay,GREEN,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'A':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 0
				imgy =  imgy + 4
				pygame.draw.line(setDisplay,YELLOW,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'T':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx + 4
				imgy =  imgy - 4
				pygame.draw.line(setDisplay,BLUE,(imgx2,imgy2),(imgx,imgy),5)
    		if i == 'G':
				imgx2 = imgx
				imgy2 = imgy
				imgx =  imgx - 4
				imgy =  imgy + 4
				pygame.draw.line(setDisplay,RED,(imgx2,imgy2),(imgx,imgy),5)
		print imgx
		print imgy

while True:
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()


