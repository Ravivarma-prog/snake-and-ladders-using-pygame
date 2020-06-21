import pygame,sys,os,time,random
from pygame.locals import *

pygame.init()


game_display=pygame.display.set_mode((500,400))
pygame.display.set_caption('snake and ladders')
screen=pygame.display.get_surface()
pygame.display.flip()
p1=pygame.image.load('player1.png')

def display_die():
    img=pygame.image.load('1.png')
    game_display.blit(img,(0,320))

def display_bg():
    pygame.draw.line(screen,(255,0,0),(90,0),(90,400))
    bg=pygame.image.load('bg.png')
    game_display.blit(bg,(100,0))
    

# def display_icon():
#     game_display.blit(p1,(110,370))

display_bg()
display_die()
# display_icon()

def draw_piece(x,y):
    game_display.blit(p1,(x,y))

def right(player_pos,x,y):
    #logic is mainly based on the total value in the dice a is for fitting x-coordinates and b for y
    a=(player_pos%10)-1
    b=(player_pos-1)//10
    if player_pos%10==0:
        #if the postion is divisible by ten then we fix the icon at the ends
        new_x=470
        new_y=y-(40*b)
    else:
        new_x=x+(40*a)
        new_y=y-(40*b)
    draw_piece(new_x,new_y)

def left(player_pos,x,y):
    a=(player_pos%10)-1
    b=(player_pos-1)//10
    if player_pos%10==0:
        new_x=110
        new_y=y-(40*b)
    else:
        new_x=x-(40*a)
        new_y=y-(40*b)
    draw_piece(new_x,new_y)
    

def movePiece(num,position):
    #logic is based on two types of traversal either right or left
    check=(position-1)//10
    if check%2==0:
        #this function is for right traversal for eg: 1->10,21->30,..
        right(position,110,370)
    if check%2!=0:
        #this is for left traversal for eg: 20<-11,40<-31,...
        left(position,470,370)        

#to display the text
def displayText():
    font=pygame.font.Font('freesansbold.ttf',20)
    text1=font.render('PRESS',True,(0,255,0),(0,0,255))
    textRect1=text1.get_rect()
    textRect1.center=(50,30)
    game_display.blit(text1,textRect1)

    text2=font.render('ENTER',True,(0,255,0),(0,0,255))
    textRect2=text2.get_rect()
    textRect2.center=(50,80)
    game_display.blit(text2,textRect2)

    text3=font.render('TO ROLL',True,(0,255,0),(0,0,255))
    textRect3=text3.get_rect()
    textRect3.center=(50,130)
    game_display.blit(text3,textRect3)

    text4=font.render('DIE',True,(0,255,0),(0,0,255))
    textRect4=text4.get_rect()
    textRect4.center=(50,180)
    game_display.blit(text4,textRect4)

def roll_die():
    
    val=random.randint(1,6)
    # print(val)
    if val==1:
        one=pygame.image.load('1.png')
        game_display.blit(one,(0,320))
    if val==2:
        two=pygame.image.load('2.png')
        game_display.blit(two,(0,320))
    if val==3:
        three=pygame.image.load('3.png')
        game_display.blit(three,(0,320))
    if val==4:
        four=pygame.image.load('4.png')
        game_display.blit(four,(0,320))
    if val==5:
        five=pygame.image.load('5.png')
        game_display.blit(five,(0,320))
    if val==6:
        six=pygame.image.load('6.png')
        game_display.blit(six,(0,320))
    return val

#to check if the postition has a ladder
def checkLadders(pos):
    new_pos=pos
    ch=False
    ladders={1:(190,250,38),4:(350,330,14),9:(470,250,31),21:(150,210,42),28:(230,50,84),51:(350,130,67),71:(470,10,91),80:(110,10,100)}
    print(ladders.keys())
    if pos in list(ladders.keys()):
        ch=True
        new_pos=ladders[pos][2]
        draw_piece(ladders[pos][0],ladders[pos][1])
    print(ch)
    return ch,new_pos

#for checking the snakes in the board
def checkSnake(pos):
    new_pos=pos
    ch=False
    snakes={17:(350,370,7),54:(350,250,34),62:(150,130,19),64:(110,170,60),87:(230,290,24),93:(390,90,73),95:(310,90,75),98:(150,90,79)}
    if pos in list(snakes.keys()):
        ch=True
        new_pos=snakes[pos][2]
        draw_piece(snakes[pos][0],snakes[pos][1])
    return ch,new_pos



def checkFinish(pos):
    if pos==100:
        font=pygame.font.Font('freesansbold.ttf',50)
        text=font.render('GAME FINISHED',True,(0,255,0),(0,0,255))
        textRect=text.get_rect()
        textRect.center=(250,250)
        game_display.blit(text,textRect)

total=0
while True:
    displayText()
    pygame.display.set_caption('snale and ladders')
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type==KEYDOWN:
            if event.key==K_RETURN:
                val=roll_die() #random rolling of dice
                total+=val
                display_bg()#to remove the previous occurence of the icon
               

                ret,new_val=checkLadders(total)

                if ret:
                    total=new_val

                check,snake_value=checkSnake(total)

                if check:
                    total=snake_value

                if total>100:
                    total=total-val
                    #if the total exceeds 100, then total should not be added instead we are retaining the position

                movePiece(val,total)#moves the piece


                checkFinish(total)
                print(total)
            elif event.key==K_ESCAPE:
                pygame.quit()
                sys.exit(0)
    pygame.display.update()
      