"""
Sample Input
AA AB
AB BB
B AA
4 AB AAAB
Possible Output for Sample Input
2 1 BB
3 1 AAB
3 3 AAAA
1 3 AAAB

Use definition to check all possibilities for up to given num of steps
- if reached output list it took to get there
- do whichever fills more criteria (length, a's, b's)
"""
combinations = []
for i in range(3):
    combinations.append(input().split(" "))
user_input = input().split()

req_step = int(user_input[0])
start = user_input[1]
end = user_input[2]

def find_idx_substring(full_string, substring):
    return [ i for i in range(len(full_string)) if full_string.startswith(substring, i)]

def find_step(current, steps_left, combinations, steps_list):
    #print(current, steps_left, steps)
    #if steps are not used up go again
    if steps_left == 0:
        return current == end
    else:
        for combination_idx in range(len(combinations)):
            replacement_option = combinations[combination_idx]
            for idx in find_idx_substring(current, replacement_option[0]):
                new_text = current[:idx] + replacement_option[1]
                remainder = len(current) - idx - len(replacement_option[0])
                if remainder > 0:
                    new_text = new_text + current[-remainder:]
                found = find_step(new_text, steps_left-1, combinations, steps_list)
                if found:
                    steps_list.append("{0} {1} {2}".format(combination_idx+1, idx+1, new_text))
                    return True
                #return found
        return False

        #for every location
        #for letter in range(len(current)):
            #use every change
            #for combination in range(len(combinations)):
                #check if it has requirements to work
                #if (letter+len(combinations[combination][0]) <= len(current) ) and (  current[letter:  letter+len(combinations[combination][0])  ] == combinations[combination][0]  ):
                    #the combination part is transformed
                    #current = current[:letter] + combinations[combination][1] + current[letter + len(combinations[combination][0]):]
#                    steps.append([combination+1, letter+1, current])
                    #if find_step(current, steps_left - 1, steps) == True:
                        #steps.append([combination + 1, letter + 1, current])
                        #return True


step_list = []
find_step(start, req_step, combinations, step_list)
step_list.reverse()
print("\n".join(step_list))