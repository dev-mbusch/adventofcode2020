import re


def clean_passport_batch(batch_file):
    '''This method cleans a batch of passports (in one string) and provides a cleaned list of passports with a single string in one line per passport.'''
    passports_dirty = batch_file.read().split('\n\n')
    passports = [passp.replace('\n',' ') for passp in passports_dirty]
    return passports

def check_passport(expected_fields, passport):
    '''This method checks whether a password contains all mandatory fields and returns a boolean: True for valid, False for invalid passports.'''
    matched_fields = re.findall(r"(?=("+'|'.join(expected_fields)+r"))",passport)
    is_valid = set(matched_fields).issuperset(set(expected_fields))
    return is_valid

def check_passport_v2(expected_fields, passport):
    valid_field_counter = 0
    # iterate over patterns from expected fields
    for field in expected_fields:
        # check whether pattern is in passport
        if re.search(field, passport):
            valid_field_counter += 1
    if valid_field_counter == len(expected_fields_strict):
        return True
    else:
        return False


if __name__ == '__main__':
    # reading input file
    file = open("input_files\day04_input_mp.txt")
    passports = clean_passport_batch(file)
    file.close()

    # creating list with mandatory passport fields
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    expected_fields_strict = [r"byr:(19[2-9]\d|200[0-2])(\s|$)", r"iyr:(201[0-9]|2020)(\s|$)", r"eyr:(202[0-9]|2030)(\s|$)", r"hgt:((((1[5-8]\d)|19[0-3])cm)|(((59)|(6\d)|(7[0-6]))in))(\s|$)", r"hcl:#[0-9a-f]{6}(\s|$)", r"ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)", r"pid:\d{9}(\s|$)"]


    # PART 1

    # counter initialization
    number_of_valid_passports = 0

    # looping through the list of passports, checking for validity. Counter increases for each valid passport.
    for passport in passports:
        if check_passport(expected_fields, passport) == True:
            number_of_valid_passports += 1

    print(number_of_valid_passports)

    # # PART 2

    # # counter initialization
    strictly_valid_passports = 0

    for passport in passports:
        if check_passport_v2(expected_fields_strict, passport) == True:
            strictly_valid_passports += 1

    print(strictly_valid_passports)

