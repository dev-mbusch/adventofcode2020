"""
https://adventofcode.com/2020/day/4
"""

import re

# Read Input File
with open(r'../input_files/day04_input_mb.txt', 'r') as fh:
    lines = [line.strip('\n') for line in fh.readlines()]

def process_data(lines):
    """Processes the input file and generates a list of individual passports."""
    passport = []
    passports = []
    for item in lines:
        if item == '':
            temp = passport[:]
            passport.clear()
            passports.append(temp)
            continue
        else:
            passport.append(item)

    return passports

def create_passport_records(passport_lines):
    """Takes a list of passport lines and creates a list of concatenated passports."""
    passporttexts = []

    for passport in passport_lines:
        pp_text = ''
        for i, line in enumerate(passport):
            if i != len(passport):
                pp_text += line + ' '
            else:
                pp_text += line

        passporttexts.append(pp_text)
        # print(pp_text)
    return passporttexts

def check_passport_validity(passport):
    """Checks the validity of the passport."""
    counter = 0

    fields = passport.split(' ')

    fields = [x.strip() for x in fields]

    if '' in fields:
        fields.remove('')

    # fields_set = set(fields)

    # if ('cid:' in fields_set and len(fields_set) == 7) or ('cid:' not in fields_set and len(fields_set) > 7):
    #     return True
    # else:
    #     return False
    # # return fields
    # # return len(fields)

    validity = {
        'byr:',
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:',
        # 'cid:',
    }



    for field in validity:
        if field in passport or field == 'cid:':
            counter += 1

    if counter >= 7:
        return True
    else:
        return False


# Use to Generate List of Passports
passport_lines = process_data(lines)
passports = create_passport_records(passport_lines)

# for passport in passports:
#     print(check_passport_validity(passport))

valid_passports = 0
for passport in passports:
    if check_passport_validity(passport):
        valid_passports += 1
print(valid_passports)
