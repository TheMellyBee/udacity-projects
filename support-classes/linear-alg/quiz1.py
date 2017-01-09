from vector import Vector

vector1 =  Vector([8.218,-9.341])
vector2 =  Vector([-1.129, 2.111])

print "One"
print vector1.plus(vector2)

print "Two"
vector3 = Vector([7.119, 8.215])
print vector3.minus(Vector([-8.223, 0.878]))

print "Three"
vector4 = Vector([1.671, -1.012, -0.318])
print vector4.scalar_mult(7.41)
