word = input().strip()
height = int(input().strip())
width = int(input().strip())

puzzle = []

for i in range(height):
    row = input().strip()
    puzzle.append(row.split(" "))



total = 0

"""
diagonal search once start of target is detected
- gives x and y of cur pos and options of where to look as well as targets
    - if a type of check (like up) in options check that
    - check if x and y are less than border
        - checks each direction
        - if found keep only that option and recursive function
        - removing one letter after it is found until everything is found
            - return 1
        - return 0 is not found

once done once set the last letter to 0 which is then changed back after checking there are no other routes to make the word
"""

def available_directions(table, x, y, target):  # remove first from target when initializing
    width = len(table[0])
    height = len(table)
    found = 0
    # check bottom right
    if (x + 1 < width and y + 1 < height) and (table[y + 1][x + 1] == target[0]):
        # if direction available check that direction. does not move there just begins check
        found += check_directional_path(table, x, y, 1, 1, target)
    # check bottom left
    if (x - 1 >= 0 and y + 1 < height) and (table[y + 1][x - 1] == target[0]):
        found += check_directional_path(table, x, y, -1, 1, target)
    # check top left
    if (x - 1 >= 0 and y - 1 >= 0) and (table[y - 1][x - 1] == target[0]):
        found += check_directional_path(table, x, y, -1, -1, target)
    # check top right
    if (x + 1 < width and y - 1 >= 0) and (table[y - 1][x + 1] == target[0]):
        found += check_directional_path(table, x, y, 1, -1, target)
    #check left
    if (x-1 >= 0) and (table[y][x-1] == target[0]):
        found += check_directional_path(table, x, y, -1, 0, target)
    #check right
    if (x + 1 < width) and (table[y][x+1] == target[0]):
        found += check_directional_path(table, x, y, 1, 0, target)
    #check up
    if (y - 1 >= 0) and (table[y-1][x] == target[0]):
        found += check_directional_path(table, x, y, 0, -1, target)
    #check down
    if (y + 1 < height) and (table[y+1][x] == target[0]):
        found += check_directional_path(table, x, y, 0, 1, target)
    #print(found)
    return found


def check_directional_path(table, x, y, x_dif, y_dif, target):
    width = len(table[0])
    height = len(table)
    if len(target) == 0:
        return 1
    elif (0 <= x + x_dif and x + x_dif < width and 0 <= y + y_dif and y + y_dif < height) and (puzzle[y + y_dif][x + x_dif] == target[0]):
        return check_directional_path(table, x + x_dif, y + y_dif, x_dif, y_dif, target[1:])
        # go to the direction again. Look for the next letter
    # dead end
    else:
        return 0



for r in range(height):
    for c in range(width):
        if puzzle[r][c] == word[0]:
            # print(puzzle[r][c])
            total += available_directions(puzzle, c, r, word[1:])
            # print(total)

print(total)

"""
Sample Input 1
MENU
5
7
F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S

Output for Sample Input 1
3

Sample Input 2
NATURE
6
9
N A T S F E G Q N
S A I B M R H F A
C F T J C U C L T
K B H U P T A N U
D P R R R J D I R
I E E K M E G B E
Output for Sample Input 2
4

hejo
4
4
h e j d
e e x o
j d j w
s o e o
"""

"""def search(table, y, x, target, options):
#current position in table (y, x) bc it's a list and first is the row. Position controls possible directions to check.
    width = len(table[0])
    height = len(table)

    if len(target) == 1:
        print(options)
        return 1, options #only 1 option
    # For the 'downright' diagonal
    elif (x + 1 < width and y + 1 < height and "downright" in options) and (puzzle[y + 1][x + 1] == target[1]):
        return search(table, y+1, x+1, target[1:], ["downright"])
    # For the 'downleft' diagonal
    elif (x - 1 >= 0 and y + 1 < height and "downleft" in options) and (puzzle[y + 1][x - 1] == target[1]):
        return search(table, y+1, x-1, target[1:], ["downleft"])
    # For the 'upleft' diagonal
    elif (x - 1 >= 0 and y - 1 >= 0 and "upleft" in options) and puzzle[y - 1][x - 1] == target[1]:
        return search(table, y-1, x-1, target[1:], ["upleft"])
    # For the 'upright' diagonal
    elif (x + 1 < width and y - 1 >= 0 and "upright" in options) and (puzzle[y - 1][x + 1] == target[1]):
        return search(table, y+1, x+1, target[1:], ["upright"])
    else:
        print(options)
        return 0, options #nowhere to go

for h in range(height):
    for w in range(width):
        if puzzle[h][w] == word[0]:

            list_directions = ["upright", "upleft", "downleft", "downright"]
            increase, list_directions = search(puzzle, h, w, word, list_directions)
            total+=increase
            while len(list_directions) == 1: #if solution found remove that and find another until none left
                list_directions = list_directions.remove(list_directions[0])
                increase, list_directions = search(puzzle, h, w, word, list_directions)
                total+=increase"""
