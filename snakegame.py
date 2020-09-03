import pygame 
import random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.init()
pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
WIDTH=1300
HEIGHT=650
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake by Kushal Sharma")
bgimg=pygame.image.load("home.jpg")
bgimg=pygame.transform.scale(bgimg,(WIDTH,HEIGHT)).convert_alpha()
goimg=pygame.image.load("game_over.jpg")
goimg=pygame.transform.scale(goimg,(600,500)).convert_alpha()
pygame.display.update()
font=pygame.font.SysFont(None,55)
def plotsnake(gameWindow,color,snakelist,snakesize):
    for x,y in snakelist:
        pygame.draw.rect(gameWindow,color,[x,y,snakesize,snakesize])
def show(text,color,x,y):
    show_score=font.render(text,True,color)
    gameWindow.blit(show_score,[x,y])
def welcome():
    exitgame=False
    while not exitgame:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load("bg.mp3")
                        pygame.mixer.music.play(-1)
                        gameloop()
        # gameWindow.fill(black)
        gameWindow.blit(bgimg,(0,0))
        show("Welcome to Snake Game",white,420,200)
        show("Developed By Kushal Sharma",white,370,280)
        show("Press enter to continue",white,430,380)
        pygame.display.update()

def gameloop():
    snakex=45
    snakey=55
    ivelo=1
    snakesize=15
    foodsize=15
    fps=60
    velox=0
    veloy=0
    score=0
    foodx=random.randint(25,WIDTH-25)
    foody=random.randint(40,HEIGHT-25)
    clock=pygame.time.Clock()
    exitgame=False
    gameover=False
    snakelist=[]
    snakelength=1
    vx=0
    vxx=0
    vy=0
    vyy=0
    vyu=0
    vyd=0
    vxr=0
    vxl=0
    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt",'w') as g:
            g.write("0")
    with open("Highscore.txt",'r') as f:
            highscore=f.read()
    while not exitgame:
        if gameover:
            gameWindow.fill(black)
            gameWindow.blit(goimg,(0,0))
            with open("Highscore.txt",'w') as f:
                f.write(str(highscore))
            # show("Game Over!",red,230,170)
            show("Press Enter to continue",white,530,230)
            show("Score:"+str(score),white,250,390)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load("bg.mp3")
                        pygame.mixer.music.play(-1)
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if vxx==0 and vxr==0:
                        if event.key==pygame.K_RIGHT:
                            velox+=ivelo
                            veloy=0
                            vx=0
                            vxx=1
                            vy=0
                            vyy=0
                            vxl=1
                            vyd=0
                            vyu=0
                    if vx==0 and vxl==0:
                        if event.key==pygame.K_LEFT:
                            velox-=ivelo
                            veloy=0
                            vx=1
                            vxx=0
                            vy=0
                            vyy=0
                            vxr=1
                            vyd=0
                            vyu=0
                    if vyy==0 and vyd==0:
                        if event.key==pygame.K_DOWN:
                            veloy+=ivelo
                            velox=0
                            vx=0
                            vxx=0
                            vy=0
                            vyy=1
                            vxl=0
                            vxr=0
                            vyu=1
                    if vy==0 and vyu==0:
                        if event.key==pygame.K_UP:
                            veloy-=ivelo
                            velox=0
                            vx=0
                            vxx=0
                            vy=1
                            vyy=0
                            vxl=0
                            vxr=0
                            vyd=1
            snakex+=velox
            snakey+=veloy
            if abs(snakex-foodx)<15 and abs(snakey-foody)<15:
                score+=10
                foodx=random.randint(25,WIDTH-25)
                foody=random.randint(40,HEIGHT-25)
                snakelength+=5
                ivelo+=0.1
                if score>int(highscore):
                    highscore=score
            gameWindow.fill(black)
            show("Score:"+str(score),red,5,5)
            show("High Score:"+str(highscore),red,900,5)
            show("____________________________________________________________________________________________________________________________________",red,1,5)
            pygame.draw.rect(gameWindow,red,[foodx,foody,foodsize,foodsize])
            head=[]
            head.append(snakex)
            head.append(snakey)
            snakelist.append(head)
            if len(snakelist)>snakelength:
                del snakelist[0]
            if head in snakelist[:-1]:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                gameover=True
            if snakex<0 or snakex>WIDTH or snakey<40 or snakey>HEIGHT:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                gameover=True
            plotsnake(gameWindow,white,snakelist,snakesize)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()    
welcome()      