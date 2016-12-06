from collections import Counter

rawMessages = "day6-input.txt"
messages = open(rawMessages).read().splitlines()
letters = ['','','','','','','','']
answer = ''

for message in messages:
    index = 0
    for letter in message:
        letters[index] += letter
        index += 1

# Part One answer.
# for item in letters:
#     answer += Counter(item).most_common()[0][0]

# Part Two answer.
for item in letters:
    answer += Counter(item).most_common()[-1][0]

print(answer)
