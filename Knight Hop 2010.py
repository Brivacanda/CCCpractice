start = input()
start = start.replace(" ", "")
start = [int(start[0]), int(start[1])]

end = input()
end = end.replace(" ", "")
end = [int(end[0]), int(end[1])]

def find_steps(starting_cords, ending_cords):
    #difference
    dif_x = abs(starting_cords[0]-ending_cords[0])
    dif_y = abs(starting_cords[1] - ending_cords[1])

    if dif_x == 0 and dif_y == 0:
        return 0
    if (dif_x == 1 and dif_y == 2) or (dif_y == 1 and dif_x == 2):
        return 1
    elif (dif_x == 1 and dif_y == 0) or (dif_x == 0 and dif_y == 1):
        return 3
    elif dif_x == 1 and dif_y == 1:
        return 2
    elif (dif_x == 2 and dif_y == 0) or (dif_x == 0 and dif_y == 2):
        return 2
    else:
        #return 4
        if dif_x > dif_y:
            return 1 + find_steps([dif_x-2, dif_y-1], [0,0])
        else:
            return 1+ find_steps([dif_x -1, dif_y -2], [0,0])

print(find_steps(start, end))