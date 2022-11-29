import pygame
import sys
import button
from pygame.locals import *
from hangman import *
from draw import*
#width and height variables
WIDTH, HEIGHT = 575, 600
#variable that stored the width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#creating and displaying the name of our game
pygame.display.set_caption("Hangman game!")
#variable that holds the color
BLACK = (255, 0, 0)
#variable that holds the color white
WHITE = (255, 255, 255)
#variable that will hold elemnts of the border
BORDER = pygame.Rect(HEIGHT, 0, 10, WIDTH)
#frame per second
FPS = 960
#velocity
VEL = 1
#uploading the background image
CORN_IMAGE = pygame.image.load("scary_image.jpg")
#creating the size of the image
CORN_IMAGE = pygame.transform.scale(CORN_IMAGE, (525, 300))

pygame.init()

#function that draws the window
    #fill in the window with the color white
    #pasting the image
WIN.blit(CORN_IMAGE, (0, 0))
    #draw the rectangle
pygame.draw.rect(WIN, BLACK, BORDER)
    #display the whole rectangle
pygame.display.update()

#begin the main function
def main():
  gamestart()
  
  clock = pygame.time.Clock()
  flag = True
  while flag:
    
    clock.tick(FPS)
    for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  flag = False
  
  keys_pressed = pygame.key.get_pressed()
  pygame.quit()
  draw_window()
  start_button.draw()
  
  pygame.quit()

if __name__ == "__main__":
  main()
  
