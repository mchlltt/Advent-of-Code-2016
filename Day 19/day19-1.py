elfCount = 3018458
giftCount = {}

for i in range(elfCount):
    giftCount[i + 1] = 1

index = 1
while True:
    if giftCount[index] > 0:
        j = 1
        if index == elfCount:
            j -= elfCount
        while giftCount[index + j] == 0:
            j += 1
            if (index + j) > elfCount:
                j -= elfCount
        giftCount[index] += giftCount[index + j]
        giftCount[index + j] = 0
        if giftCount[index] == elfCount:
            print(index)
            break
    if index < elfCount:
        index += 1
    else:
        index = 1