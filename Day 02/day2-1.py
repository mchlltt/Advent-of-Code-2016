rawDirections = "day2-input.txt"
directions = open(rawDirections).read().splitlines()
code = []
keys = []

keyMap = {
    "[-1, 1]": 1,
    "[0, 1]": 2,
    "[1, 1]": 3,
    "[-1, 0]": 4,
    "[0, 0]": 5,
    "[1, 0]": 6,
    "[-1, -1]": 7,
    "[0, -1]": 8,
    "[1, -1]": 9
}

for item in directions:
    # Start at 5
    currentKey = [0, 0]
    # For each letter,
    for letter in item:
        # Store previous key.
        previousKey = currentKey[:]

        # Move the correct direction
        if letter == "L":
            currentKey[0] -= 1
        elif letter == "R":
            currentKey[0] += 1
        elif letter == "U":
            currentKey[1] += 1
        elif letter == "D":
            currentKey[1] -= 1

        # Then check if you actually can move that direction
        # before going to the next letter.
        if (abs(currentKey[0]) == 2) | (abs(currentKey[1]) == 2):
            # If you can't, stay on the previous key.
            currentKey = previousKey
    code.append(currentKey)

# Map from coordinates back to keys.
for item in code:
    key = keyMap.get(str(item))
    keys.append(key)

print(keys)
