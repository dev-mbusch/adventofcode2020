"""
https://adventofcode.com/2020/day/9
"""

from itertools import combinations

with open(r'../input_files/day09_input_mb.txt', 'r') as fh:
    raw_input = [int(num) for num in fh.read().strip().splitlines()]

test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".strip().splitlines()
test_input = [int(x) for x in test_input]

# test_2 = raw_input[:622]

# test_target = 373803594

def compute_combinations(input, target_number):

    for i, number in enumerate(input):
        j = i
        total = number
        while total < target_number:
            j += 1
            total += input[j]

        if total == target_number:
            slice = input[i:j+1]

            return min(slice) + max(slice)


def hack(numbers, steps):
    i = 0
    start = 0
    end = steps
    checkpoint = steps
    sum_min_max = 0

    while True:
        # print(f'{i = }')

        if i == 0:
            check = numbers[checkpoint]
            # print(f'{check = }')

            combos = combos = list(combinations(numbers[start:end], 2))
            # print(combos)
            # print(numbers[start:end])
            combos = [check - sum(item) == 0 for item in combos]
            # print(combos)
            if not any(combos):
                # sum_min_max = sum(min(numbers[start:end]), max(numbers[start:end]))
                break
            checkpoint += 1
            # print(f'{checkpoint = }')
            start = checkpoint - steps
            end = checkpoint

        else:
            check = numbers[checkpoint]
            # print(f'{check = }')
            # print(f'{start = }')
            # print(f'{end = }')
            combos = list(combinations(numbers[start:end], 2))
            # print(len(numbers[start:end]))
            # print(numbers[start:end])
            # print(combos)
            combos = [check - sum(item) == 0 for item in combos]
            # print(combos)
            if not any(combos):
                # sum_min_max = compute_combinations(numbers[:checkpoint], check)
                break
            checkpoint += 1
            # print(f'{checkpoint = }')
            start = checkpoint - steps
            end = checkpoint

        i += 1

    return check, checkpoint
