from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# 2D translation
def translation_mat(p, tx, ty):
    P = [p[0] + tx, p[1] + ty, 1]
    return P


def draw_line(a, b, c, d):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(a[0], a[1])
    glVertex2f(b[0], b[1])
    glEnd()

    glColor3f(0.3, 0.5, 0.8)
    glLineStipple(1, 0x0F0F)  # a dashed pattern
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex2f(c[0], c[1])
    glVertex2f(d[0], d[1])
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    a = [100, 50]
    b = [200, 200]
    c = translation_mat(a, -50, -50)
    d = translation_mat(b, -50, -50)
    draw_line(a, b, c, d)

    a = [200, 200]
    b = [300, 50]
    c = translation_mat(a, -50, -50)
    d = translation_mat(b, -50, -50)
    draw_line(a, b, c, d)

    a = [300, 50]
    b = [100, 50]
    c = translation_mat(a, -50, -50)
    d = translation_mat(b, -50, -50)
    draw_line(a, b, c, d)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"2D Translation")

    gluOrtho2D(0.0, 1000, 0.0, 500)
    glTranslatef(500, 250, 0)  # Translate to center of screen
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
