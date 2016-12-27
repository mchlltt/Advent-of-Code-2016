from pandas import read_csv

currentLocation = [0, 0]
currentDirection = 90
directions = []
locations = ['0,0']
uniques = []

with open('day1-1input.txt') as file:
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
    # Add distance incrementally to make sure we get each step.
    # Since we're doing taxicab distance with only whole blocks, this is sufficient.
    if currentDirection == 0:
        for _ in range(int(item[1:])):
            currentLocation[0] += 1
            locations.append(str(currentLocation))
    elif currentDirection == 90:
        for _ in range(int(item[1:])):
            currentLocation[1] += 1
            locations.append(str(currentLocation))
    elif currentDirection == 180:
        for _ in range(int(item[1:])):
            currentLocation[0] -= 1
            locations.append(str(currentLocation))
    elif currentDirection == 270:
        for _ in range(int(item[1:])):
            currentLocation[1] -= 1
            locations.append(str(currentLocation))

# Add the locations to a new list until you hit the first duplicate.
# That's your answer!
for item in locations:
    if item not in uniques:
        uniques.append(item)
    else:
        correctLocation = item
        break

# Convert back to pair of integers.
correctLocation = correctLocation.replace('[', '')
correctLocation = correctLocation.replace(']', '')

distance = abs(int(correctLocation.split(',')[0])) + abs(int(correctLocation.split(',')[1]))
print(distance)
