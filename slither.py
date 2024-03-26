import pygame
import sys
import random

pygame.init()
display_width = 2560#1366
display_height = 1387#768
# gameDisplay = pygame.display.set_mode((display_width, display_height))#,pygame.FULLSCREEN,32)
gameDisplay = pygame.display.set_mode((0, 0),pygame.RESIZABLE)
print(pygame.display.get_window_size())
display_width, display_height = pygame.display.get_window_size()


pygame.display.set_caption(' SLITHERING SNAKE ')
bg = pygame.image.load('bg4.1.png')
bg1 = pygame.image.load('bg3.1.png')
bg2 = pygame.image.load('bg2.1.png')
clock = pygame.time.Clock()
FPS = 15



#color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0,155)
green=(0,155,0)
blue=(0,0,255,100)

#function to QUIT  or  RESTART
def message_to_screen(text , color , size , y_displace = 0) :
      if size=='small' :
            font_size = 25
      elif size=='medium' :
            font_size = 50
      elif size=='large' :
            font_size = 80  
      textFont = pygame.font.Font('freesansbold.ttf' , font_size)
      textSurface = textFont.render(text ,True, color)
      textRect = textSurface.get_rect()
      textRect.center = (display_width/2) , (display_height/2) + y_displace
      gameDisplay.blit(textSurface ,  textRect)
      pygame.display.update()

#function for snake body & head
snake_img = pygame.image.load('snake_head_45.png')
snake_skin = pygame.image.load('snake_skin_45.png')
egg_img = pygame.image.load('chick1.png')

direction = 'right'

def snake(block_size , snakeList) :                                     #snake function body
      if direction == 'right' :
            head_img = pygame.transform.rotate(snake_img , 270)
      if direction == 'left' :
            head_img = pygame.transform.rotate(snake_img , 90)
      if direction == 'up' :
           head_img = snake_img
      if direction == 'down' :
            head_img = pygame.transform.rotate(snake_img , 180)

      gameDisplay.blit(head_img ,( snakeList[-1][0] , snakeList[-1][1]))
      for xNy in snakeList[:-1] :
            gameDisplay.blit(snake_skin , (xNy[0] , xNy[1])) 

#function for score
def score(score):
      textFont = pygame.font.Font('freesansbold.ttf' , 30)
      textSurface = textFont.render(score ,True,white)
      gameDisplay.blit(textSurface ,  (0,0))
      pygame.display.update()


#pause function
def pause(points) :
      
      pause = True
      #gameDisplay.fill(black)
      gameDisplay.blit(bg2 , (0,0))
      score('Score : '+str(points))
      while  pause :
            for event in pygame.event.get():
                  if event.type==pygame.QUIT :
                        pygame.quit()
                        quit()

                  elif event.type==pygame.KEYDOWN :
                        if event.key==pygame.K_c:
                              pause = False

                        if event.key==pygame.K_q:
                              pygame.quit()
                              quit()

            message_to_screen('  Press C : continue  ;  Q : Quit' , green , 'medium' ,  100 )
            pygame.display.update()
            clock.tick(12)      
#Game Intro
def game_intro():

      intro = True
      #gameDisplay.fill(black)
      gameDisplay.blit(bg1 , (0,0))
      
      while  intro :
            for event in pygame.event.get():
                  if event.type==pygame.QUIT :
                        pygame.quit()
                        quit()

                  elif event.type==pygame.KEYDOWN :
                        if event.key==pygame.K_c:
                              intro = False

                        if event.key==pygame.K_q:
                              pygame.quit()
                              quit()
                              
                        
            
            message_to_screen(' Welcome To the Game  : ' ,red , 'medium',  -200 )
            message_to_screen('  SLITHERING SNAKE   ' , green , 'medium' ,  -130 )
            message_to_screen('  DO;S : ' , white , 'small' ,  -90 )
            message_to_screen(' Your the snake and the objective of the game is to eat eggs   ' , white ,'small' ,  -50 )
            message_to_screen('  the more you eat , longer you grow   ' , white , 'small' ,  0 )
            message_to_screen('  DONT;S  : ' , white , 'small' ,  90 )
            message_to_screen('  if you hit the boundaries or run over youself :::you die ' , red , 'small' ,  200 )
            message_to_screen('  press C : continue  ;  Q : Quit  ; P : pause' , blue , 'small' ,  250 )

            pygame.display.update()
            clock.tick(12)
      

#game_loop
def game_loop():

      global direction

      block_size  = 35
      apple_size = 40
      
      x = display_width/2
      y = display_height/2

      apple_x = round( random.randrange(0 , (display_width - block_size)))#/10.0)*10.0
      apple_y =  round(random.randrange(0, (display_height - block_size)))#/10.0)*10.0

      x_change = 0
      y_change = 0

      snakeList = []
      snakeLength=1
      

      gameExit = False
      gameOver = False
   
      while not gameExit :

            while gameOver == True :
                  message_to_screen('GAME OVER ' , red ,  'large' , y_displace = -50 )
                  message_to_screen('press - C : play again , Q  : Quit' , blue , 'medium' , 50)
                  
                  pygame.display.update()
                  
                  for event in pygame.event.get():

                        if event.type==pygame.QUIT :
                             pygame.quit()
                             quit()
                        
                        if event.type==pygame.KEYDOWN :
                              if event.key==pygame.K_q:
                                    pygame.quit()
                                    quit()                              
                                    
                              if event.key==pygame.K_c:
                                    game_loop()



                  
            for event in pygame.event.get():
                  if event.type==pygame.QUIT :
                        pygame.quit()
                        quit()

                  if event.type==pygame.KEYDOWN :
                        if event.key==pygame.K_LEFT:
                              x_change = -block_size/2
                              y_change = 0
                              direction = 'left'

                        if event.key==pygame.K_RIGHT:
                              x_change =  block_size/2
                              y_change = 0
                              direction = 'right'

                        if event.key==pygame.K_UP:
                              y_change = -block_size/2
                              x_change = 0
                              direction = 'up'

                        if event.key==pygame.K_DOWN:
                              y_change =  block_size/2
                              x_change = 0
                              direction = 'down'

                        if event.key==pygame.K_p:
                              pause(snakeLength - 1)


            if x < 0 or y<0 or (x+block_size) > display_width or (y+block_size) > display_height :
                  gameOver = True
                  

            x = x + x_change
            y = y + y_change

            snakeHead=[]
            snakeHead.append(x)
            snakeHead.append(y)
            snakeList.append(snakeHead)
            

            if len(snakeList) > snakeLength:
                  del snakeList[0]

            for eachSegment in snakeList[:-1] :                                                              #[:-1] analyzing element upto last element i.e exluding last element(snake head)
                  if snakeHead==eachSegment :
                        gameOver = True
          
            gameDisplay.fill( black)                                                                                                                                    #layer0
            gameDisplay.blit(bg , (0,0))
            #pygame.draw.rect(gameDisplay , red , (apple_x , apple_y , apple_size , apple_size))                 #displaying apple(before snake)_layer1
            gameDisplay.blit(egg_img , (apple_x, apple_y))
            snake( block_size , snakeList)                                                                                                            #displaying snake layer2
            score('Score : '+str(snakeLength - 1))
            

##            if ((x==apple_x) and (y==apple_y)):
##                  apple_x =round( random.randrange(0 , (display_width - block_size))/10.0)*10.0
##                  apple_y =  round(random.randrange(0, (display_height - block_size))/10.0)*10.0
##                  snakeLength+=1

            if (x>=apple_x) and x <=( apple_x+apple_size) or ((x+block_size)>=apple_x) and (x+block_size )<=( apple_x+apple_size):
                  if y>=apple_y and y<=(apple_y+apple_size) or (y+block_size)>=apple_y and (y+block_size)<=(apple_y+apple_size) :
                        apple_x =round( random.randrange(0 , (display_width - block_size)))#/10.0)*10.0
                        apple_y =  round(random.randrange(0, (display_height - block_size)))#/10.0)*10.0
                        snakeLength+=1                       
                  
                  
            
            clock.tick(FPS)
            pygame.display.update()           

game_intro()
game_loop()                        
pygame.quit()
quit()


      
 
