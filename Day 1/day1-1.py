from pandas import read_csv

currentLocation = [0, 0]
currentDirection = 90
directions = []

with open('C:/users/me4219/advent/day1-1input.txt') as file:
    data = read_csv(file)

for row in data:
    directions.append(row.strip().split('.')[0])

for item in directions:
    # Turn left or right.
    if item[0] == 'R':
        currentDirection -= 90
    elif item[0] == 'L':
        currentDirection += 90

    # Keep directions within 0, 90, 180, 270.
    # Since I'm adjusting this every time,
    # it'll never get higher than 360 or lower than -90.
    if currentDirection == 360:
        currentDirection = 0
    if currentDirection == -90:
        currentDirection = 270

    # Distance to add if facing E, N, W, S.
    if currentDirection == 0:
        currentLocation[0] += item[1:]
    elif currentDirection == 90:
        currentLocation[1] += item[1:]
    elif currentDirection == 180:
        currentLocation[0] -= item[1:]
    elif currentDirection == 270:
        currentLocation[1] -= item[1:]

distance = abs(int(currentLocation[0])) + abs(int(currentLocation[1]))
print(distance)
