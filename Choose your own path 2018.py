"""
Sample Input 2
3
2 2 3
0
1 1
Output for Sample Input 2
Y
2

Sample Input 3
7
2 2 3
1 4
3 7 6 1
1 5
2 4 7
1 1
0
"""
num_pages = int(input())
pages = []
for i in range(num_pages):
    pages.append([int(v) for v in input().split(" ")[1:]])

"""
- start at first page
- iteration for each branch
    - add 1 to steps for each iteration
    - paths are the possible movements from the page (list)
        - when no paths return total steps to get there
            output least steps
    - when arriving at a page add to list
        - check list for each page to see if all are reached
    - if paage visiting is alr visited dont go there
"""
pages_visited = [1]
min_steps = []
def path(cur_page, steps, cur_visited):
    #if no more options. This means it has ended.
    options = pages[cur_page] #list of possible pages to go to
    if len(options) == 0:
        return steps

    for p in range(len(options)): #for each page we can visit from the current one
        #if already visited
        if str(options[p]) in cur_visited:
            return -1
        else:
            #add to visited
            pages_visited.append(options[p])
            #go to that page to find out which pages are visited
            #find num steps taken
            #print(cur_visited)
            min_steps.append(path(options[p]-1, steps+1, cur_visited+str(options[p])) )
    return -1
path(0, 1, "1")
min_steps.sort()
while -1 in min_steps:
    min_steps.remove(-1)

#print("min steps:", min_steps,"\npages visited:", pages_visited)


all_visited = True
for i in range(num_pages):
    if i+1 not in pages_visited:
        all_visited = False
if all_visited:
    print("Y")
else:
    print("N")

if len(min_steps) == 0:
    print(1)
else:
    print(min_steps[0])
