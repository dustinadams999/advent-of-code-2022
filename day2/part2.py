# day 2
# part 2
import sys
from IPython import embed as shell

outcomes = {
    'A X': 3, # 0, I choose Z, add 3
    'A Y': 4, # 3, I choose X, add 1
    'A Z': 8, # 6, I choose Y, add 2
    'B X': 1, # 0, I choose X, add 1
    'B Y': 5, # 3, I choose Y, add 2
    'B Z': 9, # 6, I choose Z, add 3
    'C X': 2, # 0, I choose Y, add 2
    'C Y': 6, # 3, I choose Z, add 3
    'C Z': 7, # 6, I choose X, add 1
}

f = open(sys.argv[1], 'r')

lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

totals = []

for line in lines:
    totals.append(outcomes[line])

print(sum(totals))