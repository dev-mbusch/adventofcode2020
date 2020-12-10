with open("input_files\day08_input_mp_txt") as file:
    instructions = file.read().split("\n")

# part 1

cleaned_instructions = [instruction.split(" ") for instruction in instructions]
passed_instructions = set()
accumulator = 0
current_position = 0

while current_position not in passed_instructions:
    if current_position not in passed_instructions:
        passed_instructions.add(current_position)
        if cleaned_instructions[current_position][0] == "acc":
            accumulator += int(cleaned_instructions[current_position][1])
            current_position += 1
        elif cleaned_instructions[current_position][0] == "jmp":
            current_position = current_position + int(cleaned_instructions[current_position][1])
        else:
            current_position += 1

print(accumulator)

# part 2

for i in range(0, len(instructions)-1):
    # set of instructions to keep track of possible infinite loops
    passed_instructions = set()
    accumulator = 0
    current_position = 0
    # switch instructions routine
    if cleaned_instructions[i][0] == "nop":
        cleaned_instructions[i][0] = "jmp"
    elif cleaned_instructions[i][0] == "jmp":
        cleaned_instructions[i][0] = "nop"
    # do this as long as the instructions has not been followed already and as long as we did not followed the very last instruction
    while current_position not in passed_instructions and len(cleaned_instructions)-1 not in passed_instructions:
        passed_instructions.add(current_position)
        if cleaned_instructions[current_position][0] == "acc":
            accumulator += int(cleaned_instructions[current_position][1])
            current_position += 1
        elif cleaned_instructions[current_position][0] == "jmp":
            current_position = current_position + int(cleaned_instructions[current_position][1])
        else:
            current_position += 1
    # print solution and stop routine in case we issued the last instruction of the input file
    if len(cleaned_instructions)-1 in passed_instructions:
        print("accumulator",accumulator)
        break
    
    # revert changes in instructions before next iteration starts
    if cleaned_instructions[i][0] == "nop":
        cleaned_instructions[i][0] = "jmp"
    elif cleaned_instructions[i][0] == "jmp":
        cleaned_instructions[i][0] = "nop"