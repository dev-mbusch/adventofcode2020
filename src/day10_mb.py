"""
https://adventofcode.com/2020/day/10
"""
from itertools import tee

with open(r'../input_files/day10_input_mb.txt', 'r') as fh:
    raw_input = [int(line) for line in fh.read().strip().splitlines()]

adapters = [0] + sorted(raw_input) + [max(raw_input) + 3]

def pairwise(iterable):
    """See Itertools Recipes --> https://docs.python.org/3/library/itertools.html"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def compute_part1(input):
    counter_1 = 0
    counter_3 = 0
    for x, y in pairwise(input):
        if y - x == 1:
            counter_1 += 1
        if y - x == 3:
            counter_3 += 1
        if y - x > 3:
            print(f'{y - x = }')
            break
    return counter_1 * counter_3

print(f'Part One - Result: {compute_part1(adapters) = }.')
