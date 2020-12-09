import re

with open("input_files\day07_input_mp.txt") as file:
    puzzle_input = file.readlines()

color_check = ["shiny gold"]
color_set = set()

for color in color_check:
    #print(color)
    for rule in puzzle_input:
        #print(rule)
        if re.match(r"^(.*)\sbags\scontain\s.*"+color+".*", rule):
            matched_string = re.match(r"^(.*)\sbags\scontain\s.*"+color+".*", rule).group(1)
            if matched_string not in color_set:
                color_set.add(matched_string)
                color_check.append(matched_string)

print(len(color_set))

# Part 2

# test_input = ["shiny gold bags contain 2 dark red bags.",
# "dark red bags contain 2 dark orange bags.",
# "dark orange bags contain 2 dark yellow bags.",
# "dark yellow bags contain 2 dark green bags.",
# "dark green bags contain 2 dark blue bags.",
# "dark blue bags contain 2 dark violet bags.",
# "dark violet bags contain no other bags."]

amount = [1]
contained_bags = ["shiny gold"]

for count, bag in enumerate(contained_bags):
    for rule in puzzle_input:
        if re.match(r"^"+bag+"\sbags\scontain", rule):
            containments = re.findall(r"(\s\d+(?:\s\w+)+\s)", rule)
            containments = [(re.search(r"\d+\s(\D+)", containment.strip()).group(1), re.search(r"(\d+)", containment).group(1)) for containment in containments]
            for containment in containments:
                amount.append(int(containment[1]) * amount[count])
                contained_bags.append(containment[0])

print(sum(amount) - 1)