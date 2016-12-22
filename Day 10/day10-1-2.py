instructionFile = "day10-input.txt"
instructions = open(instructionFile).read().splitlines()
splitItems = []
initialItems = []
chipStatus = {}
outputs = {}

for item in instructions:
    itemArray = item.split(' ')
    itemArray = [x for x in itemArray if x != 'and' and x != 'to']
    if itemArray[0] == 'value':
        initialItems.append(itemArray)
    else:
        splitItems.append(itemArray)

for item in initialItems:
    value = int(item[1])
    bot = item[4]
    if bot not in chipStatus.keys():
        chipStatus[bot] = [value]
    else:
        chipStatus.get(bot).append(value)

keepGoing = True

while keepGoing:
    keepGoing = False
    for item in list(chipStatus):
        if len(chipStatus[item]) == 2:
            keepGoing = True
            chipStatus[item].sort(key=int)
            if chipStatus[item] == [17, 61]:
                print(item)
            instruction = [x for x in splitItems if x[1] == item][0]
            if instruction[4] == 'bot':
                if instruction[5] not in chipStatus.keys():
                    chipStatus[instruction[5]] = [chipStatus[item][0]]
                else:
                    chipStatus.get(instruction[5]).append(chipStatus[item][0])
            else:
                if instruction[5] not in outputs.keys():
                    outputs[instruction[5]] = [chipStatus[item][0]]
                else:
                    outputs.get(instruction[5]).append(chipStatus[item][0])
            if instruction[7] == 'bot':
                if instruction[8] not in chipStatus.keys():
                    chipStatus[instruction[8]] = [chipStatus[item][1]]
                else:
                    chipStatus.get(instruction[8]).append(chipStatus[item][1])
            else:
                if instruction[8] not in outputs.keys():
                    outputs[instruction[8]] = [chipStatus[item][1]]
                else:
                    outputs.get(instruction[8]).append(chipStatus[item][1])
            chipStatus[item] = []

print(outputs['0'][0] * outputs['1'][0] * outputs['2'][0])
