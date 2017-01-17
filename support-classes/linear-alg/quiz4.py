from vector import Vector

print "One"
v1 = Vector([-7.579,-7.88])
v2 = Vector([22.737,23.64])
print "Parallel: "
print v1.is_parallel(v2)
print "Orthogonal: "
print v1.is_orthogonal(v2)
print

print "Two"
v1 = Vector([-2.029,9.97,4.172])
v2 = Vector([-9.231,-6.639, -7.245])
print "Parallel: "
print v1.is_parallel(v2)
print "Orthogonal: "
print v1.is_orthogonal(v2)
print

print "Three"
v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])
print "Parallel: "
print v1.is_parallel(v2)
print "Orthogonal: "
print v1.is_orthogonal(v2)
print

print "Four"
v1 = Vector([2.118, 4.827])
v2 = Vector([0, 0])
print "Parallel: "
print v1.is_parallel(v2)
print "Orthogonal: "
print v1.is_orthogonal(v2)

