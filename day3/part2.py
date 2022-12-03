# day 3
# part 2
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')

lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

both_compartments = []

totals = []

# a-z: 1-26...ASCII: 97-122...ord(_) - 96 if ord(_) > 96 else ord(_) - 38
# A-Z: 27-52...ASCII: 65-90
i = 0
while i < len(lines):
    first = lines[i]
    second = lines[i+1]
    third = lines[i+2]
    #both_compartments.append(list(set(first).intersection(set(second)))[0])
    a = list(set(first).intersection(set(second).intersection(set(third))))[0]
    totals.append(ord(a) - 96 if ord(a) > 96 else ord(a) - 38)
    i = i+3

print(sum(totals))
