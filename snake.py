#code part1
import pygame,sys,os
import time 
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)


window_width=800
window_height=600
gamedisplay=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("snake prod")
font=pygame.font.SysFont(None,25,bold=True)

def myquit():
    pygame.quit()
    sys.exit(0)
    
#code part 2

clock = pygame.time.Clock()
FPS=5
blocksize=20
nopixel=0

#code part 3

def snake(blocksize,snakelist):
    for size in snakelist:
        pygame.draw.rect(gamedisplay,black,[size[0]+5,size[1],blocksize])
    
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gamedisplay.blit(screen_text,[window_width/2,window_height/2])
    

#code part4

def gameloop():
    gameexit=False
    gameover=False
    
    
    leadx=window_width/2
    leady=window_height/2
    
    changepixelsofx=0
    changepixelsofy=0
    
    snakelist=[]
    snakelength=1
    
    randomapplex=round(random.randrange(0,window_width-blocksize)/10.0)*10.0
    randomappley=round(random.randrange(0,window_height-blocksize)/10.0)*10.0
    
    #entering to the game
    
    while not gameexit:
        
        while gameoverc==True:
            gamedisplay.fill(white)
            message_to_screen("kalichath mathi mwoonose game over press c to play again")
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover=False
                    gameexit=True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    if event.key==pygame.K_c:
                        gameloop()
                
                
#logic1
    
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
            gameexit=True
            
            
            
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_ESCAPE:
            myquit()
            
        leftarrow=event.key==pygame.K_LEFT
        rightarrow=event.key==pygame.K_RIGHT       
        uparrow=event.key==pygame.K_UP
        downartow=event.key==pygame.K_DOWN
        
        if leftarrow:
            changepixelsofx=-blocksize
            changepixelsofy=nopixel  
        elif rightarrow:
            changepixelsofx=blocksize
            changepixelsofy=nopixel
        elif uparrow:
            changepixelsofy=-blocksize
            changepixelsofx=nopixel
        elif downarrow: 
            changepixelsofy=blocksize
            changepixelsofx=nopixel
            
            
#logic2


    if leadx>=window_width or leadx<0 or leady>=window_height or leady<0:
        gameover=True
        
        
    leadx+=changepixelsofx
    leady+=changepixelsofy

    gamedisplay.fill(white)

    applethickness=20


#logic3


    print([int(randomapplex),int(randomappley),applethickness,applethickness])     
    pygame.draw.rect(gamedisplay,red,[randomapplex,randomappley,applethickness,applethickness])
        
        
        
    allspriteslist=[]
    allspriteslist.append(leadx)
    allspriteslist.apend(leady)
    snakelist.append(allspriteslist)
        
        
        
         
    if len(snakelist)>snakelength:
        del snakelist[0]
            
       
    for eachsegment in snakelist[:-1]:
        if eachsegment==allspriteslist:
                gameover=True
                
   #logic4         
    snake(blocksize,snakelist)
        
    pygame.display.update()
            
    #logic5
    
    if leadx>=randomapplex and leadx<=randomapplex+applethickness:
        if leady>=randomappley and leady<=randomappley+applethickness:
            randomapplex=round(random.randrange(0, window_width-blocksize)/10.0)*10.0
            randomappley=round(random.randrange(0, window_height-blocksize)/10.0)*10.0
            snakelength+=1
            
            
    clock.tick(FPS)
    
    
    
    pygame.quit()
    quit()
    gameloop()    
