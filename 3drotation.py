import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math
from itertools import product

vertices = list(product([-2, 2], repeat=3))


def draw_cube():
    glBegin(GL_LINES)
    for edge in [
        (0, 1),
        (1, 3),
        (3, 2),
        (2, 0),
        (0, 4),
        (1, 5),
        (3, 7),
        (2, 6),
        (4, 5),
        (5, 7),
        (7, 6),
        (6, 4),
    ]:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_rotated_cube(theta):
    theta = np.radians(theta)
    rotated_vertices = [
        [
            v[0] * math.cos(theta) - v[1] * math.sin(theta),
            v[0] * math.sin(theta) + v[1] * math.cos(theta),
            v[2],
        ]
        for v in vertices
    ]

    glBegin(GL_LINES)
    for edge in [
        (0, 1),
        (1, 3),
        (3, 2),
        (2, 0),
        (0, 4),
        (1, 5),
        (3, 7),
        (2, 6),
        (4, 5),
        (5, 7),
        (7, 6),
        (6, 4),
    ]:
        for vertex in edge:
            glVertex3fv(rotated_vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glScalef(0.5, 0.5, 0.5)  # Scale the cube to half of its original size

    theta = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_cube()
        draw_rotated_cube(theta)

        pygame.display.flip()
        pygame.time.wait(10)
        theta += 1


if __name__ == "__main__":
    main()
