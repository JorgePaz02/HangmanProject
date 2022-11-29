import pygame
from draw import*
from button import*
import sys
import os
import random
import main

pygame.font.init()
font = pygame.font.Font("Sono.ttf", 20)
WHITE= (255,255,255,1)
BLACK=(0,0,0,0)
YELLOW= (0,255,255,0)
RED=(255,0,0,0)
head = BLACK
body = BLACK
leftarm = BLACK
rightarm = BLACK
leftleg = BLACK
rightleg = BLACK

START_WIDTH,START_HEIGHT = 100,80
#GLOBAL VARIABLES- OUR MAIN LISTS
word = []  #ORIGINAL WORD
answer = []  #FILLED WITH _ TILL GUESS CORRECT
screen = pygame.display.set_mode((400,400))
 
#this will draw the hangman and it gets passed the number of lives they have
def drawHMan(lives):
  screen.fill(BLACK)
  num = lives
  # lets make the post  a regulur button and not give it any action
  postbutton = button((WHITE), 90, 90, 15, 200, '')
  postbutton.draw(WIN)
  pobutton = button((WHITE), 90, 90, 100, 15, '')
  pobutton.draw(WIN)
  potbutton = button((WHITE), 50, 280, 150, 15, '')
  potbutton.draw(WIN)
  # end of drawing out the post 

  # lets draw an announcment 
  # guessbutton = button((RED), 250, 250, 205, 20, 'Enter your letter below:')
  # guessbutton.draw(WIN)

  life = font.render(str("Enter your letter below:"), False, WHITE)
  life_rect = life.get_rect()
  life_rect.center = (260,270)
  screen.blit(life, life_rect)
  # end of the announcement
  
#if they have wrong answers then change the color
  if num == 5:
  #display the head change the color
    global head
    head = RED
  elif num == 4:
  #display the body change the color
    global body
    body = RED
  elif num == 3:
  #display the right arm change the color
    global rightarm
    rightarm = RED
  elif num == 2:
  #display the left arm change the color
    global leftarm
    leftarm = RED
  elif num == 1:
  #display the left leg change the color
    global leftleg
    leftleg = RED
  elif num == 0:
  #display the right leg change the color
    global rightleg
    rightleg = RED

    
  #lets begin drawing the figure initalize them all to black
  # the head
  headx = pygame.draw.circle(screen, (head), (195, 130), 17, 3)
  # the body
  bodyx = pygame.draw.line(screen, (body), (195, 220), (195,145), 3)
  # the right arm
  rightarmx = pygame.draw.line(screen, (rightarm), (195, 160), (230,195), 3)
  # the left arm
  leftarmx = pygame.draw.line(screen, (leftarm), (195,160),(160, 195), 3)
  # the left leg
  leftlegx = pygame.draw.line(screen, (leftleg), (195, 222), (160,250), 3)
  # the right leg
  rightlegx = pygame.draw.line(screen, (rightleg), (195, 222), (230,250),3)
  #end of drawing the body

  pygame.display.update()

#BEGINS THE GAME
def gamestart(): 
  start = pygame.Rect(50,50,START_WIDTH,START_HEIGHT)
  draw_start(start)
  pygame.display.update()
  choice = input("wanna play? ")
  if choice == 'Y':
        difficulty()
  else:
    screen.fill(BLACK)
    #button for playing the game again
    playbutton = button((WHITE), 250, 250, 400, 30, 'LETS TRY THAT AGAIN! WANNA PLAY?! CLICK HERE!')
    playbutton.draw(WIN)
    #what to do when the button is clicked below
    run = True
    while run:
      pygame.display.update()
      for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
    
        if event.type == pygame.QUIT:
          run =False
          pygame.quit()
          quit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
          if playbutton.isOver(pos):
            gamestart()
            
 #SETS UP THE WORD FOR THE GAME. MAY BE UPDATED WITH RANDOMIZER
def wordset(fileName): 
    list = readfile(fileName)
    #generate a random selection from txt file
    randWord = random.choice(list)
    #add letters of the random word into word array to store answer, skipping spaces
    for item in randWord:
        if (item == " "):
            continue
        else:
            word.append(item)
            answer.append('_')
 
    #lets draw the spaces that we need for the word
    gamebegin(word)
    statement2 = font.render(i*' _ ', True, WHITE)
    statement2_rect = statement2.get_rect()
    statement2_rect.center = (450,300)
    screen.blit(statement2, statement2_rect)
  


'''
#this is previous wordset function
for item in list[0]:
    word.insert(i, item)
    i= i+1
  i=0
  for item in word:
    answer.insert(i, '_')
    i= i+1
'''
#EASY CATEGORIES
def easyClick():
  # this is a test
  # print ("we have enterd this new section")
  
  screen.fill(BLACK)
  statement2 = font.render("Please pick a category: ", True, WHITE)
  statement2_rect = statement2.get_rect()
  statement2_rect.center = (250,200)
  screen.blit(statement2, statement2_rect)

  statement = font.render("food, transportation, or colors ", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (250,220)
  screen.blit(statement, statement_rect)
  
# buttons for the categories
  #button for food
  foodbutton = button((WHITE), 90, 250, 100, 30, 'food')
  foodbutton.draw(WIN)

  #button for transportation
  transbutton = button((WHITE), 250, 250, 100, 30, 'transport')
  transbutton.draw(WIN)

  #button for colors
  colbutton = button((WHITE), 400, 250, 100, 30, 'colors')
  colbutton.draw(WIN)
# end of buttons
# button actions
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  
      if event.type == pygame.MOUSEBUTTONDOWN:
        if foodbutton.isOver(pos):
          wordset('WordLists/Easy/FoodEasy.txt')
        elif transbutton.isOver(pos):
          wordset('WordLists/Easy/TransportationMethodsEasy.txt')
        elif colbutton.isOver(pos):
          wordset('WordLists/Easy/ColorsEasy.txt')
# end of actions
          
  pygame.display.update()

    
#MEDIUM CATEGORIES
def medClick():

  screen.fill(BLACK)
  statement2 = font.render("Please pick a category: ", True, WHITE)
  statement2_rect = statement2.get_rect()
  statement2_rect.center = (250,200)
  screen.blit(statement2, statement2_rect)

  statement = font.render("food, colors, or clothing ", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (250,220)
  screen.blit(statement, statement_rect)
  
# buttons for the categories
  #button for food
  foodbutton = button((WHITE), 90, 250, 100, 30, 'food')
  foodbutton.draw(WIN)

  #button for color
  colbutton = button((WHITE), 250, 250, 100, 30, 'color')
  colbutton.draw(WIN)

  #button for clothing
  clothbutton = button((WHITE), 400, 250, 100, 30, 'cloth')
  clothbutton.draw(WIN)
# end of buttons
  
# button actions
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  
      if event.type == pygame.MOUSEBUTTONDOWN:
        if foodbutton.isOver(pos):
          wordset('WordLists/Medium/FoodMedium.txt')
        elif colbutton.isOver(pos):
          wordset('WordLists/Medium/ColorsMedium.txt')
        elif clothbutton.isOver(pos):
          wordset('WordLists/Medium/ClothingMedium.txt')
# end of actions
          
  pygame.display.update()

#HARD CATEGORIES
def hardClick():
  
  screen.fill(BLACK)
  statement2 = font.render("Please pick a category: ", True, WHITE)
  statement2_rect = statement2.get_rect()
  statement2_rect.center = (250,200)
  screen.blit(statement2, statement2_rect)

  statement = font.render("food or colors", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (250,220)
  screen.blit(statement, statement_rect)
  
#buttons for the categories
  #button for food
  foodbutton = button((WHITE), 90, 250, 100, 30, 'food')
  foodbutton.draw(WIN)

  #button for colors
  colbutton = button((WHITE), 250, 250, 100, 30, 'colors')
  colbutton.draw(WIN)
# end of buttons

# button actions
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  
      if event.type == pygame.MOUSEBUTTONDOWN:
        if foodbutton.isOver(pos):
          wordset('WordLists/Hard/FoodHard.txt')
        elif colbutton.isOver(pos):
          wordset('WordLists/Hard/ColorsHard.txt')
# end of actions 
          
  pygame.display.update()

#END of the dicciculty levels

# here is the class that lets them select their difficulty
def difficulty():
  screen.fill(BLACK)
  statement = font.render("What level of difficulty will you like? ", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (300,80)
  screen.blit(statement, statement_rect)
 
  statement2 = font.render("E for easy, M for medium, H for hard ", True, WHITE)
  statement2_rect = statement2.get_rect()
  statement2_rect.center = (300,150)
  screen.blit(statement2, statement2_rect)

  #button for easy
  easybutton = button((WHITE), 90, 250, 100, 30, 'E')
  easybutton.draw(WIN)

  #button for medium
  medbutton = button((WHITE), 250, 250, 100, 30, 'M')
  medbutton.draw(WIN)

  #button for hard
  hardbutton = button((WHITE), 400, 250, 100, 30, 'H')
  hardbutton.draw(WIN)

  #what to do when the button is clicked below
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  # if the button is clicked then do these functions 
      if event.type == pygame.MOUSEBUTTONDOWN:
        if easybutton.isOver(pos):
          easyClick()
        elif medbutton.isOver(pos):
          medClick()
        elif hardbutton.isOver(pos):
          hardClick()

  pygame.display.update()

#READS FILE AND RETURNS LIST OF ALL WORDS
def readfile(filename):  
    with open(filename, 'r') as f:
        myText = f.read().splitlines()

    return myText

#CHECKS GUESS FROM USER
def xcheck(x,word): 
  #Goes through array to find guess in chosen word if the letter is in there return 0
    for item in word:  
      if x == item:
        return 0

# this function displays the letters youve already used
def letter(list):
  # this is a test
  # print("The list after appending is : " + str(list))
  letterbutton = button((WHITE), 50, 10, 500, 30, "used letters" + str(list))
  letterbutton.draw(WIN)

  pygame.display.update()

#MAIN GAME LOOP
def gamebegin(word):  
    lives = 6
  # this holds the word that were playing with
    w = word
  # draw your hangman
    drawHMan(lives)
  # display your lives
    texts(str(lives))
  # list that holds all letters guessed
    guess_list = []
  # lets create a set that will add in the correct letters
    xset = set()
  # create a set that has all the letters of the word
    wset = set()
    for i in w:
      wset.add(i)
    # this is a test
    # print(f"this is the word set{wset}")
  # while we still have lives
    run = True
    while run:
      texts(str(lives))
      x = text()
      # variable to add to the list
      newx = x
      # appedning to the list
      guess_list  += newx
      # if you get the letter correct
      if xcheck(x,w) == 0:   
         # you got a letter correct so add it the set 
          xset.add(x)
          fillup(x)
        # test
          # print ("you got the letter correct")
          # print (xset)
      # if the letter is not in the word then take a life away
      elif not xcheck(x,w) == 0:
        lives = lives - 1
        drawHMan(lives)
        fillup(x)
        if lives == 0:
          run = False
      # printing out the letters that have already been used
      letter(guess_list) 

      if wincheck(xset,wset) == 0:
        winEndgame()
          # break
    Gameover()

# this displays the lives that you have on the screen
def texts(lives):
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 20)
  # text = font.render(str(answer), False, WHITE)
  # text_rect = text.get_rect()
  # text_rect.center = (220,200)
  life = font.render(str("Lives left:"+lives), False, WHITE)
  life_rect = life.get_rect()
  life_rect.center = (160,80)

  screen.blit(life, life_rect)
  pygame.display.update()


def Gameover():
  screen.fill(BLACK)
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 50)
  text = font.render("GAME OVER YOU RAN OUT OF LIVES!", True, RED)
  text_rect = text.get_rect()
  text_rect.center = (200,200)
  screen.blit(text, text_rect)
  #button for playing the game again
  playbutton = button((WHITE), 250, 250, 300, 30, 'WANNA PLAY AGAIN? CLICK HERE')
  playbutton.draw(WIN)
  #what to do when the button is clicked below
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  # if the button is clicked then do these functions 
      if event.type == pygame.MOUSEBUTTONDOWN:
        if playbutton.isOver(pos):
          gamestart()
  pygame.quit

# this checks if you win the game
def wincheck(set, wset):
  # if you guess all the letters then you win
  if len(set) == len(wset):
    return 0
  else:
    return 1

# if you win the game
def winEndgame():
  screen.fill(BLACK)
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 50)
  text = font.render("WINNER", True, YELLOW)
  text_rect = text.get_rect()
  text_rect.center = (200,200)
  screen.blit(text, text_rect)
  pygame.display.update()
  #button for playing the game again
  playbutton = button((WHITE), 250, 250, 300, 30, 'WANNA PLAY AGAIN? CLICK HERE!')
  playbutton.draw(WIN)

   #what to do when the button is clicked below
  run = True
  while run:
    pygame.display.update()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
  
      if event.type == pygame.QUIT:
        run =False
        pygame.quit()
        quit()
  # if the button is clicked then do these functions 
      if event.type == pygame.MOUSEBUTTONDOWN:
        if playbutton.isOver(pos):
          gamestart()
        
  pygame.quit

# this allows for user input of their guess
def text():
  clock = pygame.time.Clock()
# it will display on screen 
# basic font for user typed
  base_font = pygame.font.Font("Sono.ttf", 32)

# create rectangle
  input_rect = pygame.Rect(250, 300, 100, 32)
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
  color_active = pygame.Color(RED)
# color_passive store color(chartreuse4) which is
# color of input box.
  color_passive = pygame.Color(WHITE)
  color = color_passive
  active = False
  user_text = ''
  while True:
      for event in pygame.event.get():
      # if user types QUIT then the screen will close
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
          if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False  
          if event.type == pygame.KEYDOWN:  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:  
                user_text = user_text[:-1] 
            elif event.key == pygame.K_RETURN:
              return user_text
            else:
                user_text += event.unicode   

            
      if active:
        color = color_active
      else:
        color = color_passive          
      pygame.draw.rect(screen, color, input_rect)
      text_surface = base_font.render(user_text, True, (255, 255, 255))
      screen.blit(text_surface, (input_rect.x, input_rect.y))
      input_rect.w = max(100, text_surface.get_width()+10)
      pygame.display.flip()
      clock.tick(60)

def fillup(x):
    e = 0
    for item in word:  #Goes through array to find guess in chosen word
        if x == item:
            answer[e] = item

        e = e + 1
    pygame.font.init()
    font = pygame.font.Font("Sono.ttf", 15)
    text = font.render(str(answer), False, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (250,60)
    screen.blit(text, text_rect)
    pygame.display.update()
   
