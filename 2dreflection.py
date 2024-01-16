from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def reflection_mat(p):
    T = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
    P = [[p[0][0]], [p[1][0]], [p[2][0]]]
    result = [[0], [0], [0]]
    for i in range(len(T)):
        for j in range(len(P[0])):
            for k in range(len(P)):
                result[i][j] += T[i][k] * P[k][j]
    return result


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

    a = [[200], [-200], [1]]
    b = [[100], [-100], [1]]
    c = reflection_mat(a)
    d = reflection_mat(b)
    draw_line(a, b, c, d)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
    glutCreateWindow(b"2D Reflection")

    glOrtho(0.0, 1000, 0.0, 500, -1.0, 1.0)
    glTranslatef(500, 250, 0)  # Translate to center of the screen
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
