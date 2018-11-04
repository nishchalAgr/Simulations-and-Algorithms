import pygame, sys, math
from pygame.locals import *

pygame.init()
winX = 800
winY = 600
win = pygame.display.set_mode((winX , winY))
zeroX = int(winX / 2)
zeroY = int(winY / 10)
a1 = math.pi/2
a2 = math.pi/4
a1_v = 0
a2_v = 0
r1 = 175
r2 = 175
m1 = 5
m2 = 5
x1 = int(r1 * (math.sin(a1)) + zeroX)
y1 = int(r1 * (math.cos(a1)) + zeroY)
x2 = int(r2 * (math.sin(a2)) + x1)
y2 = int(r2 * (math.cos(a2)) + y1)
g = 1
optim = 0
optimFactor = 1 #the lower the number the more power it takes
speed = 25 #the lower the number the more power it takes,  25 should be accurate to the real world

coorX = []
coorY = []

pygame.display.set_caption("Double Pendulum")

def calcBlue(y):
    factor = (r1 + r2) / 500
    blue = ((r1  + r2) - y) / factor

    if blue > 255:
        blue = 255

    elif blue < 0:
        blue = 0

    return int(blue)

def drawTail():
    for i in range(len(coorX)):
        if i > 0:
            blue = calcBlue(coorY[i])
            pygame.draw.line(win, (255-blue,0,blue),[coorX[i-1], coorY[i-1]] ,[coorX[i], coorY[i]], 1)

def drawPend():
    global a1
    global a2
    global a1_v
    global a2_v
    global x1
    global x2
    global y1
    global y2
    global optim

    a1_a = 0
    a2_a = 0

    pygame.draw.line(win, (0,0,0), [zeroX, zeroY], [x1, y1])
    pygame.draw.circle(win, (0,0,0), [x1, y1], m1)
    pygame.draw.line(win, (0,0,0), [x1, y1], [x2, y2])
    pygame.draw.circle(win, (0,0,0), [x2, y2], m2)


    #the formula to calculate a1 and a2 is based on the one given by https://www.myphysicslab.com/pendulum/double-pendulum-en.html
    num1 = -g * (2 * m1 + m2) * math.sin(a1);
    num2 = -m2 * g * math.sin(a1-2*a2);
    num3 = -2*math.sin(a1-a2)*m2;
    num4 = a2_v*a2_v*r2+a1_v*a1_v*r1*math.cos(a1-a2);
    den = r1 * (2*m1+m2-m2*math.cos(2*a1-2*a2));
    a1_a = (num1 + num2 + num3*num4) / den;

    num1 = 2 * math.sin(a1-a2);
    num2 = (a1_v*a1_v*r1*(m1+m2));
    num3 = g * (m1 + m2) * math.cos(a1);
    num4 = a2_v*a2_v*r2*m2*math.cos(a1-a2);
    den = r2 * (2*m1+m2-m2*math.cos(2*a1-2*a2));
    a2_a = (num1*(num2+num3+num4)) / den;


    a1_v += a1_a
    a2_v += a2_a

    a1 += a1_v
    a2 += a2_v
    #
    # print("----")
    # print(a1a)
    # print(a2a)
    # print(a1)
    # print(a2)

    x1 = int(r1 * (math.sin(a1)) + zeroX)
    y1 = int(r1 * (math.cos(a1)) + zeroY)
    x2 = int(r2 * (math.sin(a2)) + x1)
    y2 = int(r2 * (math.cos(a2)) + y1)
    if(optim % optimFactor == 0):
        coorX.append(x2)
        coorY.append(y2)
    optim += 1

run = True

while run:

    pygame.time.delay(speed)

    win.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run = False

    #a1 += math.pi/8
    #print(a1)
    drawPend()
    drawTail()
    pygame.display.update()
