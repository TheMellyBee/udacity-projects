from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    def plus(self, v):
        new_cord = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_cord)


    def minus(self, v):
        new_cord = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_cord)


    def scalar_mult(self, c):
        new_cord = [c*x for x in self.coordinates]
        return Vector(new_cord)


    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))


    def normalize(self):
        try:
            mag = self.magnitude()
            return self.scalar_mult(Decimal('1.0')/mag)

        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")


    def dot_product(self, v):
        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])


    def angle_between(self, v, in_degrees=False):
        try:
            inner_mult = self.dot_product(v)
            angle_in_radians = acos(inner_mult/(self.magnitude() * v.magnitude()))

        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

        if in_degrees:
            return degrees(angle_in_radians)

        return angle_in_radians


    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)



    def __eq__(self, v):
        return self.coordinates == v.coordinates
