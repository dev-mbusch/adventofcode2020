"""
https://adventofcode.com/2020/day/5
"""

from collections import deque

# test_input = 'FBFBBFFRLR'

with open(r'../input_files/day05_input_mb.txt', 'r') as fh:
    boarding_passes = fh.read().splitlines()

def lookup_row(input):
    candidate_rows = 128
    row_deque = deque(range(128))

    for i, char in enumerate(input):
        candidate_rows = candidate_rows // 2

        if char == 'F':
            for i in range(candidate_rows):
                row_deque.pop()

        elif char == 'B':
            for i in range(candidate_rows):
                row_deque.popleft()

    return row_deque[0]

def lookup_col(input):
    candidate_cols = 8
    col_deque = deque(range(8))

    for char in input:
        candidate_cols = candidate_cols // 2

        if char == 'R':
            for i in range(candidate_cols):
                col_deque.popleft()

        elif char == 'L':
            for i in range(candidate_cols):
                col_deque.pop()

    return col_deque[0]

# Part One
seat_ids = [lookup_row(i[0:7]) * 8 + lookup_col(i[7:]) for i in boarding_passes]

# Find max SeatID
print(f'Part One - {max(seat_ids) = }.')

# Part Two
# All numbers between 54 and 930
reference = [x for x in range(54, 931)]

# Find Missing ID
missing_id = 0
for n in reference:
    if n not in seat_ids:
        missing_id = n

print(f'Part Two - {missing_id = }.')
