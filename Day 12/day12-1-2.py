codeFile = 'day12-input.txt'
rawCode = open(codeFile).read().splitlines()

# Part One initial values
# register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

# Part Two initial values
register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

i = 0

while i < len(rawCode):
    line = rawCode[i].split(' ')
    if line[0] == 'cpy':
        if line[1] in register.keys():
            register[line[2]] = register[line[1]]
        else:
            register[line[2]] = int(line[1])
        i += 1
    elif line[0] == 'inc':
        register[line[1]] += 1
        i += 1
    elif line[0] == 'dec':
        register[line[1]] -= 1
        i += 1
    elif line[0] == 'jnz':
        if line[1] in register.keys():
            if register[line[1]] != 0:
                i += int(line[2])
            else:
                i += 1
        elif int(line[1]) != 0:
            i += int(line[2])
        else:
            i += 1
    else:
        i += 1

print(register['a'])
