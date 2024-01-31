"""
S = 3P + K
K is input
"""
def shift(alpha, shifts, letter, place):
    position = alpha.index(letter)
    #print(position)
    new_position = position - (3*(place) + shifts)
    #print(new_position)
    while new_position < 0:
        new_position+=26
    #print(new_position)
    new_position = alpha[new_position]
    #print(new_position)
    return new_position
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num_shift = int(input())
word = input()
letters = []
for i in range(len(word)):
    letters.append(word[i])
#print(letters)
for i in range(len(letters)):
    letters[i] = shift(alphabet, num_shift, word[i].capitalize(), i+1)

    #letters.append(word[i].capitalize())
print("".join(letters))
#fxab = zoom