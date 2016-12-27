code = '01000100010010111'
data = code

# Part One
# diskLength = 272

# Part Two
diskLength = 35651584

while len(data) < diskLength:
    b = data[::-1]
    c = ''
    for i in range(len(b)):
        if b[i] == '0':
            c += '1'
        else:
            c += '0'
    data = data + '0' + c

data = data[:diskLength]

while len(data) % 2 == 0:
    checksum = ''
    i = 0
    while i < len(data):
        if data[i] == data[i + 1]:
            checksum += '1'
        else:
            checksum += '0'
        i += 2
    data = checksum

print(data)
