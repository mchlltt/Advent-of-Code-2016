import re

ipFile = 'day7-input.txt'
ips = open(ipFile).read().splitlines()
splitIPs = []
abas = []
mirroreds = []
ssl = []

# For each IP, split on square brackets.
for ip in ips:
    ip = re.split('\[|\]', ip)
    splitIPs.append(ip)

# For each IP
for k in range(len(splitIPs)):
    # Get an empty list ready.
    thisIPabas = []
    # For each index in the IP
    for j in range(len(splitIPs[k])):
        # build up thisIPabas
        # For the letters in the index
        for i in range(len(splitIPs[k][j]) - 2):
            # Check if there are any aba's.
            if splitIPs[k][j][i:i+3] == splitIPs[k][j][i:i+3][::-1]:
                # Then make sure those aren't aaa's.
                if splitIPs[k][j][i] != splitIPs[k][j][i+1]:
                    # For any abas, add j and the aba to list of possibilities.
                    aba = [j, splitIPs[k][j][i:i+3]]
                    thisIPabas.append(aba)
    # Add the IP's index + any aba item segments + abas themself.
    abas.append([k, thisIPabas])

# For each possibly SSL supporter (aba + bab),
for possibility in abas:
    thisIPmirrored = []
    # If we had more than one aba,
    if len(possibility[1]) > 1:
        # Check whether an aba's have corresponding bab's.
        for i in range(len(possibility[1])):
            bab = possibility[1][i][1][1] + possibility[1][i][1][0] + possibility[1][i][1][1]
            # For each other aba, check if it is the bab.
            for j in range(i, len(possibility[1])):
                # If so, add the indices of the match to thisIPmirrored.
                if bab == possibility[1][j][1]:
                    thisIPmirrored.append([possibility[1][i][0], possibility[1][j][0]])
        # If we had any aba/bab pairs, add the IP index + aba/bab pair indices to mirroreds.
        if len(thisIPmirrored) > 0:
            mirroreds.append([possibility[0], thisIPmirrored])

# OK! Now we are down to just aba/bab pairs. Let's check whether they happen in opposite sections.
# For each IP,
for grouping in mirroreds:
    # For each pair,
    for couple in range(len(grouping[1])):
        # Check whether you have an even/odd pair. The sum of the mod of the two indices will be 1 if so.
        if (grouping[1][couple][0] % 2 + grouping[1][couple][1] % 2) == 1:
            # If so, this IP supports SSL! Add the IP's index to ssl.
            ssl.append(grouping[0])

# We use set(ssl) to make sure any duplicate IPs do not get double-counted.
print(len(set(ssl)))
