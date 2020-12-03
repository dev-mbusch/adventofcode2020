"""
https://adventofcode.com/2020/day/3
"""

# Read Input
with open(r'../input_files/day03_input_mb.txt', 'r') as fh:
    lines = [line.strip('\n') for line in fh.readlines()]


def compute_tree_collisions(lines, offset_steps):
    offset = 0
    trees = 0
    for i, line in enumerate(lines):
        if i == 0:
            # print(i, '\t', line)
            continue
        else:
            # print(len(line))
            offset += offset_steps
            # print(offset)
            if offset >= len(line):
                offset = offset - len(line)
                # print(offset)
            if line[offset] == '#':
                trees += 1
            # print(i, '\t', line)
    return trees

print(f'Part One - Count of Trees hit: {compute_tree_collisions(lines, 3)}')
