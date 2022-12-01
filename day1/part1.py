# day 1
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

print('max calories: {}'.format(max(totals)))