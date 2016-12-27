fileName = "day9-input.txt"
file = open(fileName).read()
openParen = []
closeParen = []
pairs = []
operations = []
splitOps = []
decompressed = ''

for i in range(len(file)):
    if file[i] != '(' and file[i] != ')':
        pass
    elif file[i] == '(':
        openParen.append(i)
    elif file[i] == ')':
        closeParen.append(i)

for j in range(len(openParen)):
    pairs.append([openParen[j],closeParen[j]])

for k in pairs:
    operation = file[k[0] + 1:k[1]]
    operations.append(operation)

for l in operations:
    l = l.split('x')
    splitOps.append(l)

p = 0
i = 0
nextParens = pairs[0]
nextOps = splitOps[0]

while i < len(file):
    if i != nextParens[0]:
        decompressed += file[i]
        i += 1
    else:
        for _ in range(int(nextOps[1])):
            decompressed += str(file[nextParens[1] + 1:nextParens[1] + int(nextOps[0]) + 1])
        i = nextParens[1] + int(nextOps[0]) + 1
        while nextParens[0] < i and p + 1 < len(pairs):
            p += 1
            nextParens = pairs[p]
            nextOps = splitOps[p]

print(len(decompressed))
