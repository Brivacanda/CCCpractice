#faster more complicated way to start adding from the end so nothing is replaced.
rows = int(input())
columns = int(input())

actions = []
num_actions = int(input())
for i in range(num_actions):
    actions.append(input().split(" "))
#let 1 represent black and -1 represent gold
table = []
for i in range(rows):
    table.append([1]*columns)

for i in range(len(actions)):
    action = actions[i][0]
    pos = int(actions[i][1])-1
    if action == "R":
        table[pos] = [v*-1 for v in table[pos]]
    elif action == "C":
        for r in range(rows):
            table[r][pos] = table[r][pos]*-1

gold = 0
for i in range(rows):
    gold+=table[i].count(-1)
print(gold)


"""
3
3
2
R 1
C 1
"""