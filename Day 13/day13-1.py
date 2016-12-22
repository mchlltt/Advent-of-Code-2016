from itertools import product

puzzleInput = 1364
# x*x + 3*x + 2*x*y + y + y*y
graph = {}

for item in product(range(50), range(50)):
    binaryCoord = str(bin(item[0] * item[0] + 3 * item[0] + 2 * item[0] * item[1] + item[1] + item[1] * item[1] + 1364))[2:]
    coord = 0
    for digit in binaryCoord:
        coord += int(digit)
    coord %= 2
    if coord == 1:
        graph[item] = []
    else:
        graph[item] = [0]

print(graph)

for item in graph:
    if len(graph[item]) != 0:
        if item[0] > 0:
            if len(graph[(item[0] - 1, item[1])]) != 0:
                graph[item].append((item[0] - 1, item[1]))
        if item[1] > 0:
            if len(graph[(item[0], item[1] - 1)]) != 0:
                graph[item].append((item[0], item[1] - 1))
        if item[0] < 49:
            if len(graph[(item[0] + 1, item[1])]) != 0:
                graph[item].append((item[0] + 1, item[1]))
        if item[1] < 49:
            if len(graph[(item[0], item[1] + 1)]) != 0:
                graph[item].append((item[0], item[1] + 1))

print(graph)

# https://www.python.org/doc/essays/graphs/
