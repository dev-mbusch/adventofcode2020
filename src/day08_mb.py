"""
https://adventofcode.com/2020/day/8
"""

from collections import namedtuple

Instructions = namedtuple('Instructions', ['operation', 'argument'])

with open(r'./input_files/day08_input_mb.txt', 'r') as fh:
    raw_input = [line for line in fh.read().splitlines()]

raw_input = [line.split(' ') for line in raw_input]
instructions = [ Instructions(item[0], int(item[1])) for item in raw_input ]

# Part One
def process(instructions):
    i = 0
    completed = set()
    accumulator = 0


    while True:

        if i in completed:
            break

        completed.add(i)
        op = instructions[i].operation
        arg = instructions[i].argument

        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            offset = arg
            i += offset

    return accumulator

# Part Two
# def process2(instructions):
#     i = 0
#     completed = set()
#     accumulator = 0
#     counter

#     while

