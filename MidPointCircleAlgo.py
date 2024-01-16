from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pntX1, pntY1, r = 0, 0, 0


def plotPoints(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x + pntX1, y + pntY1)
    glEnd()


def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)


def MCDA():
    x, y = 0, r
    decisionParameter = 5 / 4 - r
    plotPoints(x, y)

    while y >= x:
        if decisionParameter < 0:
            x += 1
            decisionParameter += 2 * x + 1
        else:
            y -= 1
            x += 1
            decisionParameter += 2 * (x - y) + 1

        plotPoints(x, y)
        plotPoints(x, -y)
        plotPoints(-x, y)
        plotPoints(-x, -y)
        plotPoints(y, x)
        plotPoints(-y, x)
        plotPoints(y, -x)
        plotPoints(-y, -x)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    MCDA()
    glFlush()


def main():
    global pntX1, pntY1, r
    print("Enter the coordinates of the center:\n")
    pntX1 = int(input("X-coordinate   : "))
    pntY1 = int(input("\nY-coordinate : "))
    r = int(input("\nEnter radius : "))

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("Midpoint Circle Drawing Algorithm")
    glutDisplayFunc(display)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
