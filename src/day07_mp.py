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