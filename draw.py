import pygame
# import sys
# import os
# import random
WIDTH,HEIGHT=575,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = (255,0,0)
WHITE = (255,255,255)
BORDER = pygame.Rect(HEIGHT, 0, 10,WIDTH)
FPS = 60
VEL = 1
SCARY_IMAGE = pygame.image.load('scary_image.jpg')
START_IMAGE = pygame.image.load("c.PNG")
START_WIDTH,START_HEIGHT = 200,100
SCARY_IMAGE = pygame.transform.scale(SCARY_IMAGE,(570,550))
START_IMAGE = pygame.transform.scale(START_IMAGE,(START_WIDTH,START_HEIGHT))


def draw_start(start):
  WIN.fill(WHITE)
  WIN.blit(SCARY_IMAGE,(0,0))
  pygame.draw.rect(WIN,BLACK,BORDER)
  WIN.blit(START_IMAGE,(180,150))
  #400,200
  pygame.display.update()