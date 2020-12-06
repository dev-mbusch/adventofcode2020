# read file and create list, one item per ticket
with open("input_files\day06_input_mp.txt") as file:
    forms = file.read().split("\n\n")

forms = [form.replace("\n", "") for form in forms]

number_of_yes = [len(set(form)) for form in forms]

print(sum(number_of_yes))