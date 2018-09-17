import numpy
from matplotlib import pyplot


def mandelbrot(x, y, max_iterations):
    point = x + y * 1j
    z, iterations = complex(0, 0), 0
    while abs(z) < 2 and iterations < max_iterations:
        z = (z * z) + point
        iterations += 1
    return iterations


# location and size of rectangle
x1, x2 = -3.0, 2.0
y1, y2 = -1.5, 1.5
width, height = 1500, 1000
max_iterations = 127
C = numpy.zeros([height, width])
dx = (x2 - x1) / width
dy = (y2 - y1) / height

for i in range(height):
    for j in range(width):
        y = y1 + i * dy
        x = x1 + j * dx
        C[i, j] = mandelbrot(x, y, max_iterations)

pyplot.imshow(C.T)
pyplot.show()
