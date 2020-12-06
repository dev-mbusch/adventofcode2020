"""
https://adventofcode.com/2020/day/6
"""

with open(r'../input_files/day06_input_mb.txt', 'r') as fh:

    input = fh.read().split('\n\n')

groups = [line.replace('\n', ' ') for line in input]
groups = [line.replace(' ', '') for line in groups]
groups = [set(group) for group in groups]
count = [len(group) for group in groups]

# Part One
print(f'Part One - Sum of answered Questions: {sum(count) = }.')

# Part Two
groups_2 = [[set(item) for item in group.split('\n')] for group in input]

# Compute Intersection of sets for each group
groups_2_inter = [set.intersection(*group) for group in groups_2]

count_2 = sum([len(group) for group in groups_2_inter])

print(f'Part Two - Sum of questions everyone answered: {count_2 = }.')
