# read input file and store each line as element in list

# TODO: open sollte man IMMER mit sog. Context Manager nutzen.
# See --> https://www.geeksforgeeks.org/context-manager-in-python/
file = open("input_files\day01_input_mp.txt")
lines = file.read().split("\n")
file.close()

# print(lines)

# TODO: Hier hast du völlig Recht, allerdings kannst du dir den Zwischenschritt sparen.
# Also guck dir mal meinen Code an. Da nutze ich sog. "List Comprehension"
# See --> https://realpython.com/list-comprehension-python/
# convert list values to integers. might be handy later.
numbers = list(map(int, lines))

# Part 1

def find_two_magic_summands(numbers: list, magic_sum: int):
for i in range(len(numbers)):                               # TODO: Das hier ist ein NoNo (in Python)! Du iterierst über ein Iterable, also in diesem Fall eine bereits vorhandene, bekannte Liste. Deshalb kannst du direkt über die Liste laufen a la for item in list: bzw. wenn du eine Zählvariable brauchst for i, item in enumerate(liste):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == magic_sum:
                summand_1 = numbers[i]
                summand_2 = numbers[j]
                # print(numbers[i], numbers[j])
                break
    return summand_1, summand_2

two_summands = find_two_magic_summands(numbers, 2020)

print(two_summands[0] * two_summands[1])

# Part 2

def find_three_magic_summands(numbers: list, magic_sum: int):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(i+2, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == magic_sum:
                    summand_1 = numbers[i]
                    summand_2 = numbers[j]
                    summand_3 = numbers[k]
                    # print(numbers[i], numbers[j])
                    break
    return summand_1, summand_2, summand_3


three_summands = find_three_magic_summands(numbers, 2020)

print(three_summands[0] * three_summands[1] * three_summands[2])

# test case

# test_numbers = [1721,979,366,299,675]
# for i in range(len(test_numbers)):
#     for j in range(i+1, len(test_numbers)):
#         for k in range(i+2, len(test_numbers)):
#             if test_numbers[i] + test_numbers[j] + test_numbers[k] == 2020:
#                 test_summand_1 = test_numbers[i]
#                 test_summand_2 = test_numbers[j]
#                 test_summand_3 = test_numbers[k]
#                 print(test_numbers[i], test_numbers[j], test_numbers[k])
#                 break



