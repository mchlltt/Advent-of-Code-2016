rawTriangles = "day3-input.txt"
triangles = open(rawTriangles).read().splitlines()
newTriangles = []
newTriangle0 = []
newTriangle1 = []
newTriangle2 = []
valid = 0
invalid = 0

for triangle in triangles:
    # Convert triangle to list.
    triangle = triangle.strip()
    triangle = triangle.replace(' ',',')
    triangle = triangle.replace(',,,',',')
    triangle = triangle.replace(',,', ',')
    triangle = triangle.split(',')

    # Add the three items in triangle to three different new triangles.
    newTriangle0.append(triangle[0])
    newTriangle1.append(triangle[1])
    newTriangle2.append(triangle[2])

    # Once your new triangles have 3 sides, add them to the list of new triangles and then reset them.
    if len(newTriangle0) == 3:
        newTriangles.append(newTriangle0)
        newTriangles.append(newTriangle1)
        newTriangles.append(newTriangle2)
        newTriangle0 = []
        newTriangle1 = []
        newTriangle2 = []

# A triangle is only possible if the sum of any two of its sides is
# strictly greater than the length of the third side.
for triangle in newTriangles:
    if (int(triangle[0]) + int(triangle[1])) <= int(triangle[2]):
        invalid += 1
    elif (int(triangle[1]) + int(triangle[2])) <= int(triangle[0]):
        invalid += 1
    elif (int(triangle[0]) + int(triangle[2])) <= int(triangle[1]):
        invalid += 1
    else:
        valid += 1

print(valid)