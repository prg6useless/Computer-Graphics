from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# 3D translation
def translation_mat(p, tx, ty, tz):
    P = [p[0] + tx, p[1] + ty, p[2] + tz, 1]
    return P


def draw_line(a, b, c, d):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(a[0], a[1], a[2])
    glVertex3f(b[0], b[1], b[2])
    glEnd()

    glColor3f(0.3, 0.5, 0.8)
    glLineStipple(1, 0x0F0F)  # a dashed pattern
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex3f(c[0], c[1], c[2])
    glVertex3f(d[0], d[1], d[2])
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    a = [100, 50, 0]
    b = [200, 200, 0]
    c = translation_mat(a, -50, -50, 0)
    d = translation_mat(b, -50, -50, 0)
    draw_line(a, b, c, d)

    a = [200, 200, 0]
    b = [300, 50, 0]
    c = translation_mat(a, -50, -50, 0)
    d = translation_mat(b, -50, -50, 0)
    draw_line(a, b, c, d)

    a = [300, 50, 0]
    b = [100, 50, 0]
    c = translation_mat(a, -50, -50, 0)
    d = translation_mat(b, -50, -50, 0)
    draw_line(a, b, c, d)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"3D Translation")

    gluPerspective(45, (1000 / 500), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
