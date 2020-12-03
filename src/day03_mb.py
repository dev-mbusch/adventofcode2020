"""
https://adventofcode.com/2020/day/3
"""

from collections import namedtuple

# Read Input
with open(r'../input_files/day03_input_mb.txt', 'r') as fh:
    lines = [line.strip('\n') for line in fh.readlines()]

Instructions = namedtuple('Instructions', ['right', 'down'])

instructions = [
    Instructions(1, 1),
    Instructions(3, 1),
    Instructions(5, 1),
    Instructions(7, 1),
    Instructions(1, 2)
    ]

def compute_tree_collisions(lines, right, down):
    offset = 0
    trees = 0
    for i, line in enumerate(lines):
        if i == 0 or i % down != 0:
            continue
        else:
            offset += right
            if offset >= len(line):
                offset = offset - len(line)
            if line[offset] == '#':
                trees += 1
    return trees

# Part Two
collisions = 1
for instruction in instructions:
    collisions *= compute_tree_collisions(lines,instruction.right, instruction.down)

print(f'Part One - Count of collisions: {compute_tree_collisions(lines, 3, 1 )}')
print(f'Part Two - Count of collisions: {collisions:_}')
