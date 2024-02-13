"""
LLSLM becomes 11312

2


"""
books = []
books_input = input().replace('L', '1').replace('M', '2').replace('S', '3')
for i in range(len(books_input)):
    books.append(int(books_input[i]))
ls = books.count(1)
ms = books.count(2)
ss = books.count(3)
l = []
for i in range(ls):
    l.append(books[0])
    books = books[1:]
m = []
for i in range(ms):
    m.append(books[0])
    books = books[1:]
s = []
for i in range(ss):
    s.append(books[0])
    books = books[1:]

actions = 0
while (ls != l.count(1)) or (ms != m.count(2)) or (ss != s.count(3)):
    if 2 in l and 1 in m:
        l[l.index(2)] = 1
        m[m.index(1)] = 2
    elif 3 in l and 1 in s:
        l[l.index(3)] = 1
        s[s.index(1)] = 3
    elif 3 in m and 2 in s:
        m[m.index(3)] = 2
        s[s.index(2)] = 3

    elif 1 in m: #since other cases are taken care of, only this is left
        m[m.index(1)] = 3
        l[l.index(3)] = 1
    elif 1 in s:
        s[s.index(1)] = 2
        l[l.index(2)] = 1
    else:
        print("ERROR")
#    print(l, m, s, l.count(1), m.count(2), s.count(3))
    actions+=1

print(actions)


"""
swap = 0
s_has = [] #3
m_has = [] #2
l_has = [] #1
#what each section has which is not supposed to be there
for i in range(len(books)):
    if target[i] != books[i]:
        if target[i] == 1:
            l_has.append(books[i])
        elif target[i] == 2:
            m_has.append(books[i])
        elif target[i] == 3:
            s_has.append(books[i])

#total without trading places
total = len(s_has) + len(m_has) + len(l_has)

#how each section can trade
#if section has each others
swap = 0
all = [l_has, m_has, s_has]
swap+=min(l_has.count(2), m_has.count(1))
swap+=min(l_has.count(3), s_has.count(1))
swap+=min(m_has.count(3), s_has.count(2))

print(total-swap)
"""

