from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

x_max = 350
y_max = 350
x_min = 50
y_min = 50

xd1, yd1, xd2, yd2 = 0, 0, 0, 0


def init():
    glClearColor(0.0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 400, 0, 400)


def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


def cohen_line(x1, y1, x2, y2):
    # region = [x1, y1, x2, y2]

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:
        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:
            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:
                # point is above the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1)
                y = y_max

            elif code_out & BOTTOM:
                # point is below the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1)
                y = y_min

            elif code_out & RIGHT:
                # point is to the right of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1)
                x = x_max

            elif code_out & LEFT:
                # point is to the left of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1)
                x = x_min

            # Now intersection point x, y is found
            # We replace point outside clipping rectangle
            # by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glFlush()

    else:
        print("Line rejected")


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_LINE_LOOP)
    glVertex2i(x_min, y_min)
    glVertex2i(x_min, y_max)
    glVertex2i(x_max, y_max)
    glVertex2i(x_max, y_min)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    cohen_line(x1, y1, x2, y2)


def main():
    global x1, y1, x2, y2
    print("Enter line co-ordinates:")
    x1, y1, x2, y2 = map(float, input().split())

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Cohen Sutherland Line Clipping")
    glutDisplayFunc(display)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
