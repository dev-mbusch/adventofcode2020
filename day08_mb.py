"""
https://adventofcode.com/2020/day/8
"""

from collections import namedtuple

Instructions = namedtuple('Instructions', ['operation', 'argument'])
accumulator = 0
instructions_completed = []

with open(r'./input_files/day08_input_mb.txt', 'r') as fh:
    raw_input = [line for line in fh.read().splitlines()]

raw_input = [line.split(' ') for line in raw_input[0:11]]
instructions = [ Instructions(item[0], int(item[1])) for item in raw_input ]

for i, instruction in enumerate(instructions):
    instructions_completed.append(i)
    if instruction.operation == 'nop':
        print(f'{instruction.operation = } so nothing to do here.')
        continue
    elif instruction.operation == 'acc':
        accumulator += instruction.argument
        print(f'{instruction.operation = } so increase `accumulator` to {accumulator}.')
    elif instruction.operation == 'jmp':
        print(f'{instruction.operation = } so jump to instruction {i + instruction.argument}.')
        if (i + instruction.argument) in instructions_completed:
            print(f'Infinite loop detected. Program terminated. {accumulator = }')
            break
