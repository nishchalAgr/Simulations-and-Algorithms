import pygame, sys, math
from pygame.locals import *

infix = "x^2"
postfix = ""
speed = 60

pygame.init()
winX = 600
winY = 600
originX = winX/2
originY = winY/2
win = pygame.display.set_mode((winX , winY))
spacing = 20
numPoints = 0.01
pointGap = 100;

def plot(x , y):

    global color

    x *= pointGap
    y *= pointGap
    x = originX + x
    y = originY - y
    pygame.draw.circle(win, (0,0,200), (int(x),int(y)), 3)

def drawgraph():

    global infix
    global postfix

    postFix()

    x = -300
    while x < originX:
        y = eval(x)
        if y < originY and y > -originY:
            print(x , y)
            plot(x , y)
        x += numPoints

def drawplane():
    i = 0
    while i < winX:
        pygame.draw.line(win, (200,200,200), (i, 0), (i, winY))
        i += spacing
    
    i = 0
    while i < winY:
        pygame.draw.line(win, (200,200,200), (0, i), (winX, i))
        i += spacing
    
    pygame.draw.line(win, (0,0,0), (originX, 0), (originX, winY))
    pygame.draw.line(win, (0,0,0), (0, originY), (winX, originY))



def isOperator(a):
    if a == '^': return 3
    if a == '/' or a == '*': return 2
    if a == '+' or a == '-': return 1
    return 0

def exponent(first, second):
    i = 0
    exp = first
    while i < second - 1:
        first = first * exp
        i += 1
    return first

def top(stack):
    if(len(stack) != 0): return stack[len(stack) - 1]

#infix to postfix
def postFix():

    global infix
    global postfix

    stack = []

    i = 0

    while i < len(infix):

        print(i, ":" , stack)

        if infix[i] == 'x':
            postfix += 'x'

        elif infix[i].isdigit():
            while i < len(infix) and infix[i].isdigit():
                postfix += infix[i]
                i += 1
            i -= 1
            postfix += '|'

        elif infix[i] == '(':
            stack.append(infix[i])

        elif infix[i] == ')':
            while top(stack) != '(':
                postfix += top(stack)
                stack.pop()
            stack.pop()

        elif isOperator(infix[i]) > 0:
            while len(stack) != 0 and top(stack) != ')' and isOperator(infix[i]) <= isOperator(top(stack)):
                postfix += top(stack)
                stack.pop()
            stack.append(infix[i])
        
        i += 1

    while len(stack) != 0:
        postfix += top(stack)
        stack.pop()


#postfix to answer
def eval(x):

    global postfix

    stack = []

    i = 0

    while i < len(postfix):
        #if char is digit
        if(postfix[i].isdigit()):
            temp = ""
            while postfix[i] != '|':
                if(postfix[i] == 'x'):
                    stack.append(x)
                else:
                    temp += postfix[i]
                i += 1
            stack.append(int(temp))
        elif(postfix[i] == 'x'):
            stack.append(x)
        #if char is operator 
        elif(isOperator(postfix[i]) != 0):
            second = top(stack)
            stack.pop()

            first = top(stack)
            stack.pop()

            if(postfix[i] == '+'): 
                stack.append(first + second)
            elif(postfix[i] == '-'): 
                stack.append(first - second)
            elif(postfix[i] == '*'): 
                stack.append(first * second)
            elif(postfix[i] == '/'): 
                stack.append(first / second)
            elif(postfix[i] == '^'): 
                stack.append(exponent(first, second))

        i += 1

    return top(stack)

run = True
runEval = True

print("Answer:", eval(10))


win.fill((255,255,255))

time_start = pygame.time.get_ticks()   
drawplane()
drawgraph()
time_end = pygame.time.get_ticks()
print("Calculation and drawing took: " , time_end - time_start , " ms")
    #drawgraph()
    
     #a1 += math.pi/8
    #print(a1)
pygame.display.update()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run = False
#print("postfix:", postfix)
            
