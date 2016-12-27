from itertools import product


# Function via https://www.python.org/doc/essays/graphs/
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in  graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newPath = find_shortest_path(graph, node, end, path)
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath
    return shortest


def find_all_paths(graph, start, end, path2=[]):
    path2 = path2 + [start]
    if start == end:
        return [path2]
    paths = []
    for node in graph[start]:
        if node not in path2:
            newPaths = find_all_paths(graph, node, end, path2)
            for newPath in newPaths:
                paths.append(newPath)
    return paths


def find_neighbors(graph, start, neighbors=set()):
    neighbors.add(start)
    for node in graph[start]:
        if node not in neighbors:
            find_neighbors(graph, node, neighbors)
    return neighbors


def get_key_x(item):
    return item[0]


def get_key_y(item):
    return item[1]

puzzleInput = 1364
graph = {}
cleanGraph = {}

for item in product(range(52), range(52)):
    binaryCoord = str(bin(item[0] * item[0] + 3 * item[0] + 2 * item[0] * item[1] + item[1] + item[1] * item[1] + 1364))[2:]
    coord = 0
    for digit in binaryCoord:
        coord += int(digit)
    coord %= 2
    if coord == 1:
        graph[item] = None
    else:
        graph[item] = []

for item in graph:
    if graph[item] is not None:
        if item[0] > 0:
            if graph[(item[0] - 1, item[1])] is not None:
                graph[item].append((item[0] - 1, item[1]))
        if item[1] > 0:
            if graph[(item[0], item[1] - 1)] is not None:
                graph[item].append((item[0], item[1] - 1))
        if item[0] < 51:
            if graph[(item[0] + 1, item[1])] is not None:
                graph[item].append((item[0] + 1, item[1]))
        if item[1] < 51:
            if graph[(item[0], item[1] + 1)] is not None:
                graph[item].append((item[0], item[1] + 1))

for item in graph:
    if graph[item] is not None:
        if len(graph[item]) > 0:
            cleanGraph[item] = graph[item]

path = find_shortest_path(cleanGraph, (1, 1), (31,39))
neighbors = find_neighbors(cleanGraph, (1, 1))

# Subtract one because we don't want to include (1,1) as a 'step.'
print('Part One: ' + str(len(path) - 1))

reachable = {(1, 1)}
processed = {(1, 1)}

# Sort by y then x coordinates so that we can process the farthest away points first and work our way in.
# This will allow us to take full advantage of the recursive processing.

graphIterator = sorted(cleanGraph, key=get_key_y, reverse=True)
graphIterator.sort(key=get_key_x, reverse=True)

# Iterate through this sorted list of keys.
for point in graphIterator:
    # If the point is a neighbor of (1, 1),
    if point in neighbors:
        # If this point has not already been processed, find all paths from (1, 1)
        if point not in processed:
            allPaths = find_all_paths(cleanGraph, (1, 1), point)
            # Mark any points within 50 steps in any of these paths as processed and reachable.
            for path in allPaths:
                for step in path[:50]:
                    reachable.add(step)
                    processed.add(step)

print('Part Two: ' + str(len(reachable)))
