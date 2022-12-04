# day 4
# part 1
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')

lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

# if the first min is >= second min, and the first max is <= second max Or vice versa

total = 0

# min_1 -> max_1, min_2 -> max_2
for line in lines:
    min_1 = int(line.split(',')[0].split('-')[0])
    max_1 = int(line.split(',')[0].split('-')[1])
    min_2 = int(line.split(',')[1].split('-')[0])
    max_2 = int(line.split(',')[1].split('-')[1])
    # 2-8,3-7
    if (min_1 >= min_2 and max_1 <= max_2) or (min_2 >= min_1 and max_2 <= max_1):
        total += 1

print(total)