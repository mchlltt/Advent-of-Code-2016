rawTriangles = "day3-input.txt"
triangles = open(rawTriangles).read().splitlines()
invalid = 0
valid = 0

for triangle in triangles:
    # Convert triangle to list.
    triangle = triangle.strip()
    triangle = triangle.replace(' ',',')
    triangle = triangle.replace(',,,',',')
    triangle = triangle.replace(',,', ',')
    triangle = triangle.split(',')

    # A triangle is only possible if the sum of any two of its sides is
    # strictly greater than the length of the third side.
    if (int(triangle[0]) + int(triangle[1])) <= int(triangle[2]):
        invalid += 1
    elif (int(triangle[1]) + int(triangle[2])) <= int(triangle[0]):
        invalid += 1
    elif (int(triangle[0]) + int(triangle[2])) <= int(triangle[1]):
        invalid += 1
    else:
        valid += 1

print(valid)