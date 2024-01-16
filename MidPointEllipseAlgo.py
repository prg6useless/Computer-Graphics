from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def ellipse_symmetry(center_x, center_y, x, y):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)

    glVertex2i(center_x + x, center_y + y)
    glVertex2i(center_x - x, center_y + y)
    glVertex2i(center_x + x, center_y - y)
    glVertex2i(center_x - x, center_y - y)

    glEnd()


def midpoint_ellipse(center_x, center_y, r_x, r_y):
    x, y = 0, r_y

    # Region 1
    d_a = 2 * math.pow(r_y, 2) * x
    d_b = 2 * math.pow(r_x, 2) * y
    p1 = math.pow(r_y, 2) - math.pow(r_x, 2) * r_y + 0.25 * math.pow(r_x, 2)
    while d_a < d_b:
        ellipse_symmetry(center_x, center_y, x, y)

        d_a = 2 * math.pow(r_y, 2) * x
        d_b = 2 * math.pow(r_x, 2) * y

        if p1 < 0:
            p1 = p1 + d_a + math.pow(r_y, 2)
        else:
            y = y - 1
            p1 = p1 + d_a - d_b + math.pow(r_y, 2)
        x = x + 1

    # Region 2
    p2 = (
        math.pow(r_y, 2) * math.pow((x + 0.5), 2)
        + math.pow(r_x, 2) * math.pow((y - 1), 2)
        - math.pow(r_x, 2) * math.pow(r_y, 2)
    )
    while y > 0:
        ellipse_symmetry(center_x, center_y, x, y)

        if p2 <= 0:
            x = x + 1
            p2 = (
                p2
                + 2 * math.pow(r_y, 2) * x
                - 2 * math.pow(r_x, 2) * y
                + math.pow(r_x, 2)
            )
        else:
            p2 = p2 - 2 * math.pow(r_x, 2) * y + math.pow(r_x, 2)
        y = y - 1


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)

    midpoint_ellipse(300, 300, 150, 250)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Mid-Point Ellipse Drawing Algorithm")
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()
