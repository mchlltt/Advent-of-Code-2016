from math import ceil, floor

elfCount = 3018458
# elfCount = 5
elves = []

for i in range(elfCount):
    elves.append(i + 1)

elfID = 1
while True:
    if elfID in elves:

        elfIndex = elves.index(elfID)

        numTargets = len(elves) - 1
        if numTargets == 1:
            print(elfID)
            break

        if numTargets % 2 == 1:
            offset = int(ceil(numTargets/2))
        else:
            offset = int(numTargets/2)

        if elfIndex + offset > len(elves) - 1:
            offset -= len(elves)

        targetElf = elves[elfIndex + offset]
        elves.remove(targetElf)

    if elfID == elfCount:
        elfID = 1
    else:
        elfID += 1