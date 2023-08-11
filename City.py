import bpy
from random import randint

first = True
X = 90
Y = 130
SIZE = 4
y = 1
sum = 0
for i in range(35):
    z = randint(1,10)
    bpy.ops.mesh.primitive_cube_add(size=SIZE, location=(X, Y - (SIZE/2 + sum + y*SIZE/2), SIZE/2*z), scale=(1, y, z))
    sum += SIZE*y
    y = randint(1,3)           