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


def main():
    # print("enter extreme points x1, x2, y1, y2")
    # input1 = int(input())
    # input2 = int(input())
    # input3 = int(input())
    # input4 = int(input())

    inputPoints = [
        (85, 85, 200, 200),
        (200, 200, 350, 300),
        (350, 300, 150, 105),
        (150, 105, 400, 230),
    ]

    pygame.init()

    pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)

    gluOrtho2D(0, 500, 0, 500)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    # DDA(85, 85, 200, 200)
    # DDA(input1,input2,input3,input4)
    for i in range(2):
        DDA(
            inputPoints[i][0],
            inputPoints[i][1],
            inputPoints[i][2],
            inputPoints[i][3],
        )

    glEnd()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.time.wait(10)


main()
