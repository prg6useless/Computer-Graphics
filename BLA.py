import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


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
    # print("enter extreme points")
    # input1 = int(input())
    # input2 = int(input())
    # input3 = int(input())
    # input4 = int(input())

    inputPoints = [(85, 85, 200, 200), (200, 200, 350, 300)]

    pygame.init()

    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

    glOrtho(0, 800, 0, 600, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # BLA(300, 180, 200, 100)
    # BLA(input1, input2, input3, input4)
    for i in range(2):
        BLA(
            inputPoints[i][0],
            inputPoints[i][1],
            inputPoints[i][2],
            inputPoints[i][3],
        )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
