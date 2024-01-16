from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_polygon(x1, y1, x2, y2, x3, y3):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()


def draw_sheared_polygon(x1, y1, x2, y2, x3, y3, shear_f):
    glColor3f(0.3, 0.5, 0.8)
    glLineStipple(1, 0x0F0F)
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def shearing(x1, y1, x2, y2, x3, y3, shear_f):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)
    draw_polygon(x1, y1, x2, y2, x3, y3)

    glColor3f(1.0, 0.0, 0.0)
    x1 += y1 * shear_f
    x2 += y2 * shear_f
    x3 += y3 * shear_f

    draw_sheared_polygon(x1, y1, x2, y2, x3, y3, shear_f)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"2D Shearing")
    glutInitWindowSize(800, 600)
    gluOrtho2D(0.0, 800, 0.0, 600)
    glutDisplayFunc(lambda: shearing(100, 50, 200, 200, 300, 50, 2))
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutMainLoop()


if __name__ == "__main__":
    main()
