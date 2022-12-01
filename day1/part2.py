# day 1
# part 2
import sys

f = open(sys.argv[1], 'r')

lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

totals = []

cal_sum = 0
for line in lines:
    if line != '':
        cal_sum += int(line)
    else:
        totals.append(cal_sum)
        cal_sum = 0

# append the last
totals.append(cal_sum)

# sort it
totals.sort(reverse=True)

print('max calories: {}'.format(sum(totals[0:3])))