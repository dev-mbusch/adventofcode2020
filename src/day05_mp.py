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

# Solution part 1
# find indices for highest set rows
tickets_with_highest_row = [i for i, value in enumerate(rows) if value == max(rows)]

# user indices to find seat columns of highest seat row
columns_in_highest_row = [columns[i] for i in tickets_with_highest_row]

# compute magic number
solution_part_1 = (rows[tickets_with_highest_row[0]]) * 8 + max(columns_in_highest_row)

print(solution_part_1)

# Solution part 2

# create empty dictionary with row numbers as keys
row_seats = {}
for row in rows:
    row_seats[row] = []

for i in range(0, len(rows)):
    row_seats[rows[i]].append(columns[i])

# getting rid of front and back rows
del row_seats[min(rows)]
del row_seats[max(rows)]

# what is the row with empty seats
for key in row_seats:
    if len(row_seats[key]) < 8:
        my_row = key
        print(key)

# what is my seat column
my_column = {0,1,2,3,4,5,6,7} - set(row_seats[my_row])

# compute seat ID
my_seat_id = my_row * 8 + list(my_column)[0]

print(my_seat_id)