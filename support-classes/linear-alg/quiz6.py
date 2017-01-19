from vector import Vector

print "Cross Product"
v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])
print v1.cross_product(v2)

print "\nArea Parallelogram"
v1 = Vector([-8.987, -9.838, 5.031])
v2 = Vector([-4.268 , -1.861, -8.866])
print v1.area_paralellogram(v2)

print "\nArea Triangle"
v1 = Vector([1.5, 9.547, 3.691])
v2 = Vector([-6.007, 0.124, 5.772])
print v1.area_triangle(v2)