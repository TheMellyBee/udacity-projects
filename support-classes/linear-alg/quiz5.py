from vector import Vector

print "\nOne"
v = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print v.component_projection_vector(b)

print "\nTwo"
v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print v.component_orthogonal_vector(b)

print "\nThree"
v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print v.component_projection_vector(b)
print v.component_orthogonal_vector(b)
