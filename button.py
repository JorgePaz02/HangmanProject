import pygame
win = pygame.display.set_mode((500,500))
win.fill((255,255,255))
class button():
  def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
  def draw(self,win,outline=None):
    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

    if self.text != '':
      font = pygame.font.SysFont('comicsans', 25)
      text = font.render(self.text, 1, (0,0,0))
      win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


  def isOver(self, pos):
  #Pos is the mouse position or a tuple of (x,y) coordinates
    if pos[0] > self.x and pos[0] < self.x + self.width:
      if pos[1] > self.y and pos[1] < self.y + self.height:
       return True
            
    return False
