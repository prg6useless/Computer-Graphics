import glfw
from OpenGL.GL import *
from math import sin, cos, radians

w = 1200
h = 600

def initialize():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-2, 2, -1, 1, 1, 500)
    glTranslated(-10, -6, -10)

def matrix_multiply(a, b):
    rowA, rowB = len(a), len(b)
    colA, colB = len(a[0]), len(b[0])
    
    if colA != rowB:
        raise Exception("Invalid matrix multiply")
    
    res = [[0] * colB for _ in range(rowA)]
    for i in range(colB):
        for j in range(rowA):
            val = 0
            for k in range(colA):
                val += a[j][k] * b[k][i]
            res[j][i] = val
    return res

def translation(tx, ty, tz):
    return [
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ]

def rotation(axis, angle):
    t = radians(angle)

    if (axis == 'x'):
        # Pitch
        return [
            [1,      0,       0, 0],
            [0, cos(t), -sin(t), 0],
            [0, sin(t),  cos(t), 0],
            [0,      0,       0, 1]
        ]
    elif (axis == 'y'):
        # Yaw
        return [
            [ cos(t), 0, sin(t), 0],
            [      0, 1,      0, 0],
            [-sin(t), 0, cos(t), 0],
            [      0, 0,      0, 1],
        ]
    else:
        # Roll
        return [
            [cos(t), -sin(t), 0, 0],
            [sin(t),  cos(t), 0, 0],
            [     0,       0, 1, 0],
            [     0,       0, 0, 1]
        ]

def scale(sx, sy, sz):
    return [
        [sx,  0,  0, 0],
        [ 0, sy,  0, 0],
        [ 0,  0, sz, 0],
        [ 0,  0,  0, 1],
    ]

def render_axes():
    glBegin(GL_LINES)
    # x axis
    glColor3f(0.5, 0, 0)
    glVertex2f(-100, 0)
    glVertex2f(100, 0)
    # y axis
    glColor3f(0, 0.5, 0)
    glVertex2f(0, -100)
    glVertex2f(0, 100)
    # z axis
    glColor3f(0, 0, 0.5)
    glVertex3f(0, 0, -500)
    glVertex3f(0, 0, 100)
    glEnd()

def render(points, edges):
    if len(points) == 0:
        return

    glBegin(GL_LINES)
    for edge in edges:
        for index in edge:
            glVertex3f(
                points[0][index],
                points[1][index],
                points[2][index]
            )
    glEnd()

cuboid = [
    [1, 8, 8, 1,   1,   1,   8,   8],
    [1, 1, 5, 5,   5,   1,   1,   5],
    [0, 0, 0, 0, -10, -10, -10, -10],
    [1, 1, 1, 1,   1,   1,   1,   1]
]
edges = [
    # Front face edges
    (0, 1), (1, 2), (2, 3), (3, 0), 
    
    # Back face edges
    (4, 5), (5, 6), (6, 7), (7, 4), 
    
    # Side edges
    (0, 5), (1, 6), (2, 7), (3, 4)
]

transformed = []


glfw.init()
window = glfw.create_window(w, h, "3D Transformations", None, None)
glfw.make_context_current(window)

while not glfw.window_should_close(window):
    initialize()
    render_axes()
    glColor3f(1.0, 1.0, 1.0)
    render(cuboid, edges)
    glColor3f(0.7, 0.3, 1.0)
    render(transformed, edges)
    
    if glfw.PRESS == glfw.get_key(window, glfw.KEY_1):
        print("Translation")
        transformed = matrix_multiply(translation(12, 1.5, 4), cuboid)
    elif glfw.PRESS == glfw.get_key(window, glfw.KEY_2):
        print("Rotation")
        transformed = matrix_multiply(rotation('z', 100), cuboid)
    elif glfw.PRESS == glfw.get_key(window, glfw.KEY_3):
        print("Scaling")
        transformed = matrix_multiply(scale(3, 1, 0.3), cuboid)
    
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()