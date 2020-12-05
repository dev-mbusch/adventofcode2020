"""
https://adventofcode.com/2020/day/4
"""

# Read Input File
with open(r'../input_files/day04_input_mb.txt', 'r') as fh:
    raw_input = fh.read().split('\n\n')
    passports = [line.replace('\n', ' ') for line in raw_input]

requirements = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
]

def check_passport_validity(passports, required_fields):
    valid_passports = 0
    for i, passport in enumerate(passports):
        requirements_met = 0
        # print(f'{i = } {passport = }')
        for j, field in enumerate(required_fields):
            # print(f'{j = } {field = }')
            if field in passport:
                requirements_met += 1
                # print(f'{requirements_met = }')
        if requirements_met == 7:
            valid_passports += 1
            # print(f'{valid_passports =}')
    return valid_passports

# Part One
print(f'Part one - Number of valid passports: {check_passport_validity(passports, requirements)}')
