"""
https://adventofcode.com/2020/day/13
"""

with open(r'../input_files/day13_input_mb.txt', 'r') as fh:
    raw_input = fh.read().splitlines()
    input_departure = int(raw_input[0])
    input_busses = sorted([int(x) for x in raw_input[1].split(',') if x != 'x'])


def find_early_departure(departure, busses):
    missed_by_min = [departure % bus for bus in busses]
    waiting_minutes = {bus: bus - missed_minutes for bus, missed_minutes in zip(busses, missed_by_min)}

    bus = min(busses, key=lambda bus: waiting_minutes[bus])
    return bus * waiting_minutes[bus]

# Test Case Part one
TEST = """939
7,13,x,x,59,x,31,19"""

TEST_INPUT = TEST.splitlines()
departure_test = int(TEST_INPUT[0])
busses_test = sorted([int(x) for x in TEST_INPUT[1].split(',') if x != 'x'])

assert find_early_departure(departure_test, busses_test) == 295

# Results
print(f'Part One - Results: {find_early_departure(input_departure, input_busses) = }.')
