"""
3
4
3 10 8 14
1 11 12 12
6 2 3 9

yes

repeat searching from the start for no more than every tile.
- check every tile and
"""
rows = int(input().strip())
columns = int(input().strip())
table = []
for i in range(rows):
    table.append([int(v) for v in input().strip().split(" ")])

check_table = []
for i in range(rows):
    check_table.append([0]*columns)

def place_markers(table, check_table, marker_row, marker_colum):
    if check_table[marker_row-1][marker_colum-1] == 1:
        #marker already placed, do nothing
        return
    check_table[marker_row-1][marker_colum-1] = 1 #turn newly arrived one into 1
    marker_number = table[marker_row-1][marker_colum-1] #find the value
    for possible_moves in find_factors(marker_number, len(check_table), len(check_table[0])):
    #goes to each new location and searches from there until it encounters another 1
        new_marker_row = possible_moves[0] #the row of the next
        new_marker_column = possible_moves[1] #the column of the next
        place_markers(table, check_table, new_marker_row, new_marker_column)
        #Repeat (change to 1, search new moves from there)

def find_factors(number, max_row, max_col):
    max_1 = max(max_row, max_col)
    max_2 = min(max_row, max_col)
    factors = []
    for i in range(1, max_1+1):
        if number % i == 0 and number // i <= max_2:
            if i <= max_row and (number // i) <= max_col:
                factors.append([i, number//i])
            if (number // i) <= max_row and i <= max_col:
                factors.append([number//i, i])
    return factors
#factors


place_markers(table, check_table, 1, 1)
if check_table[-1][-1] == 1:
    print("yes")
else:
    print("no")
    #print(find_factors(12, 3,4))