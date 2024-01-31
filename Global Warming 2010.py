def create_sequence(start, pattern, length):
    sequence = [start]
    for i in range(length-1):
        sequence.append(sequence[-1]+ pattern[i%len(pattern)])

    return [str(value) for value in sequence]


temp = (input()).strip()
while temp != '0':
    difs = []
    temp = temp.split(" ")
    length = int(temp[0])
    temp = temp[1:][:length]
    #temp.remove(temp[0])
    for i in range(1, len(temp)):
        difs.append(int(temp[i])-int(temp[i-1]))

    match = []
    test = 1
    if len(temp) == 1:
        print("0")
    else:
        match = create_sequence(int(temp[0]), difs[0:test], len(temp))
        while " ".join(match) != " ".join(temp):
            test += 1
            match = create_sequence(int(temp[0]), difs[0:test], len(temp))

        print(test)
    temp = (input()).strip()

#print(create_sequence(3, [1,2], 7))
#7 3 4 6 4 5 7 5