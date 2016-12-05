import hashlib

# My door ID
id = 'wtnhxymk'

# Set initial index to 0 and first password to an empty string.
index = 0
firstPassword = ''

# Until we've added 8 characters total to the password,
while len(firstPassword) < 8:
    # Hash the door ID + index
    toHash = id + str(index)
    hashed = hashlib.md5(toHash)
    hex = hashed.hexdigest()
    # Increment index.
    index += 1
    # Check whether the first 5 characters of the hexdigest are 0s.
    if hex[:5] == '00000':
        # If so, add the 6th character to the password.
        firstPassword += str(hex[5])

# This is already a string, so print it as-is.
print(firstPassword)

# Reset index to 0.
index = 0
# Create a dummy list of 8 items.
secondPassword = [0, 0, 0, 0, 0, 0, 0, 0]
# Create a list with the indices for a list of 8 items.
availableIndices = [0, 1, 2, 3, 4, 5, 6, 7]

# Until we've filled all 8 indices,
while len(availableIndices) > 0:
    # Hash the same as above.
    toHash = id + str(index)
    hashed = hashlib.md5(toHash)
    hex = hashed.hexdigest()
    index += 1
    # Still check whether the first 5 characters of the hexdigest are 0s.
    if hex[:5] == '00000':
        # But then, if the 6th character can be coerced to integer,
        try:
            int(hex[5])
            # Check whether that integer is in availableIndices.
            if int(hex[5]) in availableIndices:
                # If so, set the password at that index to the 7th character.
                secondPassword[int(hex[5])] = hex[6]
                # And remove that index from the available indices.
                availableIndices.remove(int(hex[5]))
        # If the 6th character was not numeric, pass.
        except:
            pass

# Join the password list and print it.
print(''.join(secondPassword))
