from collections import Counter
from string import ascii_lowercase

rawRooms = "day4-input.txt"
rooms = open(rawRooms).read().splitlines()

sum = 0
realRooms = []
realNums = []
decodedNames = []
alphabet = ascii_lowercase + ascii_lowercase

# For each room,
for room in rooms:
    letters = []
    frequencies = []
    sortedLetters = []
    ties = []
    numbers = []
    room = room.replace(']','')
    room = room.split('[')

    # Get letters.
    for letter in room[0]:
        if letter.isalpha():
            letters.append(letter)

    # Get numbers
    for number in room[0]:
        if number.isdigit():
            numbers.append(number)

    # Convert number to integer.
    number = int(''.join(numbers))

    # Alias Counter on letters.
    frequency = Counter(letters).most_common()

    # Split Counter into list of lists.
    for pair in frequency:
        frequencies.append(pair[1])

    # The pairs are already ordered by most common letters.
    # What we're doing here is going through and adding
    # either the letter itself when it is the only one with a given frequency
    # or an alphabetized list of all the letters with the same frequency.
    # Once we've reached a new frequency (frequency[0]), the tie is over and we alphabetize/add that list.

    # Initially, there is no tie.
    tie = False

    for i in range(len(frequencies)):
        # What we do for all but the last frequency pair.
        if i < len(frequencies) - 1:
            if frequencies[i] > frequencies[i+1]:
                # Anytime its greater, there's definitely no ongoing tie, so end the tie.
                tie = False
                # If there was a list of ties going, add the letter, sort alpha, and append ties to sortedLetters.
                if len(ties) > 0:
                    ties.append(frequency[i][0])
                    ties = sorted(ties)
                    sortedLetters.extend(ties)
                    ties = []
                # If there weren't any ties going, just add the letter alone.
                else:
                    sortedLetters.append(frequency[i][0])
            # If it's not greater, it's either a new or ongoing tie. Make sure tie is true and add the letter to ties.
            else:
                tie = True
                ties.append(frequency[i][0])
        else:
            # For the last frequency pair, we either add it to ties and add ties,
            if tie:
                ties.append(frequency[i][0])
                ties = sorted(ties)
                sortedLetters.extend(ties)
            # Or we add it by itself.
            else:
                sortedLetters.append(frequency[i][0])

    # The first five letters in the sortedLetters array is our checksum.
    correctCheckSum = ''.join(sortedLetters[:5])
    # The portion of the room name that was in brackets is our supposed checksum.
    givenCheckSum = room[1]

    # If the supposed checksum is correct,
    if correctCheckSum == givenCheckSum:
        # add the sector number to the sum of the sector numbers
        sum += number
        # and add the room name and sector number to a list to be considered in the next portion.
        realRooms.append(room[0])
        realNums.append(number)

# The sum is our first half answer, so print it.
print(sum)

# Now we're going to run through all of the real room names.
for i in range(len(realRooms)):
    decoded = ''
    cypherNumberRaw = realNums[i]
    cypherName = realRooms[i]
    # Reduce the sector number with modulo.
    cypherNumber = cypherNumberRaw % 26

    for letter in cypherName:
        # Dashes go to spaces.
        if letter == '-':
            decoded += ' '

        # Numbers are removed
        elif letter.isdigit():
            decoded += ''
        # Letters have their index in the alphabet incremented by cypherNumber
        # alphabet is actually the alphabet twice in a row so that it is 52 letters long.
        # this allows a z with a cypherNumber of 26 (so index of 52) to be within alphabet's length.
        else:
            decoded += alphabet[alphabet.index(letter) + cypherNumber]

        # If 'north' is in the decoded name, print the name and its sector number.
        # The exact correct room name wasn't in the question, so this lets us select the correct answer.
    if 'north' in decoded:
        print(decoded)
        print(cypherNumberRaw)
