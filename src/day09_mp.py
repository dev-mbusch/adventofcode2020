with open("input_files\day09_input_mp.txt") as file:
    xmas_stream = file.read().split("\n")

xmas_stream = [int(line) for line in xmas_stream]

# test_input = '''35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576'''.split("\n")

# test_input = [int(line) for line in test_input]
#xmas_stream = test_input

preamble = 25

magic_number = int()

for i in range(preamble,len(xmas_stream)+1):
    sublist = xmas_stream[i-preamble:i]
    if xmas_stream[i] not in set([x+y for x in sublist for y in sublist]):
        print(xmas_stream[i])      
        break

magic_number = xmas_stream[i]

for i in range(0, len(xmas_stream)):
    sum_up = 0
    summand_set = set()
    for number in xmas_stream[i:]:
        if sum_up < magic_number:
            sum_up += number
            summand_set.add(number)
        if sum_up > magic_number:
            break
        if sum_up == magic_number and len(summand_set) >= 2:
            print("min number: ", min(summand_set))
            print("max number: ", max(summand_set))
            print("Solution Part 2: ", min(summand_set)+max(summand_set))
            break