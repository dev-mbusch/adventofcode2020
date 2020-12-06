# read file and create list, one item per ticket
with open("input_files\day06_input_mp.txt") as file:
    forms_one_line = file.read().split("\n\n")

# # Part 1
single_forms = [form.replace("\n", "") for form in forms_one_line]

number_of_yes = [len(set(form)) for form in single_forms]

print(sum(number_of_yes))

# Part 2
group_forms = [form.split("\n") for form in forms_one_line]
intersec_of_sets = []
for i in range(0, len(group_forms)):
    for j in range(0, len(group_forms[i])):
        group_forms[i][j] = set(group_forms[i][j])
    if len(group_forms[i]) > 1:
        intersec_of_sets.append(len(set.intersection(*group_forms[i])))
    else:
        intersec_of_sets.append(len(group_forms[i][j]))

print(sum(intersec_of_sets))