# NB: 'range' is used in the common sense throughout this file, not as a reference to the Python built-in.
# Read input.
IPs = open('day20-input.txt').read().splitlines()

# Initialize variables.
allowed = []
i = 0
j = 1


# Sorting function.
def get_key(item):
    return int(item.split('-')[0])


# Sort by starting number of each range.
IPs.sort(key=get_key)

# Initialize ranges with first range of banned IPs.
ranges = [(int(IPs[0].split('-')[0]), int(IPs[0].split('-')[1]))]

# Then step through all the rest of the IP ranges.
while j < len(IPs):

    # Get this range and previous range in ranges.
    previousStart = ranges[-1][0]
    previousEnd = ranges[-1][1] + 1
    start = int(IPs[j].split('-')[0])
    end = int(IPs[j].split('-')[1])

    # If the previous range in ranges overlaps with,
    if start <= previousEnd:
        # but does not contain, this range
        if end >= previousEnd:
            # change the end point of the previous range to the endpoint of this range.
            ranges[-1] = [previousStart, end]
    # Where the previous range does not overlap,
    else:
        # add any IPs in between the two ranges to 'allowed,'
        for item in range(previousEnd, start):
            allowed.append(item)
        # and add this new range to ranges.
        ranges.append([start, end])
    # Increment j.
    j += 1

# Print results.
print('First allowed: ' + str(allowed[0]))
print('Number allowed: ' + str(len(allowed) + ranges[-1][1] - 4294967295))