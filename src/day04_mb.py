"""
https://adventofcode.com/2020/day/4
"""

# Read Input File
with open(r'../input_files/day04_input_mb.txt', 'r') as fh:
    # Generate list of strings from read() and split by empty line (skip last empty line)
    passports = fh.read()[0:-1].split('\n\n')
    # Replace newlines with spaces
    passports = [line.replace('\n', ' ') for line in passports]
    # Split lines by space to get lists of lists
    passports = [item.split(' ') for item in passports]
    passports = [[item.split(':') for item in sublist] for sublist in passports]
    # Convert each passport to a dict with the required fields as keys
    passports = [dict(x) for x in passports]

requirements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', }

def has_required_fields(passport, required_fields):
    """Checks if a passport has all required fields."""

    if set(passport.keys()).issuperset(requirements):
        return True

def is_valid_byr(birthyear):
    """Checks for valid Birth Year."""
    if birthyear.isdigit() and (1920 <= int(birthyear) <= 2002):
        return True
    else:
        return False

def is_valid_iyr(issue_year):
    """Checks for valid Issue Year."""
    if issue_year.isdigit() and (2010 <= int(issue_year) <= 2020):
        return True
    else:
        return False

def is_valid_eyr(experiation_year):
    """Checks for valid Expiration Year."""
    if experiation_year.isdigit() and (2020 <= int(experiation_year) <= 2030):
        return True
    else:
        return False

def is_valid_hgt(height):
    """Checks for valid Height."""
    if 'cm' in height:
        measurement = int(height.split('cm')[0])
        if 150 <= measurement <= 193:
            return True
        else:
            return False
    elif 'in' in height:
        measurement = int(height.split('in')[0])
        if 59 <= measurement <= 76:
            return True
        else:
            return False
    else:
        return False

def is_valid_hcl(hair_color):
    """Checks for valid Hair Color."""
    if len(hair_color) == 7 and hair_color[0] == '#' and set(hair_color[1:]).issubset(set('0123456789abcdef')):
        return True
    else:
        return False

def is_valid_ecl(eye_color):
    """Checks for valid Eye Color."""
    if eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False

def is_valid_pid(passport_id):
    """Checks for valid Passport ID."""
    if passport_id.isdigit() and len(passport_id) == 9:
        return True
    else:
        return False

# Part One
valid_passports_1 = 0
for passport in passports:
    if has_required_fields(passport, requirements):
        valid_passports_1 += 1
print(f'Part One - Number of {valid_passports_1 = }.')

# Part Two
valid_passports_2 = 0
# Filter invalid passports out
passports_all_fields = [x for x in passports if has_required_fields(x, requirements) == True]

for passport in passports_all_fields:
    if all([
        is_valid_byr(passport['byr']),
        is_valid_iyr(passport['iyr']),
        is_valid_eyr(passport['eyr']),
        is_valid_hgt(passport['hgt']),
        is_valid_hcl(passport['hcl']),
        is_valid_ecl(passport['ecl']),
        is_valid_pid(passport['pid'])]
        ):
            valid_passports_2 += 1
print(f'Part Two - Number of {valid_passports_2 = }.')
