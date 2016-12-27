rules = ['Disc #1 has 7 positions; at time=0, it is at position 0.',
         'Disc #2 has 13 positions; at time=0, it is at position 0.',
         'Disc #3 has 3 positions; at time=0, it is at position 2.',
         'Disc #4 has 5 positions; at time=0, it is at position 2.',
         'Disc #5 has 17 positions; at time=0, it is at position 0.',
         'Disc #6 has 19 positions; at time=0, it is at position 7.',
         'Disc #7 has 11 positions; at time=0, it is at position 0.']

time = -1

while True:
    time += 1
    if (time + 1) % 7 == 0:
        if (time + 2) % 13 == 0:
            if (2 + time + 3) % 3 == 0:
                if (2 + time + 4) % 5 == 0:
                    if (time + 5) % 17 == 0:
                        if (7 + time + 6) % 19 == 0:
                            print(time)
                            break

while True:
    time += 1
    if (time + 1) % 7 == 0:
        if (time + 2) % 13 == 0:
            if (2 + time + 3) % 3 == 0:
                if (2 + time + 4) % 5 == 0:
                    if (time + 5) % 17 == 0:
                        if (7 + time + 6) % 19 == 0:
                            if (time + 7) % 11 == 0:
                                print(time)
                                break
