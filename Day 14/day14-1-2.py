from hashlib import md5
from re import search, findall

salt = 'ihaygndm'
index = 0
triples = {}
myKeys = []
keyIndices = []
partTwo = True

while len(myKeys) < 72:
    hashed = md5((salt + str(index)).encode('utf-8')).hexdigest().lower()
    if partTwo:
        for _ in range(2016):
            hashed = md5(hashed.encode('utf-8')).hexdigest().lower()
    triple = search(r'(.)\1{2}', hashed)
    quint = findall(r'(.)\1{4}', hashed)
    if triple:
        triples[index]={'hashed': hashed, 'triplet': triple.group(0)}
    if len(quint) > 0:
        for item in triples:
            if (index - item - 1) in range(1000):
                for match in quint:
                    trip = match + match + match
                    if triples[item]['triplet'] == trip:
                        myKeys.append(triples[item]['hashed'])
                        keyIndices.append(item)
    index += 1

keyIndices.sort(key=int)
print(keyIndices[63])
