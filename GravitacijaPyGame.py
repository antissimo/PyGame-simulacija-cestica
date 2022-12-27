import pygame
import math
import random
from enum import Enum
Balls=[]
def colorreact(color1,color2):
    colorMatrix=[[-0.6,0.7,-1.1,-0.5],[-0.3,5,-0.6,0.5],[0.8,0,-0.6,0],[0.6,-1.2,0,0]]
    return colorMatrix[color1.value-1][color2.value-1]
class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3
    Yellow = 4
class Ball:
    def __init__(self,boja,xpozicija,ypozicija,xbrzina,ybrzina):
        self.boja=boja
        self.xpozicija=xpozicija
        self.ypozicija=ypozicija
        self.xbrzina=xbrzina
        self.ybrzina=ybrzina
        Balls.append(self)
    def calculateDistance(self,ball):
        return math.sqrt((self.xpozicija-ball.xpozicija)**2 + (self.ypozicija-ball.ypozicija)**2)#cudno radi kad je d**2 umisto d 
    def calculateAngle(self,ball):
        if (ball.xpozicija-self.xpozicija)==0:
            return 0
        return abs(math.atan((ball.ypozicija-self.ypozicija)/(ball.xpozicija-self.xpozicija)))
    def react(self):
        for ball in Balls:
            if ball!=self:
                self.xbrzina+=math.sin(self.calculateAngle(ball))*colorreact(self.boja,ball.boja)/self.calculateDistance(ball)*3
                self.ybrzina+=math.cos(self.calculateAngle(ball))*colorreact(self.boja,ball.boja)/self.calculateDistance(ball)*3
        self.xpozicija+=self.xbrzina
        if self.xpozicija>1490:
            self.xpozicija=2980-self.xpozicija
            self.xbrzina=self.xbrzina*(-1)
        if self.ypozicija>740:
            self.ypozicija=1480-self.ypozicija
            self.ybrzina=self.ybrzina*(-1)
        if self.ypozicija<10:
            self.ypozicija=20-self.ypozicija
            self.ybrzina=self.ybrzina*(-1)
        if self.xpozicija<10:
            self.xpozicija=20-self.xpozicija
            self.xbrzina=self.xbrzina*(-1)
        self.ypozicija+=self.ybrzina
def drawBalls(Balls):
    for ball in Balls:
        if ball.boja==Color.Red:
            pygame.draw.circle(screen, (255, 0, 0), (ball.xpozicija, ball.ypozicija), 10)
            pygame.display.flip()
        if ball.boja==Color.Green:
            pygame.draw.circle(screen, (0, 255, 0), (ball.xpozicija, ball.ypozicija), 10)
            pygame.display.flip()
        if ball.boja==Color.Blue:
            pygame.draw.circle(screen, (0, 0, 255), (ball.xpozicija, ball.ypozicija), 10)
            pygame.display.flip()
        if ball.boja==Color.Yellow:
            pygame.draw.circle(screen, (255, 255, 0), (ball.xpozicija, ball.ypozicija), 10)
            pygame.display.flip()
def createBalls(ballsRed,ballsGreen,ballsBlue,ballsYellow):
    for i in range(ballsRed):
        xpozicija=random.randint(0,1500)
        ypozicija=random.randint(0,750)
        boja=Color.Red
        ball=Ball(boja,xpozicija,ypozicija,0,0)
        pygame.draw.circle(screen, (255, 0, 0), (xpozicija, ypozicija), 10)
        pygame.display.flip()
    for i in range(ballsGreen):
        xpozicija=random.randint(0,1500)
        ypozicija=random.randint(0,750)
        boja=Color.Green
        ball=Ball(boja,xpozicija,ypozicija,0,0)
        pygame.draw.circle(screen, (0, 255, 0), (xpozicija, ypozicija), 10)
        pygame.display.flip()
    for i in range(ballsBlue):
        xpozicija=random.randint(0,1500)
        ypozicija=random.randint(0,750)
        boja=Color.Blue
        ball=Ball(boja,xpozicija,ypozicija,0,0)
        pygame.draw.circle(screen, (0, 0, 255), (xpozicija, ypozicija), 10)
        pygame.display.flip()
    for i in range(ballsYellow):
        xpozicija=random.randint(0,1500)
        ypozicija=random.randint(0,750)
        boja=Color.Yellow
        ball=Ball(boja,xpozicija,ypozicija,0,0)
        pygame.draw.circle(screen, (255, 255, 0), (xpozicija, ypozicija), 10)
        pygame.display.flip()
pygame.init()
screen = pygame.display.set_mode([1500, 750])
running = True
createBalls(100,10,10,10)#proporcionalno je sa kvadratom broja loptica, pa kad je vise od 40 loptica, fps odpadne

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for ball in Balls:
        ball.react()
    screen.fill((0, 0, 0))
    drawBalls(Balls)
    
pygame.quit()
