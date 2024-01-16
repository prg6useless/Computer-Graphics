from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians


def rotation_mat(p, angle):
    angle = radians(angle)
    T = [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
    P = [p[0][0], p[1][0], 1]
    result = [0, 0, 0]

    for i in range(len(T)):
        for j in range(len(P)):
            result[i] += T[i][j] * P[j]

    return [[result[0]], [result[1]], [result[2]]]


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

    a = [[150], [150], [1]]
    b = [[200], [200], [1]]
    c = rotation_mat(a, -45)
    d = rotation_mat(b, -45)
    draw_line(a, b, c, d)

    a = [[200], [200], [1]]
    b = [[300], [50], [1]]
    c = rotation_mat(a, -45)
    d = rotation_mat(b, -45)
    draw_line(a, b, c, d)

    a = [[300], [50], [1]]
    b = [[150], [150], [1]]
    c = rotation_mat(a, -45)
    d = rotation_mat(b, -45)
    draw_line(a, b, c, d)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"2D Rotation")

    gluOrtho2D(0.0, 1000, 0.0, 500)
    glTranslatef(500, 250, 0)  # Translate to center of screen
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
