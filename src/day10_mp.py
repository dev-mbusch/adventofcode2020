with open("input_files\day10_input_mp.txt") as file:
    input = [int(value) for value in file.read().split("\n")]


# input = '''28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3'''

# input = input.split("\n")
# input = [int(value) for value in input]
# print(input)

input.sort()

jolt_differences = [-1*(input[count-1] - jolt) for count, jolt in enumerate(input)]

# add charging outlet
jolt_differences[0] = input[0]

# add device's built in adapter
jolt_differences.append(3)

print("Solution part 1: ", jolt_differences.count(1) * jolt_differences.count(3))


# Part 2
# cut list into sublists with only 1 step jolt differences
subsequences = []
start = 0
end = int()
for count, difference in enumerate(jolt_differences):
    if difference == 3:
        end = count
        subsequences.append(jolt_differences[start:end])
        start = end

# number of combinations matches fibonacci sequence
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

count_ones = []
for subsequence in subsequences:
    count_ones.append(subsequence.count(1))

solution2 = 1

for value in count_ones:
    if value > 0:
        solution2 *= max(tribonacci([0,0,1], value + 3))

print("Solution part 2: ", solution2)