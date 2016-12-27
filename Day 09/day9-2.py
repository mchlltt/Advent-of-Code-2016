# This solution is not my own work, though it follows a similar approach to the one I took in my attempts.

def decompressed_length(data):
    i = 0
    total = 0
    while i < len(data):
        if data[i] == '(':
            i += 1
            newString = ''
            while data[i] != ')':
                newString += data[i]
                i += 1
            length = int(newString.split('x')[0])
            amount = int(newString.split('x')[1])
            total += amount*decompressed_length(data[i+1:i+length+1])
            i += length
        else:
            total += 1
        i += 1
    return total


fileName = "day9-input.txt"
file = open(fileName).read()
print(decompressed_length(file))