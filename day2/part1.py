# day 2
# part 1
import sys

outcomes = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

f = open(sys.argv[1], 'r')

lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

totals = []

for line in lines:
    totals.append(outcomes[line] + outcomes[line[2]])

print(sum(totals))