import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# PyGame Initialization
pygame.init()

# Dimensions of the Flag
flag_width = 800
flag_height = 600

radius = 5.0
radius2 = 2.3
vertices = 80

pygame.display.set_mode((flag_width, flag_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("Nepal's Flag")

# Initialization of OpenGL
glClearColor(0.9, 0.9, 0.9, 1.0)
glViewport(0, 0, flag_width, flag_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, flag_width, 0, flag_height, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()


def red_triangles():
    # Upper Triangle
    glColor3f(1.0, 0.0, 0.0)  # Red
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 530)  # Top Left
    glVertex2f(100, 280)  # Bottom Left
    glVertex2f(460, 280)  # Bottom Right
    glEnd()

    # Lower Triangle
    glColor3f(1.0, 0.0, 0.0)  # Red
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 50)  # Bottom Left
    glVertex2f(100, 322)  # Top Left
    glVertex2f(460, 50)  # Bottom Right
    glEnd()


def draw_borders():
    # Upper Blue Triangle
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glBegin(GL_TRIANGLES)
    glVertex2f(90, 550)  # Top Left
    glVertex2f(90, 270)  # Bottom Left
    glVertex2f(490, 270)  # Bottom Right
    glEnd()

    # Lower Blue Triangle
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glBegin(GL_TRIANGLES)
    glVertex2f(90, 40)  # Bottom Left
    glVertex2f(90, 342)  # Top Left
    glVertex2f(490, 40)  # Bottom Right
    glEnd()


def circle(x, y, radius, color):
    color  # white
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Center of the Circle
    for i in range(vertices + 1):
        angle = i * (2 * math.pi / vertices)
        x = radius * math.cos(angle) + x
        y = radius * math.sin(angle) + y
        glVertex2f(x, y)
    glEnd()


def draw_spikes(x, y, num_spikes, outer_radius, inner_radius, color):
    angle_increment = 2 * math.pi / num_spikes

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Center of the Circle
    for i in range(num_spikes + 1):
        angle = i * angle_increment
        if i % 2 == 0:
            x_i = inner_radius * math.cos(angle) + x
            y_i = inner_radius * math.sin(angle) + y
        else:
            x_i = outer_radius * math.cos(angle) + x
            y_i = outer_radius * math.sin(angle) + y
        glVertex2f(x_i, y_i)
    glEnd()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_borders()
    red_triangles()

    # Draw the circle
    circle(200, 100, 3, glColor3f(1.0, 1.0, 1.0))  # Lower
    circle(200, 320, 4.5, glColor3f(1.0, 1.0, 1.0))  # Upper White
    circle(200, 340, 4.2, glColor3f(1.0, 0.0, 0.0))  # UpperRred
    circle(200, 330, 2.5, glColor3f(1.0, 1.0, 1.0))  # Smaller Upper White

    # Draw the spikes around the circles

    draw_spikes(
        202, 137, 24, 65.0, 34.0, glColor3f(1.0, 1.0, 1.0)
    )  # spikes around lower circle

    # draw_spikes(
    #     200, 320, 48, 65.0, 34.0, glColor3f(0.0, 0.0, 0.0)
    # )  # spikes around upper white circle

    # Update the display
    pygame.display.flip()
    pygame.time.wait(50)
