"""
- Check each square
- expand diagonally bottom right
- stop when encountering tree

- input


- loop per row
    - loop per column
        - expand
            - while not encountering tree add to area checked
                How to check
                - for i in range (start, x (how far horizontally))
                - make column for each x. loop for x (bc square)
                    - make list of columns and check if tree inside. if not update biggest to x^2/xy
    - stop when reaching edge (x or y = width or length)
if too slow make it so that we start checking for tree from the biggest square
"""
size = int(input())
num_trees = int(input())
map = []
#gets the map with 0 being empty and 1 being tree
for i in range(size):
    map.append([0]*size)
#map is set of rows with same num of columns as rows
for i in range(num_trees):
    get_tree = input()
    get_tree = [int(v) for v in get_tree.split(" ")]
    #first is row/y then it is column/x
    map[get_tree[0]-1][get_tree[1]-1] = 1
#print(map)

def tree_check(tree_locations, x, y, size): #x y's of current every tile of current square, size should start at 1
    max_distance = len(tree_locations[0])
    new_locations = []
    #if doesn't go out of bounds
    if x[-1]+1 < max_distance and y[-1]+1 < max_distance:
        x.append(x[-1]+1)
        y.append(y[-1]+1)
        for i in range(len(x)):
            new_locations.append(tree_locations[y[-1]][x[i]]) #new row included below it as y is increased and all xplus the corner oneis included
            new_locations.append(tree_locations[y[i]][x[-1]]) #y[i] just column to the right and x[-1] shifts it so its new bc we increased b4
        if 1 in new_locations:
            return size #end bc cant expand anymore
        else: #if it can still expand
            #expand
            return tree_check(tree_locations, x, y, size+1)
    else: #if at edge of the map
        #return current size
        return size

max_size = 0
for row in range(size):
    for column in range(size):
        if map[row][column] != 1:
            new_size = tree_check(map, [column], [row], 1)
            if new_size > max_size:
                max_size = new_size

print(max_size)

"""
Sample Input 1
5
1
2 4
Output for Sample Input 1
3

Sample Input 2
15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14
Output for Sample Input 2
7
"""