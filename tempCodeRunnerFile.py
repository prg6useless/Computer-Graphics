from OpenGL.GL import *
from OpenGL.GLUT import *


# 2D scaling
def scaling_mat(p, sx, sy):
    P = [p[0][0] * sx, p[1][0] * sy, 1]
    return [[P[0]], [P[1]], [P[2]]]


def draw_line(a, b, c, d):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(a[0][0], a[1][0])
    glVertex2f(b[0][0], b[1][0])
    glEnd()

    glColor3f(0.3, 0.5, 0.8)
    glLineStipple(1, 0x0F0F)  # a dashed pattern
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex2f(c[0][0], c[1][0])
    glVertex2f(d[0][0], d[1][0])
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    a = [[0], [0], [1]]
    b = [[100], [100], [1]]
    c = scaling_mat(a, 2, 2)
    d = scaling_mat(b, 2, 2)
    draw_line(a, b, c, d)

    a = [[100], [100], [1]]
    b = [[200], [0], [1]]
    c = scaling_mat(a, 2, 2)
    d = scaling_mat(b, 2, 2)
    draw_line(a, b, c, d)

    a = [[200], [0], [1]]
    b = [[100], [-100], [1]]
    c = scaling_mat(a, 2, 2)
    d = scaling_mat(b, 2, 2)
    draw_line(a, b, c, d)

    a = [[100], [-100], [1]]
    b = [[0], [0], [1]]
    c = scaling_mat(a, 2, 2)
    d = scaling_mat(b, 2, 2)
    draw_line(a, b, c, d)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"2D Scaling and Drawing Lines")

    glOrtho(0.0, 1000, 0.0, 500, -1.0, 1.0)

    glTranslatef(500, 250, 0)  # Translate to center of screen
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
