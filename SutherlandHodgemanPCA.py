from copy import copy
import glfw
from OpenGL.GL import *

x_min = 200
y_min = 200
x_max = 450
y_max = 450


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def sutherland_hodgeman(polygon: list[Point]):
    sides = len(polygon)

    clipped = []
    # Left border
    for i in range(sides):
        p1 = copy(polygon[i])
        p2 = copy(polygon[(i + 1) % sides])
        slope = (p2.y - p1.y) / (p2.x - p1.x)

        if p1.x >= x_min:
            if p2.x >= x_min:
                # Both inside
                clipped.append(p1)
            else:
                # Inside to outside
                slope = (p2.y - p1.y) / (p2.x - p1.x)
                p2.y = p1.y + slope * (x_min - p1.x)
                p2.x = x_min
                clipped.append(p1)
                clipped.append(p2)
        else:
            if p2.x >= x_min:
                # Outside to inside
                slope = (p2.y - p1.y) / (p2.x - p1.x)
                p1.y = p1.y + slope * (x_min - p1.x)
                p1.x = x_min
                clipped.append(p1)
            else:
                # Both outside
                pass

    polygon = clipped
    sides = len(polygon)
    clipped = []

    # Right border
    for i in range(sides):
        p1 = copy(polygon[i])
        p2 = copy(polygon[(i + 1) % sides])

        if p1.x <= x_max:
            if p2.x <= x_max:
                # Both inside
                clipped.append(p1)
            else:
                # Inside to outside
                slope = (p2.y - p1.y) / (p2.x - p1.x)
                p2.y = p1.y + slope * (x_max - p1.x)
                p2.x = x_max
                clipped.append(p1)
                clipped.append(p2)
        else:
            if p2.x <= x_max:
                # Outside to inside
                slope = (p2.y - p1.y) / (p2.x - p1.x)
                p1.y = p1.y + slope * (x_max - p1.x)
                p1.x = x_max
                clipped.append(p1)
            else:
                # Both outside
                pass

    polygon = clipped
    sides = len(polygon)
    clipped = []

    # Bottom border
    for i in range(sides):
        p1 = copy(polygon[i])
        p2 = copy(polygon[(i + 1) % sides])

        if p1.y >= y_min:
            if p2.y >= y_min:
                # Both inside
                clipped.append(p1)
            else:
                # Inside to outside
                slope_inv = (p2.x - p1.x) / (p2.y - p1.y)
                p2.x = p1.x + slope_inv * (y_min - p1.y)
                p2.y = y_min
                clipped.append(p1)
                clipped.append(p2)
        else:
            if p2.y >= y_min:
                # Outside to inside
                slope_inv = (p2.x - p1.x) / (p2.y - p1.y)
                p1.x = p1.x + slope_inv * (y_min - p1.y)
                p1.y = y_min
                clipped.append(p1)
            else:
                # Both outside
                pass

    polygon = clipped
    sides = len(polygon)
    clipped = []

    # Top border
    for i in range(sides):
        p1 = copy(polygon[i])
        p2 = copy(polygon[(i + 1) % sides])

        if p1.y <= y_max:
            if p2.y <= y_max:
                # Both inside
                clipped.append(p1)
            else:
                # Inside to outside
                slope_inv = (p2.x - p1.x) / (p2.y - p1.y)
                p2.x = p1.x + slope_inv * (y_max - p1.y)
                p2.y = y_max
                clipped.append(p1)
                clipped.append(p2)
        else:
            if p2.y <= y_max:
                # Outside to inside
                slope_inv = (p2.x - p1.x) / (p2.y - p1.y)
                p1.x = p1.x + slope_inv * (y_max - p1.y)
                p1.y = y_max
                clipped.append(p1)
            else:
                # Both outside
                pass

    return clipped


def draw_poly(polygon):
    glBegin(GL_LINE_LOOP)
    for point in polygon:
        glVertex2f(point.x, point.y)
    glEnd()


glfw.init()
window = glfw.create_window(600, 600, "Sutherland Hodgeman Polygon Clipping", None, None)
glfw.make_context_current(window)

polygon = [
    Point(282, 116),
    Point(535, 300),
    Point(412, 377),
    Point(242, 490),
    Point(162, 278),
    Point(200, 220),
]

clipped = sutherland_hodgeman(polygon)
print(clipped)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)

    glColor3f(1, 1, 1)
    # Clipping window
    glBegin(GL_LINES)
    glVertex2f(x_min, y_min)
    glVertex2f(x_min, y_max)
    glVertex2f(x_max, y_max)
    glVertex2f(x_max, y_min)
    glVertex2f(x_min, y_max)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glEnd()

    draw_poly(polygon)
    glColor3f(0, 1, 0)
    draw_poly(clipped)

    glfw.swap_buffers(window)
    glfw.poll_events()
