import re

# read file and create list, one item per ticket
with open("input_files\day05_input_mp.txt") as file:
    tickets = file.read().splitlines()

# change letters to bit representation
for i in range(0, len(tickets)):
    tickets[i] = re.sub("B|R", "1", tickets[i])
    tickets[i] = re.sub("L|F", "0", tickets[i])

# create lists for seat rows and seat columns, converting bit representation into integers
rows = [int(x[0:7], 2) for x in tickets]
columns = [int(x[7:10], 2) for x in tickets]

# find indices for highest set rows
tickets_with_highest_row = [i for i, value in enumerate(rows) if value == max(rows)]

# user indices to find seat columns of highest seat row
columns_in_highest_row = [columns[i] for i in tickets_with_highest_row]

# compute magic number
solution_part_1 = (rows[tickets_with_highest_row[0]]) * 8 + max(columns_in_highest_row)

print(solution_part_1)