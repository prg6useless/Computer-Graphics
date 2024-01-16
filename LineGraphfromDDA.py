import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def DDA(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1

    # steps needed
    steps = max(abs(dx), abs(dy))

    # increase in x and y coordinates for every step
    Xinc, Yinc = dx / steps, dy / steps

    for _ in range(int(steps)):
        glVertex2f(x1, y1)
        print(f"Plotting : ({x1},{y1})")
        x1, y1 = x1 + Xinc, y1 + Yinc


def plotPoints(a, b):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(a, b)
    glEnd()
    print(f"Plotting : ({a},{b})")
    pygame.display.flip()


def BLA(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    x, y = x0, y0

    if x1 >= x0:
        xi = 1
    else:
        xi = -1
    if y1 >= y0:
        yi = 1
    else:
        yi = -1
    plotPoints(x, y)

    if dx > dy:  # m < 1
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx
        while x != x1:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi
            plotPoints(x, y)
    else:  # m >= 1
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy
        while y != y1:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi
            plotPoints(x, y)


def main():
    print("enter which algorithm to use")
    inputAlgo = input()

    # inputPoints = [
    #     (85, 85, 200, 200),
    #     (200, 200, 350, 300),
    #     (350, 300, 550, 505),
    #     (550, 505, 600, 630),
    # ]

    inputPoints = [(85, 85), (200, 200), (350, 300), (550, 505), (600, 630)]

    if inputAlgo == "DDA":
        pygame.init()

        pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)

        gluOrtho2D(0, 800, 0, 800)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
        glBegin(GL_POINTS)
        for i in range(len(inputPoints) - 1):
            DDA(
                inputPoints[i][0],
                inputPoints[i][1],
                inputPoints[i + 1][0],
                inputPoints[i + 1][1],
            )
        glEnd()
        pygame.display.flip()

    elif inputAlgo == "BLA":
        pygame.init()

        pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)

        glOrtho(0, 800, 0, 800, -1, 1)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        for i in range(len(inputPoints) - 1):
            BLA(
                inputPoints[i][0],
                inputPoints[i][1],
                inputPoints[i + 1][0],
                inputPoints[i + 1][1],
            )

    else:
        print("please enter a valid algorithm")
        exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.time.wait(10)


main()
