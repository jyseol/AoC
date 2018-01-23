#!/usr/bin/env/ python3

with open("advent04.in", "r") as f:
    input = f.read().strip()

### Separate input by line
### Becomes a list of lines
input = input.split('\n')

### Dictionary of the alphabet
alpha_val = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, \
'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, \
'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, \
'x':24, 'y':25, 'z':26}

### Split each word in a line
### Becomes a list of items in a line
final = 0
for each_line in input:
    line_list = each_line.split(' ')
    line_int = []
    for each in line_list:
        each_val = 0
        for letter in each:
            each_val += alpha_val[letter]
        line_int.append(each_val)
    line_int.sort()
    indicatee = "works"
    for each in range(0, len(line_int)-1):
        if indicatee == "wrong":
            break
        elif line_int[each] == line_int[each+1]:
            indicatee = "wrong"
    if indicatee == "works":
        final += 1

print ("The number of valid passphrases are:", final)
### Answer is NOT 209
