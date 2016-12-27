from numpy import zeros, sum

instructionsFile = "day8-input.txt"
rawInstructions = open(instructionsFile).read().splitlines()
instructions = []
# Create array of zeros.
board = zeros((6, 50))

# Simplify instructions.
for item in rawInstructions:
    # Split on spaces.
    item = item.split(' ')
    # If there are two words in the item, it's rect. Make the item 'rect', A, B.
    if len(item) == 2:
        item[1] = item[1].split('x')
        item = [item[0], item[1][0], item[1][1]]
    # If there are five words in the item, it's rotate. Make the item 'row'/'column', A, B.
    elif len(item) == 5:
        item[2] = item[2].split('=')[1]
        item = [item[1], item[2], item[4]]
    instructions.append(item)

# Walk through the cleaned instructions.
for item in instructions:
    # If the direction is rect, make the AxB rectangle's values 1.
    if item[0] == 'rect':
        board[:int(item[2]), :int(item[1])] = 1
    # If the direction is row,
    elif item[0] == 'row':
        # Use the offset value to determine at which point the values will wrap.
        offsetUp = int(item[2])
        offsetDown = 50 - int(item[2])
        newRow = zeros(50)
        newRow[:offsetUp] = board[int(item[1]), offsetDown:]
        newRow[offsetUp:] = board[int(item[1]), :offsetDown]
        # Replace the row in question with the modified row.
        board[int(item[1]), :] = newRow
    elif item[0] == 'column':
        # Use the offset value to determine at which point the values will wrap.
        offsetUp = int(item[2])
        offsetDown = 6 - int(item[2])
        newColumn = zeros(6)
        newColumn[:offsetUp] = board[offsetDown:, int(item[1])]
        newColumn[offsetUp:] = board[:offsetDown, int(item[1])]
        # Replace the column with the modified column.
        board[:, int(item[1])] = newColumn

# Print the sum of all the 1's and 0's.
print(sum(board))

# Convert the dtype to string.
board = board.astype('str')

# Replace 1's with blocks and 0's with blanks.
board[board == '1.0'] = '█'
board[board == '0.0'] = ' '

# Print each row joined.
for i in range(6):
    print(''.join(board[i, :]))
