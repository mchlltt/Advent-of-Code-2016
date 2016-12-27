import re

ipFile = 'day7-input.txt'
ips = open(ipFile).read().splitlines()
splitIPs = []
valid = []
invalid = []

# For each IP, split on square brackets.
for ip in ips:
    ip = re.split('\[|\]', ip)
    splitIPs.append(ip)

# For each IP,
for k in range(len(splitIPs)):
    # For each item in the IP,
    for j in range(len(splitIPs[k])):
        # For the letters in the item,
        for i in range(len(splitIPs[k][j]) - 3):
            # If a letter and the subsequent letter are the same as the third and fourth letter reversed,
            if splitIPs[k][j][i:i+2] == splitIPs[k][j][i+2:i+4][::-1]:
                # And it's not because it's all 4 the same letter,
                if splitIPs[k][j][i] != splitIPs[k][j][i + 1]:
                    # Check where the abba happens.
                    # If it's in an even word, it's potentially valid.
                    if j in [0, 2, 4, 6]:
                        # Add the ip, joined, to valid.
                        valid.append(''.join(splitIPs[k]))
                    # If it's in an odd word, it's definitely invalid.
                    elif j in [1, 3, 5, 7]:
                        # Add the ip, joined, to invalid.
                        invalid.append(''.join(splitIPs[k]))

# Since an IP could contain multiple abba's, we need to check the potentially valid IPs
# and make sure they're not also in invalid. If they're in invalid, remove them from valid.
for str in valid:
    if str in invalid:
        valid.remove(str)

# We use set(valid) to make sure any duplicate IPs do not get double-counted.
print(len(set(valid)))