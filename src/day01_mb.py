"""
https://adventofcode.com/2020/day/1
"""

def two_add_up(inputs, target=2020):
    inputs_two = inputs[:]
    inputs_two.sort(reverse=True)

    for first_input in inputs_two:
        temp = first_input
        for second_input in inputs_two:
            if target - temp - second_input == 0:
                result = temp * second_input
                return result


def three_add_up(inputs, target=2020):
    inputs_three = inputs[:]
    inputs_three.sort(reverse=True)

    for first_input in inputs_three:
        temp1 = first_input
        for second_input in inputs_three:
            temp2 = second_input
            for third_input in inputs_three:
                if target - temp1 - temp2 - third_input == 0:
                    result = temp1 * temp2 * third_input
                    return result

# Test Case Part One
test_input = [1721, 979, 366, 299, 675, 1456]
assert two_add_up(test_input) == 514579

# Test Case Part Two
test_input = [1721, 979, 366, 299, 675, 1456]
assert three_add_up(test_input) == 241861950


if __name__ == '__main__':
    with open('../input_files/day01_input_mb.txt', 'r') as fh:
        inputs = [int(line.strip()) for line in fh.readlines()]
        # print(inputs)
    print(two_add_up(inputs))
    print(three_add_up(inputs))
