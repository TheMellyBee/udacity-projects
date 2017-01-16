import math

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
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        try:
            mag = self.magnitude()
            return self.scalar_mult(1/mag)

        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    def dot_product(self, v):
        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])

    # TODO fix with exceptions for more stability
    # TODO change to one function
    def radian_angle(self, v):
        dot = self.dot_product(v)
        return math.acos(dot/(self.magnitude() * v.magnitude()))

    def  degree_angle(self, v):
        return math.degrees(self.radian_angle(v))

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)



    def __eq__(self, v):
        return self.coordinates == v.coordinates
