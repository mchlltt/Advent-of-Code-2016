from collections import Counter

rows = ['^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.']
width = len(rows[0])
traps = ['^^.', '.^^', '^..', '..^']

while len(rows) < 400000:
    previous = rows[-1]
    newRow = ''
    for i in range(width):
        info = ''
        if i == 0:
            info += '.'
        else:
            info += previous[i - 1]
        info += previous[i]
        if i == width - 1:
            info += '.'
        else:
            info += previous[i + 1]
        if info in traps:
            newRow += '^'
        else:
            newRow += '.'
    rows.append(newRow)

tiles = Counter(''.join(rows)).most_common()

print(tiles)
