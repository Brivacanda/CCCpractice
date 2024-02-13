"""
Sample Input 1
ABCCDEABAA
ABCDE
Output for Sample Input 1
yes

Sample Input 2
ABCDDEBCAB
ABA
Output for Sample Input 2
no
"""
main = input("")
target = input("")
variations = []
for i in range(len(target)):
    target = target[1:]+target[0]
    variations.append(target)
innit = "no"
for i in range(len(variations)):
    if variations[i] in main:
        innit = "yes"
print(innit)