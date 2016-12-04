import math

class Vector:

    def __init__(self, c):
        self.coordinates = c

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        squares = [x**2 for x in self.coordinates]
        return math.sqrt(sum(squares))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

a = Vector([-0.221, 7.437])
b = Vector([8.813, -1.331, -6.247])
c = Vector([5.581, -2.136])
d = Vector([1.996, 3.108, -4.554])
print a.magnitude()
print b.magnitude()
print c.normalize()
print d.normalize()


