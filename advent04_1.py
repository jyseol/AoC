#!/usr/bin/env/ python3

with open("advent04.in", "r") as f:
    input = f.read().strip()


### Separate input by line
### Becomes a list of lines
input = input.split('\n')

### Split each word in a line
### Becomes a list of items in a line
final = 0
for each_line in input:
    line_list = each_line.split(' ')
    counteach = 0
    for each in line_list:
        counteach += line_list.count(each)
    if counteach == len(line_list):
        final += 1

print ("The number of valid passphrases are:", final)
